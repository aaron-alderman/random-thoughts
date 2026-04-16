const { clampNumber, createSettingsPersister, formatNumber } = window.FftHeatmapCommon;
const { createAdaptiveResponseModel } = window.AdaptiveResponseModel;
const { createAdaptiveResponseUi } = window.AdaptiveResponseUi;

const defaultSampleRate = 48000;
const maxOscillatorFrequency = 20000;
const settingsStorageKey = "adaptive-response-lab-settings-v2";
const analysisIntervalMs = 100;
const displayIntervalMs = 400;
const measurementTolerance = 1e-6;
const trackedPeakOffsetLimitHz = 5;
const responseChartPadding = { top: 18, right: 18, bottom: 42, left: 84 };

const ui = createAdaptiveResponseUi({
  measurementTolerance,
  trackedPeakOffsetLimitHz,
  responseChartPadding,
});

const {
  adaptiveSweepEnabledInput,
  amplitudeInput,
  balanceInput,
  exportCsvButton,
  explorePointsInput,
  fftSizeSelect,
  frequencyInput,
  maxDbInput,
  minDbInput,
  refineVisitsInput,
  resetResponseButton,
  responseTab,
  restartSweepButton,
  smoothingInput,
  startButton,
  stopButton,
  sweepEndHzInput,
  sweepLogInput,
  sweepSettleSecondsInput,
  sweepStartHzInput,
  sweepStepSecondsInput,
  toneEnabled,
  waveformTab,
} = ui.elements;

const adaptiveModel = createAdaptiveResponseModel({
  measurementTolerance,
  peakOffsetLimitHz: trackedPeakOffsetLimitHz,
});

let audioContext = null;
let mediaStream = null;
let sourceNode = null;
let analyserNode = null;
let oscillatorNode = null;
let gainNode = null;
let leftGainNode = null;
let rightGainNode = null;
let mergerNode = null;
let analysisTimerId = null;
let displayTimerId = null;

const waveformBufferLength = 2048;
const waveformData = new Float32Array(waveformBufferLength);

let fftFrameData = new Float32Array(1024);
let currentStepAverageData = new Float32Array(1024);
let currentStepFrameCount = 0;
let waveformDirty = true;
let responseDirty = true;
let analysisSettings = null;
let adaptiveSettings = null;

const persistSettings = createSettingsPersister(settingsStorageKey, () => ui.collectSettings(), 150);

function setStatus(text) {
  ui.setStatus(text);
}

function markUiDirty({ waveform = false, response = false } = {}) {
  waveformDirty = waveformDirty || waveform;
  responseDirty = responseDirty || response;
}

function getSampleRate() {
  return audioContext ? audioContext.sampleRate : defaultSampleRate;
}

function loadSettings() {
  try {
    const raw = window.localStorage.getItem(settingsStorageKey);
    if (!raw) {
      return;
    }

    const settings = JSON.parse(raw);
    if (!settings || typeof settings !== "object") {
      return;
    }

    ui.loadSettings(settings);
  } catch (error) {
    console.warn("Unable to load adaptive settings", error);
  }
}

function readAnalysisSettingsFromInputs() {
  let minDb = Number(minDbInput.value);
  let maxDb = Number(maxDbInput.value);

  if (!Number.isFinite(minDb)) minDb = -100;
  if (!Number.isFinite(maxDb)) maxDb = -20;
  if (minDb >= maxDb - 1) minDb = maxDb - 1;

  return {
    fftSize: Math.round(clampNumber(Number(fftSizeSelect.value), 1024, 32768, 2048)),
    smoothing: clampNumber(Number(smoothingInput.value), 0, 0.99, 0.75),
    minDb,
    maxDb,
  };
}

function readAdaptiveSettingsFromInputs() {
  let startHz = clampNumber(Number(sweepStartHzInput.value), 20, maxOscillatorFrequency, 440);
  let endHz = clampNumber(Number(sweepEndHzInput.value), 20, maxOscillatorFrequency, 880);

  if (startHz >= endHz) {
    endHz = Math.min(maxOscillatorFrequency, startHz + 0.1);
  }

  const stepSeconds = clampNumber(Number(sweepStepSecondsInput.value), 0.1, 86400, 8);
  const maxSettleSeconds = Math.max(0, stepSeconds - 0.05);

  return {
    enabled: adaptiveSweepEnabledInput.checked,
    startHz,
    endHz,
    explorePointsPerSeason: Math.round(clampNumber(Number(explorePointsInput.value), 1, 20000, 17)),
    log: sweepLogInput.checked,
    refineVisitsPerSeason: Math.round(clampNumber(Number(refineVisitsInput.value), 0, 20000, 24)),
    stepSeconds,
    settleSeconds: clampNumber(Number(sweepSettleSecondsInput.value), 0, maxSettleSeconds, 0.5),
  };
}

