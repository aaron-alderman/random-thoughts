const {
  clampNumber,
  createSettingsPersister,
  formatBalanceLabel,
  formatFrequencyCompact,
  formatNumber,
} = window.FftHeatmapCommon;
const {
  drawMetricChart: drawSharedMetricChart,
  drawWaveform: drawSharedWaveform,
  drawWaveformGrid: drawSharedWaveformGrid,
  formatDb,
  formatHertz,
  formatOffset,
  getMetricRange,
} = window.ResponseExperimentUiCommon;

const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopButton");
const resetResponseButton = document.getElementById("resetResponseButton");
const toneEnabled = document.getElementById("toneEnabled");
const frequencyInput = document.getElementById("frequencyInput");
const amplitudeInput = document.getElementById("amplitudeInput");
const amplitudeValue = document.getElementById("amplitudeValue");
const balanceInput = document.getElementById("balanceInput");
const balanceValue = document.getElementById("balanceValue");
const statusText = document.getElementById("statusText");
const waveformTab = document.getElementById("waveformTab");
const responseTab = document.getElementById("responseTab");
const waveformView = document.getElementById("waveformView");
const responseView = document.getElementById("responseView");
const waveformCanvas = document.getElementById("waveformCanvas");
const amplitudeChartCanvas = document.getElementById("amplitudeChartCanvas");
const widthChartCanvas = document.getElementById("widthChartCanvas");
const offsetChartCanvas = document.getElementById("offsetChartCanvas");
const fftSizeSelect = document.getElementById("fftSizeSelect");
const smoothingInput = document.getElementById("smoothingInput");
const smoothingValue = document.getElementById("smoothingValue");
const minDbInput = document.getElementById("minDbInput");
const maxDbInput = document.getElementById("maxDbInput");
const fftResolution = document.getElementById("fftResolution");
const trackedAmplitudeValue = document.getElementById("trackedAmplitudeValue");
const trackedWidthValue = document.getElementById("trackedWidthValue");
const trackedOffsetValue = document.getElementById("trackedOffsetValue");
const fftAverageCount = document.getElementById("fftAverageCount");
const exportStatusValue = document.getElementById("exportStatusValue");
const sweepEnabledInput = document.getElementById("sweepEnabledInput");
const sweepStartHzInput = document.getElementById("sweepStartHzInput");
const sweepEndHzInput = document.getElementById("sweepEndHzInput");
const sweepStepsInput = document.getElementById("sweepStepsInput");
const sweepLogInput = document.getElementById("sweepLogInput");
const sweepContinuousInput = document.getElementById("sweepContinuousInput");
const sweepLoopInput = document.getElementById("sweepLoopInput");
const sweepStepSecondsInput = document.getElementById("sweepStepSecondsInput");
const sweepSettleSecondsInput = document.getElementById("sweepSettleSecondsInput");
const restartSweepButton = document.getElementById("restartSweepButton");
const exportCsvButton = document.getElementById("exportCsvButton");
const sweepCurrentFrequency = document.getElementById("sweepCurrentFrequency");
const sweepStepProgress = document.getElementById("sweepStepProgress");
const sweepRecordedRows = document.getElementById("sweepRecordedRows");

const waveformContext = waveformCanvas.getContext("2d");
const amplitudeChartContext = amplitudeChartCanvas.getContext("2d");
const widthChartContext = widthChartCanvas.getContext("2d");
const offsetChartContext = offsetChartCanvas.getContext("2d");

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
let responseRows = [];
let liveMeasurement = null;
let sweepCurrentFrequencyValue = 440;
let sweepStepStartTime = null;
let sweepPassStartTime = null;
let currentSweepFrequencies = [];
let currentSweepBoundaries = [];
let currentSweepStepIndex = 0;

const defaultSampleRate = 48000;
const maxOscillatorFrequency = 20000;
const settingsStorageKey = "tracked-response-lab-settings-v1";
const analysisIntervalMs = 100;
const displayIntervalMs = 400;
const measurementTolerance = 1e-6;
const trackedPeakOffsetLimitHz = 5;
const responseChartPadding = { top: 18, right: 18, bottom: 42, left: 84 };

let activeView = "response";
let waveformDirty = true;
let responseDirty = true;
let analysisSettings = null;
let sweepSettings = null;

function setStatus(text) {
  statusText.textContent = text;
}

function setActiveView(view) {
  activeView = view === "waveform" ? "waveform" : "response";
  const showWaveform = activeView === "waveform";

  waveformTab.classList.toggle("active", showWaveform);
  waveformTab.setAttribute("aria-selected", String(showWaveform));
  waveformView.classList.toggle("active", showWaveform);
  waveformView.hidden = !showWaveform;

  responseTab.classList.toggle("active", !showWaveform);
  responseTab.setAttribute("aria-selected", String(!showWaveform));
  responseView.classList.toggle("active", !showWaveform);
  responseView.hidden = showWaveform;

  waveformDirty = true;
  responseDirty = true;
  persistSettings();
}