function refreshAnalysisSettings() {
  analysisSettings = readAnalysisSettingsFromInputs();
  return analysisSettings;
}

function refreshAdaptiveSettings() {
  adaptiveSettings = readAdaptiveSettingsFromInputs();
  return adaptiveSettings;
}

function getAnalysisSettings() {
  return analysisSettings ?? refreshAnalysisSettings();
}

function getAdaptiveSettings() {
  return adaptiveSettings ?? refreshAdaptiveSettings();
}

function getFrequencyValue() {
  return clampNumber(Number(frequencyInput.value), 20, maxOscillatorFrequency, 440);
}

function isAdaptiveRunning() {
  return Boolean(audioContext && getAdaptiveSettings().enabled);
}

function measureTrackedResponse(spectrum, drivenFrequency) {
  return adaptiveModel.measureTrackedResponse({
    spectrum,
    drivenFrequency,
    sampleRate: getSampleRate(),
  });
}

function isCurrentStepSettled(currentTime = audioContext ? audioContext.currentTime : 0) {
  return !isAdaptiveRunning() || adaptiveModel.getDwellStartTime() === null
    ? true
    : currentTime - adaptiveModel.getDwellStartTime() >= getAdaptiveSettings().settleSeconds;
}

function getAdaptiveSnapshot() {
  const previewMeasurement =
    currentStepFrameCount > 0
      ? measureTrackedResponse(currentStepAverageData, adaptiveModel.getActiveTargetFrequency())
      : null;

  return adaptiveModel.buildSnapshot({
    settings: getAdaptiveSettings(),
    isRunning: isAdaptiveRunning(),
    previewMeasurement,
    currentStepFrameCount,
    settled: isCurrentStepSettled(),
    manualFrequency: getFrequencyValue(),
  });
}

function resetCurrentStepAverage() {
  currentStepAverageData = new Float32Array(fftFrameData.length);
  currentStepAverageData.fill(getAnalysisSettings().minDb);
  currentStepFrameCount = 0;
}

function reinitializeFftBuffers() {
  fftFrameData = new Float32Array(getAnalysisSettings().fftSize / 2);
  resetCurrentStepAverage();
}

function renderUi({ drawWaveformIfDirtyOnly = false, drawResponseIfDirtyOnly = false } = {}) {
  const snapshot = getAdaptiveSnapshot();
  const elapsedSeconds =
    isAdaptiveRunning() && adaptiveModel.getDwellStartTime() !== null
      ? Math.max(0, audioContext.currentTime - adaptiveModel.getDwellStartTime())
      : 0;

  ui.renderControls({
    analysisSettings: getAnalysisSettings(),
    adaptiveSettings: getAdaptiveSettings(),
    snapshot,
    sampleRate: getSampleRate(),
    currentStepFrameCount,
    isRunning: isAdaptiveRunning(),
    elapsedSeconds,
  });

  if (ui.getActiveView() === "waveform" && (!drawWaveformIfDirtyOnly || waveformDirty)) {
    ui.drawWaveform(waveformData);
    waveformDirty = false;
  }

  if (ui.getActiveView() === "response" && (!drawResponseIfDirtyOnly || responseDirty)) {
    ui.drawResponseCharts({
      snapshot,
      analysisSettings: getAnalysisSettings(),
      adaptiveSettings: getAdaptiveSettings(),
      sampleRate: getSampleRate(),
    });
    responseDirty = false;
  }
}

function applyOscillatorFrequency(frequency) {
  if (!oscillatorNode || !audioContext) {
    return;
  }

  oscillatorNode.frequency.setValueAtTime(frequency, audioContext.currentTime);
}

function syncToneSettings() {
  if (!gainNode || !audioContext) {
    return;
  }

  const now = audioContext.currentTime;
  const amplitude = Number(amplitudeInput.value) / 100;
  const pan = clampNumber(Number(balanceInput.value) / 100, -1, 1, 0);
  const toneFrequency = isAdaptiveRunning() ? adaptiveModel.getActiveTargetFrequency() : getFrequencyValue();
  const angle = ((pan + 1) * Math.PI) / 4;
  const leftGain = (toneEnabled.checked ? amplitude : 0) * Math.cos(angle);
  const rightGain = (toneEnabled.checked ? amplitude : 0) * Math.sin(angle);

  applyOscillatorFrequency(toneFrequency);
  gainNode.gain.setValueAtTime(1, now);
  leftGainNode.gain.setValueAtTime(leftGain, now);
  rightGainNode.gain.setValueAtTime(rightGain, now);
}

function commitFrequencyInput() {
  const frequency = getFrequencyValue();
  frequencyInput.value = formatNumber(frequency, frequency % 1 === 0 ? 0 : 1);

  if (!isAdaptiveRunning()) {
    adaptiveModel.setActiveTargetFrequency(frequency);
    syncToneSettings();
  }

  renderUi();
  persistSettings();
}

function commitDbInputs() {
  let minDb = clampNumber(Number(minDbInput.value), -160, -1, -100);
  let maxDb = clampNumber(Number(maxDbInput.value), -159, 0, -20);

  if (minDb >= maxDb - 1) {
    if (document.activeElement === minDbInput) {
      minDb = maxDb - 1;
    } else {
      maxDb = minDb + 1;
    }
  }

  minDbInput.value = String(Math.round(minDb));
  maxDbInput.value = String(Math.round(maxDb));
  applyAnalysisSettings();
  persistSettings();
}

function commitAdaptiveInputs() {
  refreshAdaptiveSettings();
  const settings = getAdaptiveSettings();
  sweepStartHzInput.value = formatNumber(settings.startHz, settings.startHz % 1 === 0 ? 0 : 1);
  sweepEndHzInput.value = formatNumber(settings.endHz, settings.endHz % 1 === 0 ? 0 : 1);
  explorePointsInput.value = String(settings.explorePointsPerSeason);
  refineVisitsInput.value = String(settings.refineVisitsPerSeason);
  sweepStepSecondsInput.value = formatNumber(settings.stepSeconds, settings.stepSeconds % 1 === 0 ? 0 : 1);
  sweepSettleSecondsInput.value = formatNumber(
    settings.settleSeconds,
    settings.settleSeconds % 1 === 0 ? 0 : 1
  );
  markUiDirty({ response: true });
  renderUi();
  persistSettings();
}

function applyAnalysisSettings() {
  const settings = refreshAnalysisSettings();

  if (analyserNode) {
    if (analyserNode.fftSize !== settings.fftSize) {
      analyserNode.fftSize = settings.fftSize;
      reinitializeFftBuffers();
      clearAdaptiveData(isAdaptiveRunning());
    }

    analyserNode.minDecibels = settings.minDb;
    analyserNode.maxDecibels = settings.maxDb;
    analyserNode.smoothingTimeConstant = settings.smoothing;
  } else {
    reinitializeFftBuffers();
  }

  smoothingInput.value = settings.smoothing.toFixed(2);
  markUiDirty({ response: true });
  renderUi();
  persistSettings();
}

function scheduleAdaptiveTarget(frequency) {
  adaptiveModel.scheduleTarget(frequency, audioContext ? audioContext.currentTime : null);
  frequencyInput.value = formatNumber(frequency, frequency % 1 === 0 ? 0 : 1);
  resetCurrentStepAverage();
  syncToneSettings();
  markUiDirty({ response: true });
}

function clearAdaptiveData(restartRun = false) {
  adaptiveModel.clear({ manualFrequency: getFrequencyValue() });
  resetCurrentStepAverage();

  if (restartRun && audioContext && isAdaptiveRunning()) {
    const nextFrequency = adaptiveModel.scheduleNext({
      settings: getAdaptiveSettings(),
      analysisMinDb: getAnalysisSettings().minDb,
      now: audioContext.currentTime,
    });
    if (Number.isFinite(nextFrequency)) {
      scheduleAdaptiveTarget(nextFrequency);
    }
  }

  markUiDirty({ response: true });
  renderUi();
}