function collectSettings() {
  return {
    activeView,
    toneEnabled: toneEnabled.checked,
    frequencyInput: frequencyInput.value,
    amplitudeInput: amplitudeInput.value,
    balanceInput: balanceInput.value,
    fftSizeSelect: fftSizeSelect.value,
    smoothingInput: smoothingInput.value,
    minDbInput: minDbInput.value,
    maxDbInput: maxDbInput.value,
    sweepEnabledInput: sweepEnabledInput.checked,
    sweepStartHzInput: sweepStartHzInput.value,
    sweepEndHzInput: sweepEndHzInput.value,
    sweepStepsInput: sweepStepsInput.value,
    sweepLogInput: sweepLogInput.checked,
    sweepContinuousInput: sweepContinuousInput.checked,
    sweepLoopInput: sweepLoopInput.checked,
    sweepStepSecondsInput: sweepStepSecondsInput.value,
    sweepSettleSecondsInput: sweepSettleSecondsInput.value,
  };
}

const persistSettings = createSettingsPersister(settingsStorageKey, collectSettings, 150);

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

    if (typeof settings.activeView === "string") {
      activeView = settings.activeView;
    }

    if (typeof settings.toneEnabled === "boolean") toneEnabled.checked = settings.toneEnabled;
    if (typeof settings.frequencyInput === "string") frequencyInput.value = settings.frequencyInput;
    if (typeof settings.amplitudeInput === "string") amplitudeInput.value = settings.amplitudeInput;
    if (typeof settings.balanceInput === "string") balanceInput.value = settings.balanceInput;
    if (typeof settings.fftSizeSelect === "string") fftSizeSelect.value = settings.fftSizeSelect;
    if (typeof settings.smoothingInput === "string") smoothingInput.value = settings.smoothingInput;
    if (typeof settings.minDbInput === "string") minDbInput.value = settings.minDbInput;
    if (typeof settings.maxDbInput === "string") maxDbInput.value = settings.maxDbInput;
    if (typeof settings.sweepEnabledInput === "boolean") {
      sweepEnabledInput.checked = settings.sweepEnabledInput;
    }
    if (typeof settings.sweepStartHzInput === "string") sweepStartHzInput.value = settings.sweepStartHzInput;
    if (typeof settings.sweepEndHzInput === "string") sweepEndHzInput.value = settings.sweepEndHzInput;
    if (typeof settings.sweepStepsInput === "string") sweepStepsInput.value = settings.sweepStepsInput;
    if (typeof settings.sweepLogInput === "boolean") sweepLogInput.checked = settings.sweepLogInput;
    if (typeof settings.sweepContinuousInput === "boolean") {
      sweepContinuousInput.checked = settings.sweepContinuousInput;
    }
    if (typeof settings.sweepLoopInput === "boolean") sweepLoopInput.checked = settings.sweepLoopInput;
    if (typeof settings.sweepStepSecondsInput === "string") {
      sweepStepSecondsInput.value = settings.sweepStepSecondsInput;
    }
    if (typeof settings.sweepSettleSecondsInput === "string") {
      sweepSettleSecondsInput.value = settings.sweepSettleSecondsInput;
    }
  } catch (error) {
    console.warn("Unable to load settings", error);
  }
}

function getSampleRate() {
  return audioContext ? audioContext.sampleRate : defaultSampleRate;
}

function getNyquist() {
  return getSampleRate() / 2;
}

function readAnalysisSettingsFromInputs() {
  let minDb = Number(minDbInput.value);
  let maxDb = Number(maxDbInput.value);

  if (!Number.isFinite(minDb)) {
    minDb = -100;
  }
  if (!Number.isFinite(maxDb)) {
    maxDb = -20;
  }
  if (minDb >= maxDb - 1) {
    minDb = maxDb - 1;
  }

  const fftSize = Math.round(clampNumber(Number(fftSizeSelect.value), 1024, 32768, 2048));

  return {
    fftSize,
    smoothing: clampNumber(Number(smoothingInput.value), 0, 0.99, 0.75),
    minDb,
    maxDb,
  };
}

function readSweepSettingsFromInputs() {
  let startHz = clampNumber(Number(sweepStartHzInput.value), 20, maxOscillatorFrequency, 440);
  let endHz = clampNumber(Number(sweepEndHzInput.value), 20, maxOscillatorFrequency, 880);

  if (startHz >= endHz) {
    endHz = Math.min(maxOscillatorFrequency, startHz + 0.1);
  }

  const stepSeconds = clampNumber(Number(sweepStepSecondsInput.value), 0.1, 86400, 60);
  const maxSettleSeconds = Math.max(0, stepSeconds - 0.05);

  return {
    enabled: sweepEnabledInput.checked,
    startHz,
    endHz,
    steps: Math.round(clampNumber(Number(sweepStepsInput.value), 2, 20000, 50)),
    log: sweepLogInput.checked,
    continuous: sweepContinuousInput.checked,
    loop: sweepLoopInput.checked,
    stepSeconds,
    settleSeconds: clampNumber(Number(sweepSettleSecondsInput.value), 0, maxSettleSeconds, 0.5),
  };
}