function startAdaptiveRun(clearExisting = true) {
  const nextFrequency = adaptiveModel.start({
    settings: getAdaptiveSettings(),
    analysisMinDb: getAnalysisSettings().minDb,
    now: audioContext ? audioContext.currentTime : null,
    clearExisting,
    manualFrequency: getFrequencyValue(),
  });

  if (!Number.isFinite(nextFrequency)) {
    setStatus("Adaptive scheduler could not choose a target");
    return;
  }

  frequencyInput.value = formatNumber(nextFrequency, nextFrequency % 1 === 0 ? 0 : 1);
  resetCurrentStepAverage();
  syncToneSettings();
  markUiDirty({ response: true });
  renderUi();
  persistSettings();
}

function stopAdaptiveRun() {
  adaptiveModel.stop({ manualFrequency: getFrequencyValue() });
  resetCurrentStepAverage();
  syncToneSettings();
  markUiDirty({ response: true });
  renderUi();
  persistSettings();
}

function restartAdaptiveRun() {
  if (isAdaptiveRunning()) {
    startAdaptiveRun(true);
  } else {
    clearAdaptiveData(false);
  }
  persistSettings();
}

function commitCurrentAdaptiveMeasurement() {
  if (currentStepFrameCount === 0) {
    return false;
  }

  const measurement = measureTrackedResponse(currentStepAverageData, adaptiveModel.getActiveTargetFrequency());
  if (!measurement) {
    return false;
  }

  adaptiveModel.commitMeasurement(measurement, {
    frequency: adaptiveModel.getActiveTargetFrequency(),
  });
  return true;
}

function finalizeCurrentDwell() {
  if (!commitCurrentAdaptiveMeasurement()) {
    adaptiveModel.rescheduleCurrent(audioContext ? audioContext.currentTime : null);
    resetCurrentStepAverage();
    setStatus("No settled frames collected for this target; repeating");
    return;
  }

  const nextFrequency = adaptiveModel.scheduleNext({
    settings: getAdaptiveSettings(),
    analysisMinDb: getAnalysisSettings().minDb,
    now: audioContext ? audioContext.currentTime : null,
  });

  if (!Number.isFinite(nextFrequency)) {
    setStatus("Adaptive scheduler stalled");
    stopAdaptiveRun();
    return;
  }

  scheduleAdaptiveTarget(nextFrequency);
}

function accumulateCurrentStep(minDb) {
  currentStepFrameCount += 1;

  for (let index = 0; index < fftFrameData.length; index += 1) {
    const sample = Number.isFinite(fftFrameData[index]) ? fftFrameData[index] : minDb;
    const previous = currentStepAverageData[index];
    currentStepAverageData[index] = previous + (sample - previous) / currentStepFrameCount;
  }
}

function exportResponseCsv() {
  if (!adaptiveModel.hasPoints()) {
    setStatus("No adaptive response points to export");
    return;
  }

  const rows = adaptiveModel.getExportRows();
  const sampleRate = getSampleRate();
  const fftSize = getAnalysisSettings().fftSize;
  const header = [
    "row_index",
    "drive_frequency_hz",
    "visit_count",
    "matched_amplitude_mean_db",
    "matched_amplitude_std_db",
    "matched_width_mean_hz",
    "matched_width_std_hz",
    "matched_peak_offset_mean_hz",
    "matched_peak_offset_std_hz",
    "sample_rate_hz",
    "fft_size",
  ];
  const lines = rows.map((row, index) => [
    index,
    row.frequency.toFixed(6),
    row.visits,
    row.amplitudeMeanDb.toFixed(6),
    row.amplitudeStdDb.toFixed(6),
    row.widthMeanHz.toFixed(6),
    row.widthStdHz.toFixed(6),
    row.offsetMeanHz.toFixed(6),
    row.offsetStdHz.toFixed(6),
    sampleRate.toFixed(3),
    fftSize,
  ]);
  const csv = [header, ...lines].map((line) => line.join(",")).join("\r\n");
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  const timestamp = new Date().toISOString().replace(/[:]/g, "-");

  anchor.href = url;
  anchor.download = `adaptive-response-${timestamp}.csv`;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
  setStatus(`Exported ${rows.length} adaptive response point${rows.length === 1 ? "" : "s"} to CSV`);
}

function initializeAnalyser() {
  const settings = getAnalysisSettings();
  analyserNode = audioContext.createAnalyser();
  analyserNode.fftSize = settings.fftSize;
  analyserNode.minDecibels = settings.minDb;
  analyserNode.maxDecibels = settings.maxDb;
  analyserNode.smoothingTimeConstant = settings.smoothing;
  reinitializeFftBuffers();
}

function analysisTick() {
  if (!analyserNode) {
    return;
  }

  const analysis = getAnalysisSettings();
  const adaptive = getAdaptiveSettings();

  analyserNode.getFloatTimeDomainData(waveformData);
  analyserNode.getFloatFrequencyData(fftFrameData);
  markUiDirty({ waveform: true });

  if (adaptive.enabled) {
    if (adaptiveModel.getDwellStartTime() === null) {
      startAdaptiveRun(false);
    }

    if (adaptiveModel.getDwellStartTime() === null) {
      return;
    }

    if (isCurrentStepSettled()) {
      accumulateCurrentStep(analysis.minDb);
      adaptiveModel.setLiveMeasurement(
        measureTrackedResponse(currentStepAverageData, adaptiveModel.getActiveTargetFrequency())
      );
    } else {
      adaptiveModel.clearLiveMeasurement();
    }

    if (audioContext.currentTime - adaptiveModel.getDwellStartTime() >= adaptive.stepSeconds) {
      finalizeCurrentDwell();
    }

    markUiDirty({ response: true });
    return;
  }

  adaptiveModel.setActiveTargetFrequency(getFrequencyValue());
  adaptiveModel.setLiveMeasurement(measureTrackedResponse(fftFrameData, adaptiveModel.getActiveTargetFrequency()));
  markUiDirty({ response: true });
}

function displayTick() {
  renderUi({ drawWaveformIfDirtyOnly: true, drawResponseIfDirtyOnly: true });
}

async function startAudio() {
  if (audioContext) {
    return;
  }

  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({
      audio: {
        echoCancellation: false,
        noiseSuppression: false,
        autoGainControl: false,
      },
      video: false,
    });

    audioContext = new AudioContext({ latencyHint: "interactive" });
    await audioContext.resume();
    sourceNode = audioContext.createMediaStreamSource(mediaStream);
    initializeAnalyser();

    oscillatorNode = audioContext.createOscillator();
    oscillatorNode.type = "sine";
    gainNode = audioContext.createGain();
    leftGainNode = audioContext.createGain();
    rightGainNode = audioContext.createGain();
    mergerNode = audioContext.createChannelMerger(2);

    sourceNode.connect(analyserNode);
    oscillatorNode.connect(gainNode);
    gainNode.connect(leftGainNode);
    gainNode.connect(rightGainNode);
    leftGainNode.connect(mergerNode, 0, 0);
    rightGainNode.connect(mergerNode, 0, 1);
    mergerNode.connect(audioContext.destination);

    oscillatorNode.start();
    adaptiveModel.setActiveTargetFrequency(getFrequencyValue());
    adaptiveModel.stop({ manualFrequency: getFrequencyValue() });

    if (getAdaptiveSettings().enabled) {
      startAdaptiveRun(true);
    } else {
      syncToneSettings();
    }

    analysisTimerId = window.setInterval(analysisTick, analysisIntervalMs);
    displayTimerId = window.setInterval(displayTick, displayIntervalMs);
    ui.setAudioButtonState({ startDisabled: true, stopDisabled: false });
    setStatus(getAdaptiveSettings().enabled ? "Audio running with adaptive scheduler" : "Audio running");
    renderUi();
  } catch (error) {
    console.error(error);
    setStatus(`Start failed: ${error.message}`);
    await stopAudio();
  }
}