function refreshAnalysisSettings() {
  analysisSettings = readAnalysisSettingsFromInputs();
  return analysisSettings;
}

function refreshSweepSettings() {
  sweepSettings = readSweepSettingsFromInputs();
  return sweepSettings;
}

function getAnalysisSettings() {
  return analysisSettings ?? refreshAnalysisSettings();
}

function getSweepSettings() {
  return sweepSettings ?? refreshSweepSettings();
}

function buildSweepFrequencies(settings) {
  if (settings.steps <= 1) {
    return [settings.startHz];
  }

  const frequencies = [];
  for (let index = 0; index < settings.steps; index += 1) {
    const ratio = index / (settings.steps - 1);
    const frequency = settings.log
      ? settings.startHz * (settings.endHz / settings.startHz) ** ratio
      : settings.startHz + (settings.endHz - settings.startHz) * ratio;
    frequencies.push(frequency);
  }

  return frequencies;
}

function buildSweepBoundaries(settings, frequencies) {
  if (frequencies.length === 0) {
    return [];
  }

  const boundaries = new Float32Array(frequencies.length + 1);
  boundaries[0] = settings.startHz;
  boundaries[boundaries.length - 1] = settings.endHz;

  for (let index = 1; index < frequencies.length; index += 1) {
    boundaries[index] = settings.log
      ? Math.sqrt(frequencies[index - 1] * frequencies[index])
      : (frequencies[index - 1] + frequencies[index]) * 0.5;
  }

  return Array.from(boundaries);
}

function getSweepFrequencyAtProgress(settings, progress) {
  const clampedProgress = clampNumber(progress, 0, 1, 0);
  return settings.log
    ? settings.startHz * (settings.endHz / settings.startHz) ** clampedProgress
    : settings.startHz + (settings.endHz - settings.startHz) * clampedProgress;
}

function getSweepBinIndex(frequency) {
  if (currentSweepFrequencies.length <= 1 || currentSweepBoundaries.length < 2) {
    return 0;
  }

  if (frequency <= currentSweepBoundaries[0]) {
    return 0;
  }
  if (frequency >= currentSweepBoundaries[currentSweepBoundaries.length - 1]) {
    return currentSweepFrequencies.length - 1;
  }

  for (let index = 0; index < currentSweepFrequencies.length; index += 1) {
    if (frequency < currentSweepBoundaries[index + 1]) {
      return index;
    }
  }

  return currentSweepFrequencies.length - 1;
}

function getActiveSweepFrequency() {
  if (currentSweepFrequencies.length === 0) {
    return sweepCurrentFrequencyValue;
  }

  const safeIndex = Math.min(currentSweepFrequencies.length - 1, Math.max(0, currentSweepStepIndex));
  return currentSweepFrequencies[safeIndex];
}

function getFrequencyValue() {
  return clampNumber(Number(frequencyInput.value), 20, maxOscillatorFrequency, 440);
}

function isSweepActive() {
  return Boolean(audioContext && getSweepSettings().enabled);
}

function findHalfPowerCrossing(spectrum, peakIndex, thresholdDb, resolutionHz, direction) {
  let previousIndex = peakIndex;
  let previousValue = spectrum[peakIndex];

  for (
    let currentIndex = peakIndex + direction;
    currentIndex >= 0 && currentIndex < spectrum.length;
    currentIndex += direction
  ) {
    const currentValue = spectrum[currentIndex];
    if (currentValue <= thresholdDb) {
      const delta = currentValue - previousValue;
      if (!Number.isFinite(delta) || Math.abs(delta) < measurementTolerance) {
        return currentIndex * resolutionHz;
      }

      const ratio = (thresholdDb - previousValue) / delta;
      const interpolatedIndex = previousIndex + (currentIndex - previousIndex) * ratio;
      return interpolatedIndex * resolutionHz;
    }

    previousIndex = currentIndex;
    previousValue = currentValue;
  }

  return Number.NaN;
}

function measureTrackedResponse(spectrum, drivenFrequency) {
  if (!spectrum || spectrum.length === 0 || !Number.isFinite(drivenFrequency)) {
    return null;
  }

  const resolutionHz = getNyquist() / spectrum.length;
  const nearestIndex = Math.min(
    spectrum.length - 1,
    Math.max(0, Math.round(drivenFrequency / Math.max(resolutionHz, measurementTolerance)))
  );
  const searchRadiusBins = Math.max(
    1,
    Math.ceil(trackedPeakOffsetLimitHz / Math.max(resolutionHz, measurementTolerance))
  );
  const searchStart = Math.max(0, nearestIndex - searchRadiusBins);
  const searchEnd = Math.min(spectrum.length - 1, nearestIndex + searchRadiusBins);

  let peakIndex = nearestIndex;
  let peakValue = spectrum[nearestIndex];

  for (let index = searchStart; index <= searchEnd; index += 1) {
    if (spectrum[index] > peakValue) {
      peakValue = spectrum[index];
      peakIndex = index;
    }
  }

  const amplitudeDb = peakValue;
  const rawPeakFrequencyHz = peakIndex * resolutionHz;
  const peakOffsetHz = clampNumber(
    rawPeakFrequencyHz - drivenFrequency,
    -trackedPeakOffsetLimitHz,
    trackedPeakOffsetLimitHz,
    0
  );
  const peakFrequencyHz = drivenFrequency + peakOffsetHz;
  const halfPowerThresholdDb = amplitudeDb - 3;
  const leftCrossingHz = findHalfPowerCrossing(
    spectrum,
    peakIndex,
    halfPowerThresholdDb,
    resolutionHz,
    -1
  );
  const rightCrossingHz = findHalfPowerCrossing(
    spectrum,
    peakIndex,
    halfPowerThresholdDb,
    resolutionHz,
    1
  );
  const widthHz =
    Number.isFinite(leftCrossingHz) && Number.isFinite(rightCrossingHz)
      ? Math.max(resolutionHz, rightCrossingHz - leftCrossingHz)
      : resolutionHz;

  return {
    amplitudeDb,
    widthHz,
    peakFrequencyHz,
    peakOffsetHz,
  };
}

function findResponseRowIndex(frequency) {
  let low = 0;
  let high = responseRows.length - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const difference = responseRows[mid].frequency - frequency;

    if (Math.abs(difference) <= measurementTolerance) {
      return { index: mid, found: true };
    }

    if (difference < 0) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return { index: low, found: false };
}

function upsertResponseRow(frequency, measurement, visitCount = 1) {
  const search = findResponseRowIndex(frequency);

  if (!search.found) {
    responseRows.splice(search.index, 0, {
      frequency,
      amplitudeDb: measurement.amplitudeDb,
      widthHz: measurement.widthHz,
      peakFrequencyHz: measurement.peakFrequencyHz,
      peakOffsetHz: measurement.peakOffsetHz,
      visits: visitCount,
    });
    return;
  }

  const row = responseRows[search.index];
  const nextVisits = row.visits + visitCount;
  row.amplitudeDb = row.amplitudeDb + ((measurement.amplitudeDb - row.amplitudeDb) * visitCount) / nextVisits;
  row.widthHz = row.widthHz + ((measurement.widthHz - row.widthHz) * visitCount) / nextVisits;
  row.peakFrequencyHz =
    row.peakFrequencyHz + ((measurement.peakFrequencyHz - row.peakFrequencyHz) * visitCount) / nextVisits;
  row.peakOffsetHz = row.peakOffsetHz + ((measurement.peakOffsetHz - row.peakOffsetHz) * visitCount) / nextVisits;
  row.visits = nextVisits;
}

function getPreviewMeasurement() {
  if (!isSweepActive() || currentStepFrameCount === 0) {
    return null;
  }

  const frequency = getActiveSweepFrequency();
  const measurement = measureTrackedResponse(currentStepAverageData, frequency);
  if (!measurement) {
    return null;
  }

  return {
    frequency,
    ...measurement,
    visits: 1,
    preview: true,
  };
}

function getDisplayedMeasurement() {
  const previewMeasurement = getPreviewMeasurement();
  if (previewMeasurement) {
    return previewMeasurement;
  }

  if (liveMeasurement) {
    return liveMeasurement;
  }

  return responseRows.length > 0 ? responseRows[responseRows.length - 1] : null;
}

function getDisplayResponseRows() {
  const previewMeasurement = getPreviewMeasurement();
  if (!previewMeasurement) {
    return responseRows;
  }

  const search = findResponseRowIndex(previewMeasurement.frequency);
  const nextRows = responseRows.slice();

  if (search.found) {
    nextRows[search.index] = previewMeasurement;
    return nextRows;
  }

  nextRows.splice(search.index, 0, previewMeasurement);
  return nextRows;
}