async function stopAudio() {
  if (analysisTimerId !== null) {
    window.clearInterval(analysisTimerId);
    analysisTimerId = null;
  }

  if (displayTimerId !== null) {
    window.clearInterval(displayTimerId);
    displayTimerId = null;
  }

  if (oscillatorNode) {
    oscillatorNode.stop();
    oscillatorNode.disconnect();
    oscillatorNode = null;
  }

  if (gainNode) {
    gainNode.disconnect();
    gainNode = null;
  }

  if (leftGainNode) {
    leftGainNode.disconnect();
    leftGainNode = null;
  }

  if (rightGainNode) {
    rightGainNode.disconnect();
    rightGainNode = null;
  }

  if (mergerNode) {
    mergerNode.disconnect();
    mergerNode = null;
  }

  if (sourceNode) {
    sourceNode.disconnect();
    sourceNode = null;
  }

  if (analyserNode) {
    analyserNode.disconnect();
    analyserNode = null;
  }

  if (mediaStream) {
    for (const track of mediaStream.getTracks()) {
      track.stop();
    }
    mediaStream = null;
  }

  if (audioContext) {
    await audioContext.close();
    audioContext = null;
  }

  adaptiveModel.stop({ manualFrequency: getFrequencyValue() });
  waveformData.fill(0);
  resetCurrentStepAverage();
  ui.setAudioButtonState({ startDisabled: false, stopDisabled: true });
  setStatus("Idle");
  ui.clearPlots();
  markUiDirty({ waveform: true, response: true });
  ui.drawWaveformGrid(ui.elements.waveformCanvas.width, ui.elements.waveformCanvas.height);
  renderUi();
}

startButton.addEventListener("click", () => {
  void startAudio();
});

stopButton.addEventListener("click", () => {
  void stopAudio();
});

resetResponseButton.addEventListener("click", () => {
  clearAdaptiveData(false);
});

restartSweepButton.addEventListener("click", () => {
  restartAdaptiveRun();
});

exportCsvButton.addEventListener("click", () => {
  exportResponseCsv();
});

window.addEventListener("beforeunload", () => {
  persistSettings.flush();
});

toneEnabled.addEventListener("change", () => {
  syncToneSettings();
  persistSettings();
});

waveformTab.addEventListener("click", () => {
  ui.setActiveView("waveform");
  markUiDirty({ waveform: true, response: true });
  renderUi();
  persistSettings();
});

responseTab.addEventListener("click", () => {
  ui.setActiveView("response");
  markUiDirty({ waveform: true, response: true });
  renderUi();
  persistSettings();
});

frequencyInput.addEventListener("blur", commitFrequencyInput);
frequencyInput.addEventListener("change", commitFrequencyInput);

amplitudeInput.addEventListener("input", () => {
  syncToneSettings();
  renderUi();
  persistSettings();
});

balanceInput.addEventListener("input", () => {
  syncToneSettings();
  renderUi();
  persistSettings();
});

fftSizeSelect.addEventListener("change", applyAnalysisSettings);
smoothingInput.addEventListener("input", applyAnalysisSettings);
minDbInput.addEventListener("blur", commitDbInputs);
minDbInput.addEventListener("change", commitDbInputs);
maxDbInput.addEventListener("blur", commitDbInputs);
maxDbInput.addEventListener("change", commitDbInputs);

adaptiveSweepEnabledInput.addEventListener("change", () => {
  commitAdaptiveInputs();
  if (audioContext) {
    if (adaptiveSweepEnabledInput.checked) {
      startAdaptiveRun(true);
      setStatus("Audio running with adaptive scheduler");
    } else {
      stopAdaptiveRun();
      setStatus("Audio running");
    }
  }
  renderUi();
  persistSettings();
});

sweepStartHzInput.addEventListener("blur", commitAdaptiveInputs);
sweepStartHzInput.addEventListener("change", commitAdaptiveInputs);
sweepEndHzInput.addEventListener("blur", commitAdaptiveInputs);
sweepEndHzInput.addEventListener("change", commitAdaptiveInputs);
explorePointsInput.addEventListener("blur", commitAdaptiveInputs);
explorePointsInput.addEventListener("change", commitAdaptiveInputs);
sweepLogInput.addEventListener("change", commitAdaptiveInputs);
refineVisitsInput.addEventListener("blur", commitAdaptiveInputs);
refineVisitsInput.addEventListener("change", commitAdaptiveInputs);
sweepStepSecondsInput.addEventListener("blur", commitAdaptiveInputs);
sweepStepSecondsInput.addEventListener("change", commitAdaptiveInputs);
sweepSettleSecondsInput.addEventListener("blur", commitAdaptiveInputs);
sweepSettleSecondsInput.addEventListener("change", commitAdaptiveInputs);

loadSettings();
ui.setActiveView(ui.getActiveView());
reinitializeFftBuffers();
commitFrequencyInput();
commitAdaptiveInputs();
commitDbInputs();
ui.setAudioButtonState({ startDisabled: false, stopDisabled: true });
ui.drawWaveformGrid(ui.elements.waveformCanvas.width, ui.elements.waveformCanvas.height);
renderUi();