function updateControls() {
  const currentAnalysisSettings = getAnalysisSettings();
  const currentSweepSettings = getSweepSettings();
  const resolutionHz = getSampleRate() / currentAnalysisSettings.fftSize;
  const balance = clampNumber(Number(balanceInput.value), -100, 100, 0);
  const displayedMeasurement = getDisplayedMeasurement();

  amplitudeValue.textContent = `${amplitudeInput.value}%`;
  balanceValue.textContent = formatBalanceLabel(balance);
  smoothingValue.textContent = currentAnalysisSettings.smoothing.toFixed(2);
  fftResolution.textContent = `${resolutionHz.toFixed(1)} Hz/bin`;
  fftAverageCount.textContent = `${currentStepFrameCount} frame${currentStepFrameCount === 1 ? "" : "s"}`;
  exportStatusValue.textContent = `${responseRows.length} row${responseRows.length === 1 ? "" : "s"}`;
  sweepRecordedRows.textContent = `${responseRows.length} point${responseRows.length === 1 ? "" : "s"}`;
  exportCsvButton.disabled = responseRows.length === 0;

  const displayedFrequency = isSweepActive() ? sweepCurrentFrequencyValue : getFrequencyValue();
  sweepCurrentFrequency.textContent = formatFrequencyCompact(displayedFrequency);

  let elapsed = 0;
  if (isSweepActive() && sweepStepStartTime !== null) {
    elapsed = Math.max(0, audioContext.currentTime - sweepStepStartTime);
  }
  if (isSweepActive()) {
    const phaseLabel = isCurrentStepSettled() ? "collect" : "settle";
    sweepStepProgress.textContent = `${elapsed.toFixed(1)} / ${currentSweepSettings.stepSeconds.toFixed(
      1
    )} s (${phaseLabel})`;
  } else {
    sweepStepProgress.textContent = `${elapsed.toFixed(1)} / ${currentSweepSettings.stepSeconds.toFixed(1)} s`;
  }

  trackedAmplitudeValue.textContent = displayedMeasurement ? formatDb(displayedMeasurement.amplitudeDb) : "n/a";
  trackedWidthValue.textContent = displayedMeasurement ? formatHertz(displayedMeasurement.widthHz) : "n/a";
  trackedOffsetValue.textContent = displayedMeasurement ? formatOffset(displayedMeasurement.peakOffsetHz) : "n/a";
}

function resetCurrentStepAverage() {
  currentStepAverageData = new Float32Array(fftFrameData.length);
  currentStepAverageData.fill(getAnalysisSettings().minDb);
  currentStepFrameCount = 0;
  updateControls();
}

function reinitializeFftBuffers() {
  const binCount = getAnalysisSettings().fftSize / 2;
  fftFrameData = new Float32Array(binCount);
  resetCurrentStepAverage();
}

function clearResponseData(resetSweepTimer = false) {
  responseRows = [];
  liveMeasurement = null;
  resetCurrentStepAverage();

  if (resetSweepTimer && audioContext) {
    sweepStepStartTime = audioContext.currentTime;
    sweepPassStartTime = audioContext.currentTime;
  }

  updateControls();
  responseDirty = true;
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
  const frequency = isSweepActive() ? sweepCurrentFrequencyValue : getFrequencyValue();
  const angle = ((pan + 1) * Math.PI) / 4;
  const channelAmplitude = toneEnabled.checked ? amplitude : 0;
  const leftGain = channelAmplitude * Math.cos(angle);
  const rightGain = channelAmplitude * Math.sin(angle);

  applyOscillatorFrequency(frequency);
  gainNode.gain.setValueAtTime(1, now);
  if (leftGainNode) {
    leftGainNode.gain.setValueAtTime(leftGain, now);
  }
  if (rightGainNode) {
    rightGainNode.gain.setValueAtTime(rightGain, now);
  }
}

function commitFrequencyInput() {
  const frequency = getFrequencyValue();
  frequencyInput.value = formatNumber(frequency, frequency % 1 === 0 ? 0 : 1);

  if (!isSweepActive()) {
    sweepCurrentFrequencyValue = frequency;
    syncToneSettings();
  }

  updateControls();
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

function commitSweepInputs() {
  refreshSweepSettings();
  const currentSweepSettings = getSweepSettings();
  sweepStartHzInput.value = formatNumber(
    currentSweepSettings.startHz,
    currentSweepSettings.startHz % 1 === 0 ? 0 : 1
  );
  sweepEndHzInput.value = formatNumber(currentSweepSettings.endHz, currentSweepSettings.endHz % 1 === 0 ? 0 : 1);
  sweepStepsInput.value = String(currentSweepSettings.steps);
  sweepStepSecondsInput.value = formatNumber(
    currentSweepSettings.stepSeconds,
    currentSweepSettings.stepSeconds % 1 === 0 ? 0 : 1
  );
  sweepSettleSecondsInput.value = formatNumber(
    currentSweepSettings.settleSeconds,
    currentSweepSettings.settleSeconds % 1 === 0 ? 0 : 1
  );
  responseDirty = true;
  updateControls();
  persistSettings();
}

function isCurrentStepSettled(currentTime = audioContext ? audioContext.currentTime : 0) {
  if (!isSweepActive() || sweepStepStartTime === null) {
    return true;
  }

  return currentTime - sweepStepStartTime >= getSweepSettings().settleSeconds;
}

function applyAnalysisSettings() {
  const settings = refreshAnalysisSettings();

  if (analyserNode) {
    if (analyserNode.fftSize !== settings.fftSize) {
      analyserNode.fftSize = settings.fftSize;
      reinitializeFftBuffers();
      clearResponseData(isSweepActive());
    }

    analyserNode.minDecibels = settings.minDb;
    analyserNode.maxDecibels = settings.maxDb;
    analyserNode.smoothingTimeConstant = settings.smoothing;
  } else {
    reinitializeFftBuffers();
  }

  smoothingInput.value = settings.smoothing.toFixed(2);
  updateControls();
  responseDirty = true;
  persistSettings();
}

function startSweep(resetRows = true) {
  const currentSweepSettings = getSweepSettings();
  currentSweepFrequencies = buildSweepFrequencies(currentSweepSettings);
  currentSweepBoundaries = buildSweepBoundaries(currentSweepSettings, currentSweepFrequencies);
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = currentSweepFrequencies[0];
  frequencyInput.value = formatNumber(
    sweepCurrentFrequencyValue,
    sweepCurrentFrequencyValue % 1 === 0 ? 0 : 1
  );
  sweepStepStartTime = audioContext ? audioContext.currentTime : null;
  sweepPassStartTime = audioContext ? audioContext.currentTime : null;

  if (resetRows) {
    responseRows = [];
  }

  liveMeasurement = null;
  resetCurrentStepAverage();
  syncToneSettings();
  updateControls();
  responseDirty = true;
  persistSettings();
}

function stopSweep() {
  if (sweepCurrentFrequencyValue) {
    frequencyInput.value = formatNumber(
      sweepCurrentFrequencyValue,
      sweepCurrentFrequencyValue % 1 === 0 ? 0 : 1
    );
  }

  sweepStepStartTime = null;
  sweepPassStartTime = null;
  resetCurrentStepAverage();
  currentSweepFrequencies = [];
  currentSweepBoundaries = [];
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = getFrequencyValue();
  syncToneSettings();
  updateControls();
  responseDirty = true;
  persistSettings();
}

function restartSweep() {
  if (isSweepActive()) {
    startSweep(true);
  } else {
    clearResponseData(false);
    updateControls();
  }
  persistSettings();
}

function commitCurrentSweepMeasurement() {
  if (currentStepFrameCount === 0) {
    return false;
  }

  const frequency = getActiveSweepFrequency();
  const measurement = measureTrackedResponse(currentStepAverageData, frequency);
  if (!measurement) {
    return false;
  }

  upsertResponseRow(frequency, measurement, 1);
  liveMeasurement = null;
  return true;
}

function finalizeSweepStep() {
  if (!commitCurrentSweepMeasurement()) {
    sweepStepStartTime = audioContext ? audioContext.currentTime : null;
    return;
  }

  const currentSweepSettings = getSweepSettings();
  const nextIndex = currentSweepStepIndex + 1;

  if (nextIndex >= currentSweepFrequencies.length) {
    if (currentSweepSettings.loop) {
      currentSweepStepIndex = 0;
      sweepCurrentFrequencyValue = currentSweepFrequencies[0];
    } else {
      sweepEnabledInput.checked = false;
      stopSweep();
      setStatus(`Sweep completed at ${formatFrequencyCompact(sweepCurrentFrequencyValue)}`);
      return;
    }
  } else {
    currentSweepStepIndex = nextIndex;
    sweepCurrentFrequencyValue = currentSweepFrequencies[currentSweepStepIndex];
  }

  frequencyInput.value = formatNumber(
    sweepCurrentFrequencyValue,
    sweepCurrentFrequencyValue % 1 === 0 ? 0 : 1
  );
  sweepStepStartTime = audioContext.currentTime;
  resetCurrentStepAverage();
  syncToneSettings();
}

function advanceContinuousSweep(currentTime, currentSweepSettings) {
  const totalDuration = currentSweepSettings.stepSeconds * currentSweepFrequencies.length;
  if (!Number.isFinite(totalDuration) || totalDuration <= 0) {
    return;
  }

  if (sweepPassStartTime === null) {
    sweepPassStartTime = currentTime;
  }

  const elapsedPass = Math.max(0, currentTime - sweepPassStartTime);
  const progress = Math.min(1, elapsedPass / totalDuration);
  const frequency = getSweepFrequencyAtProgress(currentSweepSettings, progress);
  const targetIndex = getSweepBinIndex(frequency);

  while (currentSweepStepIndex < targetIndex) {
    commitCurrentSweepMeasurement();
    currentSweepStepIndex += 1;
    sweepStepStartTime = currentTime;
    resetCurrentStepAverage();
    responseDirty = true;
  }

  sweepCurrentFrequencyValue = frequency;
  applyOscillatorFrequency(frequency);

  if (elapsedPass >= totalDuration) {
    commitCurrentSweepMeasurement();
    responseDirty = true;

    if (currentSweepSettings.loop) {
      currentSweepStepIndex = 0;
      sweepPassStartTime = currentTime;
      sweepStepStartTime = currentTime;
      sweepCurrentFrequencyValue = currentSweepFrequencies[0];
      resetCurrentStepAverage();
      syncToneSettings();
    } else {
      sweepEnabledInput.checked = false;
      stopSweep();
      setStatus(`Sweep completed at ${formatFrequencyCompact(currentSweepSettings.endHz)}`);
    }
  }
}

function accumulateCurrentStep(minDb) {
  currentStepFrameCount += 1;

  for (let index = 0; index < fftFrameData.length; index += 1) {
    const sample = Number.isFinite(fftFrameData[index]) ? fftFrameData[index] : minDb;
    const previous = currentStepAverageData[index];
    currentStepAverageData[index] = previous + (sample - previous) / currentStepFrameCount;
  }
}

function drawWaveform() {
  drawSharedWaveform(waveformCanvas, waveformContext, waveformData);
  waveformDirty = false;
}

function drawResponseCharts() {
  const rows = getDisplayResponseRows();
  const resolutionHz = getSampleRate() / getAnalysisSettings().fftSize;

  drawSharedMetricChart({
    canvas: amplitudeChartCanvas,
    context: amplitudeChartContext,
    rows,
    xAxis: getSweepSettings(),
    padding: responseChartPadding,
    series: { meanKey: "amplitudeDb" },
    styles: {
      strokeStyle: "#6ee7ff",
      previewFillStyle: "rgba(110, 231, 255, 0.5)",
    },
    yAxisLabel: "Matched amplitude",
    formatValue: formatDb,
    range: getMetricRange(rows, {
      meanKey: "amplitudeDb",
      fallbackMin: getAnalysisSettings().minDb,
      fallbackMax: getAnalysisSettings().maxDb,
      measurementTolerance,
    }),
  });

  drawSharedMetricChart({
    canvas: widthChartCanvas,
    context: widthChartContext,
    rows,
    xAxis: getSweepSettings(),
    padding: responseChartPadding,
    series: { meanKey: "widthHz" },
    styles: {
      strokeStyle: "#ff6f91",
      previewFillStyle: "rgba(255, 111, 145, 0.5)",
    },
    yAxisLabel: "FWHM width",
    formatValue: formatHertz,
    range: getMetricRange(rows, {
      meanKey: "widthHz",
      fallbackMin: 0,
      fallbackMax: Math.max(50, resolutionHz * 6),
      includeZero: true,
      measurementTolerance,
    }),
  });

  drawSharedMetricChart({
    canvas: offsetChartCanvas,
    context: offsetChartContext,
    rows,
    xAxis: getSweepSettings(),
    padding: responseChartPadding,
    series: { meanKey: "peakOffsetHz" },
    styles: {
      strokeStyle: "#f7d06f",
      previewFillStyle: "rgba(247, 208, 111, 0.5)",
    },
    yAxisLabel: "Peak offset",
    formatValue: formatOffset,
    range: getMetricRange(rows, {
      meanKey: "peakOffsetHz",
      fallbackMin: -trackedPeakOffsetLimitHz,
      fallbackMax: trackedPeakOffsetLimitHz,
      includeZero: true,
      measurementTolerance,
    }),
  });

  responseDirty = false;
}

function exportResponseCsv() {
  if (responseRows.length === 0) {
    setStatus("No tracked response points to export");
    return;
  }

  const sampleRate = getSampleRate();
  const currentAnalysisSettings = getAnalysisSettings();
  const header = [
    "row_index",
    "drive_frequency_hz",
    "visit_count",
    "matched_amplitude_db",
    "matched_width_hz",
    "matched_peak_frequency_hz",
    "matched_peak_offset_hz",
    "sample_rate_hz",
    "fft_size",
  ];
  const rows = responseRows.map((row, index) => [
    index,
    row.frequency.toFixed(6),
    String(row.visits ?? 1),
    row.amplitudeDb.toFixed(6),
    row.widthHz.toFixed(6),
    row.peakFrequencyHz.toFixed(6),
    row.peakOffsetHz.toFixed(6),
    sampleRate.toFixed(3),
    String(currentAnalysisSettings.fftSize),
  ]);
  const csv = [header, ...rows].map((line) => line.join(",")).join("\r\n");
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  const timestamp = new Date().toISOString().replace(/[:]/g, "-");

  anchor.href = url;
  anchor.download = `tracked-response-${timestamp}.csv`;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
  setStatus(`Exported ${responseRows.length} tracked response row${responseRows.length === 1 ? "" : "s"} to CSV`);
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

  const currentAnalysisSettings = getAnalysisSettings();
  const currentSweepSettings = getSweepSettings();

  analyserNode.getFloatTimeDomainData(waveformData);
  analyserNode.getFloatFrequencyData(fftFrameData);
  waveformDirty = true;

  if (currentSweepSettings.enabled) {
    if (sweepStepStartTime === null) {
      startSweep(false);
    }

    if (currentSweepSettings.continuous) {
      advanceContinuousSweep(audioContext.currentTime, currentSweepSettings);
      if (!sweepEnabledInput.checked) {
        return;
      }
      if (isCurrentStepSettled(audioContext.currentTime)) {
        accumulateCurrentStep(currentAnalysisSettings.minDb);
      }
    } else {
      if (isCurrentStepSettled(audioContext.currentTime)) {
        accumulateCurrentStep(currentAnalysisSettings.minDb);
      }

      if (audioContext.currentTime - sweepStepStartTime >= currentSweepSettings.stepSeconds) {
        finalizeSweepStep();
      }
    }

    responseDirty = true;
  } else {
    sweepCurrentFrequencyValue = getFrequencyValue();
    liveMeasurement = measureTrackedResponse(fftFrameData, sweepCurrentFrequencyValue);
    responseDirty = true;
  }
}

function displayTick() {
  updateControls();

  if (activeView === "waveform" && waveformDirty) {
    drawWaveform();
  }

  if (activeView === "response" && responseDirty) {
    drawResponseCharts();
  }
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
    sweepCurrentFrequencyValue = getFrequencyValue();
    sweepStepStartTime = null;

    if (getSweepSettings().enabled) {
      startSweep(true);
    } else {
      syncToneSettings();
    }

    analysisTimerId = window.setInterval(analysisTick, analysisIntervalMs);
    displayTimerId = window.setInterval(displayTick, displayIntervalMs);
    displayTick();

    startButton.disabled = true;
    stopButton.disabled = false;
    setStatus(getSweepSettings().enabled ? "Audio running with sweep" : "Audio running");
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

  startButton.disabled = false;
  stopButton.disabled = true;
  setStatus("Idle");
  sweepStepStartTime = null;
  sweepPassStartTime = null;
  currentSweepFrequencies = [];
  currentSweepBoundaries = [];
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = getFrequencyValue();
  liveMeasurement = null;
  resetCurrentStepAverage();

  waveformContext.clearRect(0, 0, waveformCanvas.width, waveformCanvas.height);
  amplitudeChartContext.clearRect(0, 0, amplitudeChartCanvas.width, amplitudeChartCanvas.height);
  widthChartContext.clearRect(0, 0, widthChartCanvas.width, widthChartCanvas.height);
  offsetChartContext.clearRect(0, 0, offsetChartCanvas.width, offsetChartCanvas.height);
  waveformDirty = true;
  responseDirty = true;
  drawSharedWaveformGrid(waveformContext, waveformCanvas.width, waveformCanvas.height);
  drawResponseCharts();
}

startButton.addEventListener("click", () => {
  void startAudio();
});

stopButton.addEventListener("click", () => {
  void stopAudio();
});

resetResponseButton.addEventListener("click", () => {
  clearResponseData(true);
});

restartSweepButton.addEventListener("click", () => {
  restartSweep();
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
  setActiveView("waveform");
});

responseTab.addEventListener("click", () => {
  setActiveView("response");
});

frequencyInput.addEventListener("blur", commitFrequencyInput);
frequencyInput.addEventListener("change", commitFrequencyInput);

amplitudeInput.addEventListener("input", () => {
  updateControls();
  syncToneSettings();
  persistSettings();
});

balanceInput.addEventListener("input", () => {
  updateControls();
  syncToneSettings();
  persistSettings();
});

fftSizeSelect.addEventListener("change", applyAnalysisSettings);
smoothingInput.addEventListener("input", applyAnalysisSettings);
minDbInput.addEventListener("blur", commitDbInputs);
minDbInput.addEventListener("change", commitDbInputs);
maxDbInput.addEventListener("blur", commitDbInputs);
maxDbInput.addEventListener("change", commitDbInputs);

sweepEnabledInput.addEventListener("change", () => {
  if (audioContext && sweepEnabledInput.checked) {
    commitSweepInputs();
    startSweep(true);
    setStatus("Audio running with sweep");
  } else if (audioContext) {
    stopSweep();
    setStatus("Audio running");
  }
  updateControls();
  persistSettings();
});

sweepStartHzInput.addEventListener("blur", commitSweepInputs);
sweepStartHzInput.addEventListener("change", commitSweepInputs);
sweepEndHzInput.addEventListener("blur", commitSweepInputs);
sweepEndHzInput.addEventListener("change", commitSweepInputs);
sweepStepsInput.addEventListener("blur", commitSweepInputs);
sweepStepsInput.addEventListener("change", commitSweepInputs);
sweepLogInput.addEventListener("change", commitSweepInputs);
sweepContinuousInput.addEventListener("change", commitSweepInputs);
sweepLoopInput.addEventListener("change", () => {
  refreshSweepSettings();
  updateControls();
  persistSettings();
});
sweepStepSecondsInput.addEventListener("blur", commitSweepInputs);
sweepStepSecondsInput.addEventListener("change", commitSweepInputs);
sweepSettleSecondsInput.addEventListener("blur", commitSweepInputs);
sweepSettleSecondsInput.addEventListener("change", commitSweepInputs);

loadSettings();
reinitializeFftBuffers();
commitFrequencyInput();
commitSweepInputs();
commitDbInputs();
updateControls();
setActiveView(activeView);
drawSharedWaveformGrid(waveformContext, waveformCanvas.width, waveformCanvas.height);
drawResponseCharts();
