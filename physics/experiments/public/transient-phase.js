const {
  buildColumnBackground,
  buildDisplayRows,
  buildHeatmapMarginals,
  buildHeatmapPalette,
  buildHeatmapRowGeometry,
  clampNumber,
  createSettingsPersister,
  drawHeatmapAxes,
  drawRightMarginal,
  drawTopMarginal,
  formatBalanceLabel,
  formatFrequencyCompact,
  formatNumber,
  getFrequencyX,
  getHeatmapLayout,
  getOrBuildColumnBins,
  subtractColumnBackground,
  upsertHeatmapRow,
} = window.FftHeatmapCommon;

const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopButton");
const resetFftButton = document.getElementById("resetFftButton");
const toneEnabled = document.getElementById("toneEnabled");
const frequencyInput = document.getElementById("frequencyInput");
const amplitudeInput = document.getElementById("amplitudeInput");
const amplitudeValue = document.getElementById("amplitudeValue");
const balanceInput = document.getElementById("balanceInput");
const balanceValue = document.getElementById("balanceValue");
const statusText = document.getElementById("statusText");
const waveformTab = document.getElementById("waveformTab");
const heatmapTab = document.getElementById("heatmapTab");
const waveformView = document.getElementById("waveformView");
const heatmapView = document.getElementById("heatmapView");
const waveformCanvas = document.getElementById("waveformCanvas");
const fftCanvas = document.getElementById("fftCanvas");
const fftSizeSelect = document.getElementById("fftSizeSelect");
const smoothingInput = document.getElementById("smoothingInput");
const smoothingValue = document.getElementById("smoothingValue");
const minDbInput = document.getElementById("minDbInput");
const maxDbInput = document.getElementById("maxDbInput");
const subtractColumnBackgroundInput = document.getElementById("subtractColumnBackgroundInput");
const backgroundPercentileInput = document.getElementById("backgroundPercentileInput");
const freqScaleSelect = document.getElementById("freqScaleSelect");
const displayStartInput = document.getElementById("displayStartInput");
const displayEndInput = document.getElementById("displayEndInput");
const fftResolution = document.getElementById("fftResolution");
const fftRange = document.getElementById("fftRange");
const fftAverageCount = document.getElementById("fftAverageCount");
const fftBackgroundStatus = document.getElementById("fftBackgroundStatus");
const fftVisibleBand = document.getElementById("fftVisibleBand");
const sweepEnabledInput = document.getElementById("sweepEnabledInput");
const sweepStartHzInput = document.getElementById("sweepStartHzInput");
const sweepEndHzInput = document.getElementById("sweepEndHzInput");
const sweepStepsInput = document.getElementById("sweepStepsInput");
const jumpIntervalSecondsInput = document.getElementById("jumpIntervalSecondsInput");
const sweepLogInput = document.getElementById("sweepLogInput");
const sweepContinuousInput = document.getElementById("sweepContinuousInput");
const sweepLoopInput = document.getElementById("sweepLoopInput");
const sweepStepSecondsInput = document.getElementById("sweepStepSecondsInput");
const restartSweepButton = document.getElementById("restartSweepButton");
const exportCsvButton = document.getElementById("exportCsvButton");
const sweepCurrentFrequency = document.getElementById("sweepCurrentFrequency");
const sweepStepProgress = document.getElementById("sweepStepProgress");
const sweepRecordedRows = document.getElementById("sweepRecordedRows");

const waveformContext = waveformCanvas.getContext("2d");
const fftContext = fftCanvas.getContext("2d");

let audioContext = null;
let mediaStream = null;
let sourceNode = null;
let analyserNode = null;
let processorNode = null;
let analysisTimerId = null;
let displayTimerId = null;

const waveformBufferLength = 2048;
const waveformData = new Float32Array(waveformBufferLength);

let fftFrameData = new Float32Array(1024);
let currentStepAverageData = new Float32Array(1024);
let currentStepFrameCount = 0;
let heatmapRows = [];
let sweepCurrentFrequencyValue = 0;
let sweepStepStartTime = null;
let currentSweepFrequencies = [];
let currentSweepStepIndex = 0;
let carrierPhase = 0;
let samplesUntilPhaseJump = 0;
let currentCarrierFrequencyValue = 440;
let currentPhaseJumpDegreesValue = 0;
let currentJumpIntervalSecondsValue = 0.5;
let currentLeftGainValue = 0;
let currentRightGainValue = 0;
let phaseJumpApplied = false;
let boundaryTransitionSamplesRemaining = 0;
let boundaryTransitionTotalSamples = 0;
let boundaryTransitionResetPending = false;

const defaultSampleRate = 48000;
const maxCarrierFrequency = 20000;
const fftAxisPadding = { top: 12, right: 16, bottom: 34, left: 76 };
const fftMarginalLayout = { topHeight: 56, rightWidth: 82, gap: 12 };
const heatmapPalette = buildHeatmapPalette();
const settingsStorageKey = "phase-jump-lab-settings-v1";
const analysisIntervalMs = 100;
const displayIntervalMs = 400;
const boundaryTransitionSeconds = 0.008;
const heatmapRowTolerance = 1e-6;
let activeView = "heatmap";
let waveformDirty = true;
let heatmapDirty = true;
let fftSettings = null;
let sweepSettings = null;
let columnBinCache = { key: null, value: null };

function setStatus(text) {
  statusText.textContent = text;
}

function setActiveView(view) {
  activeView = view === "waveform" ? "waveform" : "heatmap";
  const showWaveform = activeView === "waveform";

  waveformTab.classList.toggle("active", showWaveform);
  waveformTab.setAttribute("aria-selected", String(showWaveform));
  waveformView.classList.toggle("active", showWaveform);
  waveformView.hidden = !showWaveform;

  heatmapTab.classList.toggle("active", !showWaveform);
  heatmapTab.setAttribute("aria-selected", String(!showWaveform));
  heatmapView.classList.toggle("active", !showWaveform);
  heatmapView.hidden = showWaveform;
  waveformDirty = true;
  heatmapDirty = true;
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
    subtractColumnBackgroundInput: subtractColumnBackgroundInput.checked,
    backgroundPercentileInput: backgroundPercentileInput.value,
    freqScaleSelect: freqScaleSelect.value,
    displayStartInput: displayStartInput.value,
    displayEndInput: displayEndInput.value,
    sweepEnabledInput: sweepEnabledInput.checked,
    sweepStartHzInput: sweepStartHzInput.value,
    sweepEndHzInput: sweepEndHzInput.value,
    sweepStepsInput: sweepStepsInput.value,
    jumpIntervalSecondsInput: jumpIntervalSecondsInput.value,
    sweepLoopInput: sweepLoopInput.checked,
    sweepStepSecondsInput: sweepStepSecondsInput.value,
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
    if (typeof settings.subtractColumnBackgroundInput === "boolean") {
      subtractColumnBackgroundInput.checked = settings.subtractColumnBackgroundInput;
    }
    if (typeof settings.backgroundPercentileInput === "string") {
      backgroundPercentileInput.value = settings.backgroundPercentileInput;
    }
    if (typeof settings.freqScaleSelect === "string") freqScaleSelect.value = settings.freqScaleSelect;
    if (typeof settings.displayStartInput === "string") displayStartInput.value = settings.displayStartInput;
    if (typeof settings.displayEndInput === "string") displayEndInput.value = settings.displayEndInput;
    if (typeof settings.sweepEnabledInput === "boolean") {
      sweepEnabledInput.checked = settings.sweepEnabledInput;
    }
    if (typeof settings.sweepStartHzInput === "string") sweepStartHzInput.value = settings.sweepStartHzInput;
    if (typeof settings.sweepEndHzInput === "string") sweepEndHzInput.value = settings.sweepEndHzInput;
    if (typeof settings.sweepStepsInput === "string") sweepStepsInput.value = settings.sweepStepsInput;
    if (typeof settings.jumpIntervalSecondsInput === "string") {
      jumpIntervalSecondsInput.value = settings.jumpIntervalSecondsInput;
    }
    if (typeof settings.sweepLoopInput === "boolean") sweepLoopInput.checked = settings.sweepLoopInput;
    if (typeof settings.sweepStepSecondsInput === "string") {
      sweepStepSecondsInput.value = settings.sweepStepSecondsInput;
    }
  } catch (error) {
    console.warn("Unable to load settings", error);
  }
}

function formatDegreesCompact(value) {
  return `${formatNumber(value, Math.abs(value % 1) < 1e-6 ? 0 : 1)} deg`;
}

function getSampleRate() {
  return audioContext ? audioContext.sampleRate : defaultSampleRate;
}

function getNyquist() {
  return getSampleRate() / 2;
}

function readFftSettingsFromInputs() {
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

  const backgroundPercentile = Math.round(clampNumber(Number(backgroundPercentileInput.value), 0, 50, 20));
  let displayStart = Number(displayStartInput.value);
  let displayEnd = Number(displayEndInput.value);

  if (!Number.isFinite(displayStart)) {
    displayStart = 0;
  }
  if (!Number.isFinite(displayEnd)) {
    displayEnd = 12000;
  }

  return {
    fftSize: Number(fftSizeSelect.value),
    smoothing: Number(smoothingInput.value),
    minDb,
    maxDb,
    subtractColumnBackground: subtractColumnBackgroundInput.checked,
    backgroundPercentile,
    scale: freqScaleSelect.value,
    displayStart,
    displayEnd,
  };
}

function readSweepSettingsFromInputs() {
  let startHz = clampNumber(Number(sweepStartHzInput.value), 0, 360, 0);
  let endHz = clampNumber(Number(sweepEndHzInput.value), 0, 360, 180);

  if (startHz >= endHz) {
    endHz = Math.min(360, startHz + 1);
  }

  return {
    enabled: sweepEnabledInput.checked,
    startHz,
    endHz,
    steps: Math.round(clampNumber(Number(sweepStepsInput.value), 2, 360, 50)),
    jumpIntervalSeconds: clampNumber(Number(jumpIntervalSecondsInput.value), 0.01, 60, 0.5),
    loop: sweepLoopInput.checked,
    stepSeconds: clampNumber(Number(sweepStepSecondsInput.value), 0.1, 86400, 60),
  };
}

function refreshFftSettings() {
  fftSettings = readFftSettingsFromInputs();
  columnBinCache.key = null;
  return fftSettings;
}

function refreshSweepSettings() {
  sweepSettings = readSweepSettingsFromInputs();
  return sweepSettings;
}

function getFftSettings() {
  return fftSettings ?? refreshFftSettings();
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
    const frequency = settings.startHz + (settings.endHz - settings.startHz) * ratio;
    frequencies.push(frequency);
  }

  return frequencies;
}

function getActiveSweepRowFrequency() {
  if (currentSweepFrequencies.length === 0) {
    return sweepCurrentFrequencyValue;
  }

  const safeIndex = Math.min(currentSweepFrequencies.length - 1, Math.max(0, currentSweepStepIndex));
  return currentSweepFrequencies[safeIndex];
}

function getVisibleFrequencyRange(scale = getFftSettings().scale) {
  const nyquist = getNyquist();
  const minimumStart = scale === "log" ? 20 : 0;
  const settings = getFftSettings();

  let start = Number.isFinite(settings.displayStart) ? settings.displayStart : minimumStart;
  let end = Number.isFinite(settings.displayEnd) ? settings.displayEnd : Math.min(12000, nyquist);

  start = Math.max(minimumStart, Math.min(start, nyquist - 1));
  end = Math.max(start + 1, Math.min(end, nyquist));

  return { start, end };
}

function getFrequencyValue() {
  return clampNumber(Number(frequencyInput.value), 20, maxCarrierFrequency, 440);
}

function getCurrentPhaseJumpDegrees() {
  if (isSweepActive()) {
    return getActiveSweepRowFrequency();
  }

  return clampNumber(Number(sweepStartHzInput.value), 0, 360, 0);
}

function isSweepActive() {
  return Boolean(audioContext && getSweepSettings().enabled);
}

function updateControls() {
  const fftSettings = getFftSettings();
  const sweepSettings = getSweepSettings();
  const visibleRange = getVisibleFrequencyRange(fftSettings.scale);
  const resolutionHz = getSampleRate() / fftSettings.fftSize;
  const balance = clampNumber(Number(balanceInput.value), -100, 100, 0);

  amplitudeValue.textContent = `${amplitudeInput.value}%`;
  balanceValue.textContent = formatBalanceLabel(balance);
  smoothingValue.textContent = fftSettings.smoothing.toFixed(2);
  fftRange.textContent = `${Math.round(fftSettings.minDb)} dB to ${Math.round(fftSettings.maxDb)} dB`;
  fftResolution.textContent = `${resolutionHz.toFixed(1)} Hz/bin`;
  fftAverageCount.textContent = `${currentStepFrameCount} frame${currentStepFrameCount === 1 ? "" : "s"}`;
  fftBackgroundStatus.textContent = fftSettings.subtractColumnBackground
    ? heatmapRows.length >= 2
      ? `Per-column P${fftSettings.backgroundPercentile}`
      : "Need 2 rows"
    : "Off";
  fftVisibleBand.textContent = `${formatFrequencyCompact(visibleRange.start)} to ${formatFrequencyCompact(
    visibleRange.end
  )}`;

  const displayedPhaseJump = isSweepActive() ? sweepCurrentFrequencyValue : getCurrentPhaseJumpDegrees();
  sweepCurrentFrequency.textContent = formatDegreesCompact(displayedPhaseJump);
  sweepRecordedRows.textContent = `${heatmapRows.length} row${heatmapRows.length === 1 ? "" : "s"}`;
  exportCsvButton.disabled = heatmapRows.length === 0;

  let elapsed = 0;
  if (isSweepActive() && sweepStepStartTime !== null) {
    elapsed = Math.max(0, audioContext.currentTime - sweepStepStartTime);
  }
  sweepStepProgress.textContent = `${elapsed.toFixed(1)} / ${sweepSettings.stepSeconds.toFixed(1)} s`;
}

function resetCurrentStepAverage() {
  currentStepAverageData = new Float32Array(fftFrameData.length);
  currentStepAverageData.fill(getFftSettings().minDb);
  currentStepFrameCount = 0;
  updateControls();
}

function reinitializeFftBuffers() {
  const binCount = getFftSettings().fftSize / 2;
  fftFrameData = new Float32Array(binCount);
  resetCurrentStepAverage();
}

function clearHeatmap(resetSweepTimer = false) {
  heatmapRows = [];
  resetCurrentStepAverage();

  if (resetSweepTimer && audioContext) {
    sweepStepStartTime = audioContext.currentTime;
  }

  updateControls();
  heatmapDirty = true;
}

function applyOscillatorFrequency(frequency) {
  currentCarrierFrequencyValue = frequency;
}

function syncToneSettings() {
  if (!audioContext) {
    return;
  }

  const amplitude = Number(amplitudeInput.value) / 100;
  const pan = clampNumber(Number(balanceInput.value) / 100, -1, 1, 0);
  const frequency = getFrequencyValue();
  const phaseJumpDegrees = getCurrentPhaseJumpDegrees();
  const jumpIntervalSeconds = getSweepSettings().jumpIntervalSeconds;
  const angle = ((pan + 1) * Math.PI) / 4;
  const channelAmplitude = toneEnabled.checked ? amplitude : 0;
  currentLeftGainValue = channelAmplitude * Math.cos(angle);
  currentRightGainValue = channelAmplitude * Math.sin(angle);
  currentPhaseJumpDegreesValue = phaseJumpDegrees;
  currentJumpIntervalSecondsValue = jumpIntervalSeconds;
  currentCarrierFrequencyValue = frequency;

  applyOscillatorFrequency(frequency);
}

function resetPhaseJumpCycle(resetCarrierPhase = false) {
  if (resetCarrierPhase) {
    carrierPhase = 0;
  }
  samplesUntilPhaseJump = Math.max(1, Math.round(currentJumpIntervalSecondsValue * getSampleRate()));
  phaseJumpApplied = false;
}

function queueBoundaryTransition(resetCarrierPhase = true) {
  if (!audioContext) {
    resetPhaseJumpCycle(resetCarrierPhase);
    return;
  }

  boundaryTransitionTotalSamples = Math.max(16, Math.round(boundaryTransitionSeconds * getSampleRate()));
  boundaryTransitionSamplesRemaining = boundaryTransitionTotalSamples;
  boundaryTransitionResetPending = resetCarrierPhase;
}

function commitFrequencyInput() {
  const frequency = getFrequencyValue();
  frequencyInput.value = formatNumber(frequency, frequency % 1 === 0 ? 0 : 1);
  syncToneSettings();

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
  applyFftSettings();
  persistSettings();
}

function commitBackgroundInputs() {
  refreshFftSettings();
  const fftSettings = getFftSettings();
  backgroundPercentileInput.value = String(fftSettings.backgroundPercentile);
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function commitVisibleRangeInputs() {
  const visibleRange = getVisibleFrequencyRange(getFftSettings().scale);
  displayStartInput.value = formatNumber(visibleRange.start, visibleRange.start % 1 === 0 ? 0 : 1);
  displayEndInput.value = formatNumber(visibleRange.end, visibleRange.end % 1 === 0 ? 0 : 1);
  refreshFftSettings();
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function commitSweepInputs() {
  refreshSweepSettings();
  const sweepSettings = getSweepSettings();
  sweepStartHzInput.value = formatNumber(sweepSettings.startHz, sweepSettings.startHz % 1 === 0 ? 0 : 1);
  sweepEndHzInput.value = formatNumber(sweepSettings.endHz, sweepSettings.endHz % 1 === 0 ? 0 : 1);
  sweepStepsInput.value = String(sweepSettings.steps);
  jumpIntervalSecondsInput.value = formatNumber(
    sweepSettings.jumpIntervalSeconds,
    sweepSettings.jumpIntervalSeconds % 1 === 0 ? 0 : 2
  );
  sweepStepSecondsInput.value = formatNumber(
    sweepSettings.stepSeconds,
    sweepSettings.stepSeconds % 1 === 0 ? 0 : 1
  );
  syncToneSettings();
  if (audioContext) {
    resetPhaseJumpCycle();
  }
  updateControls();
  persistSettings();
}

function applyFftSettings() {
  const settings = refreshFftSettings();

  if (analyserNode) {
    if (analyserNode.fftSize !== settings.fftSize) {
      analyserNode.fftSize = settings.fftSize;
      reinitializeFftBuffers();
      if (isSweepActive()) {
        clearHeatmap(true);
      }
    }

    analyserNode.minDecibels = settings.minDb;
    analyserNode.maxDecibels = settings.maxDb;
    analyserNode.smoothingTimeConstant = settings.smoothing;
  } else {
    reinitializeFftBuffers();
  }

  backgroundPercentileInput.value = String(settings.backgroundPercentile);
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function startSweep(resetRows = true) {
  const sweepSettings = getSweepSettings();
  currentSweepFrequencies = buildSweepFrequencies(sweepSettings);
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = currentSweepFrequencies[0];
  sweepStepStartTime = audioContext ? audioContext.currentTime : null;

  if (resetRows) {
    heatmapRows = [];
  }

  resetCurrentStepAverage();
  syncToneSettings();
  queueBoundaryTransition(true);
  updateControls();
  heatmapDirty = true;
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
  resetCurrentStepAverage();
  currentSweepFrequencies = [];
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = getCurrentPhaseJumpDegrees();
  syncToneSettings();
  if (audioContext) {
    queueBoundaryTransition(true);
  }
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function restartSweep() {
  if (isSweepActive()) {
    startSweep(true);
  } else {
    clearHeatmap(false);
    updateControls();
  }
  persistSettings();
}

function commitCurrentSweepBin() {
  if (currentStepFrameCount === 0) {
    return false;
  }

  upsertHeatmapRow(heatmapRows, getActiveSweepRowFrequency(), currentStepAverageData, 1, heatmapRowTolerance);
  return true;
}

function finalizeSweepStep() {
  if (!commitCurrentSweepBin()) {
    sweepStepStartTime = audioContext ? audioContext.currentTime : null;
    return;
  }

  const sweepSettings = getSweepSettings();
  const nextIndex = currentSweepStepIndex + 1;

  if (nextIndex >= currentSweepFrequencies.length) {
    if (sweepSettings.loop) {
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

  sweepStepStartTime = audioContext.currentTime;
  resetCurrentStepAverage();
  syncToneSettings();
  queueBoundaryTransition(true);
}

function accumulateCurrentStep(minDb) {
  currentStepFrameCount += 1;

  for (let i = 0; i < fftFrameData.length; i += 1) {
    const sample = Number.isFinite(fftFrameData[i]) ? fftFrameData[i] : minDb;
    const previous = currentStepAverageData[i];
    currentStepAverageData[i] = previous + (sample - previous) / currentStepFrameCount;
  }
}

function drawWaveformGrid(width, height) {
  waveformContext.save();
  waveformContext.strokeStyle = "rgba(255, 255, 255, 0.08)";
  waveformContext.lineWidth = 1;

  for (let i = 1; i < 6; i += 1) {
    const y = (height / 6) * i;
    waveformContext.beginPath();
    waveformContext.moveTo(0, y);
    waveformContext.lineTo(width, y);
    waveformContext.stroke();
  }

  for (let i = 1; i < 8; i += 1) {
    const x = (width / 8) * i;
    waveformContext.beginPath();
    waveformContext.moveTo(x, 0);
    waveformContext.lineTo(x, height);
    waveformContext.stroke();
  }

  waveformContext.restore();
}

function drawWaveform() {
  const { width, height } = waveformCanvas;
  waveformContext.clearRect(0, 0, width, height);
  drawWaveformGrid(width, height);

  waveformContext.strokeStyle = "#6ee7ff";
  waveformContext.lineWidth = 2;
  waveformContext.beginPath();

  for (let i = 0; i < waveformData.length; i += 1) {
    const x = (i / (waveformData.length - 1)) * width;
    const y = height * 0.5 - waveformData[i] * height * 0.42;

    if (i === 0) {
      waveformContext.moveTo(x, y);
    } else {
      waveformContext.lineTo(x, y);
    }
  }

  waveformContext.stroke();
  waveformDirty = false;
}

function getSweepScaleSettings(rows) {
  const sweepSettings = getSweepSettings();
  let minFrequency = sweepSettings.startHz;
  let maxFrequency = sweepSettings.endHz;

  if (rows.length > 0) {
    minFrequency = rows[0].frequency;
    maxFrequency = rows[rows.length - 1].frequency;
  }

  if (minFrequency >= maxFrequency) {
    maxFrequency = minFrequency + 1;
  }

  return {
    minFrequency,
    maxFrequency,
    log: false,
  };
}

function getSweepY(frequency, height, scaleSettings) {
  const safeFrequency = Math.min(scaleSettings.maxFrequency, Math.max(scaleSettings.minFrequency, frequency));

  if (scaleSettings.log) {
    const logMin = Math.log10(scaleSettings.minFrequency);
    const logMax = Math.log10(scaleSettings.maxFrequency);
    const logValue = Math.log10(safeFrequency);
    return ((logValue - logMin) / (logMax - logMin)) * height;
  }

  return ((safeFrequency - scaleSettings.minFrequency) / (scaleSettings.maxFrequency - scaleSettings.minFrequency)) * height;
}

function getDisplayRows() {
  const previewRow =
    isSweepActive() && currentStepFrameCount > 0
      ? {
          frequency: getActiveSweepRowFrequency(),
          spectrum: currentStepAverageData,
          preview: true,
        }
      : null;

  return buildDisplayRows(heatmapRows, previewRow, heatmapRowTolerance);
}

function exportHeatmapCsv() {
  if (heatmapRows.length === 0) {
    setStatus("No recorded heatmap rows to export");
    return;
  }

  const sampleRate = getSampleRate();
  const binCount = heatmapRows[0].spectrum.length;
  const nyquist = sampleRate / 2;
  const binFrequencies = Array.from({ length: binCount }, (_, index) =>
    (index * nyquist) / binCount
  );

  const header = [
    "row_index",
    "phase_jump_degrees",
    "visit_count",
    "sample_rate_hz",
    "fft_size",
    ...binFrequencies.map((frequency) => `response_${frequency.toFixed(3)}_hz`),
  ];

  const rows = heatmapRows.map((row, index) => [
    index,
    row.frequency.toFixed(6),
    String(row.visits ?? 1),
    sampleRate.toFixed(3),
    String(binCount * 2),
    ...Array.from(row.spectrum, (value) => value.toFixed(6)),
  ]);

  const csv = [header, ...rows].map((line) => line.join(",")).join("\r\n");
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  const timestamp = new Date().toISOString().replace(/[:]/g, "-");

  anchor.href = url;
  anchor.download = `phase-jump-heatmap-${timestamp}.csv`;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
  setStatus(`Exported ${heatmapRows.length} heatmap row${heatmapRows.length === 1 ? "" : "s"} to CSV`);
}

function drawFftHeatmap() {
  const { width, height } = fftCanvas;
  const settings = getFftSettings();
  const visibleRange = getVisibleFrequencyRange(settings.scale);
  const layout = getHeatmapLayout(width, height, fftAxisPadding, fftMarginalLayout);
  const rows = getDisplayRows();
  const columnBackground = settings.subtractColumnBackground
    ? buildColumnBackground(heatmapRows, settings.backgroundPercentile, settings.minDb)
    : null;
  const renderedRows = rows.map((row) => ({
    ...row,
    renderedSpectrum: subtractColumnBackground(row.spectrum, columnBackground, settings.minDb),
  }));
  const sweepScaleSettings = getSweepScaleSettings(renderedRows);
  const rowGeometry = buildHeatmapRowGeometry(
    renderedRows,
    layout.heatmapHeight,
    (frequency, chartHeight) => getSweepY(frequency, chartHeight, sweepScaleSettings)
  );
  const nyquist = getNyquist();

  fftContext.clearRect(0, 0, width, height);
  drawHeatmapAxes({
    ctx: fftContext,
    layout,
    settings,
    minFrequency: visibleRange.start,
    maxFrequency: visibleRange.end,
    rows: renderedRows,
    rowGeometry,
    formatYAxisLabel: formatDegreesCompact,
    yAxisTitle: "Phase jump",
    emptyLabel: "No sweep rows yet",
  });

  if (renderedRows.length === 0) {
    return;
  }

  const columnBins = getOrBuildColumnBins(columnBinCache, {
    width: layout.heatmapWidth,
    binCount: renderedRows[0].renderedSpectrum.length,
    scale: settings.scale,
    minFrequency: visibleRange.start,
    maxFrequency: visibleRange.end,
    nyquist,
  });

  const { columnTotals, rowTotals } = buildHeatmapMarginals(renderedRows, columnBins);
  drawTopMarginal({
    ctx: fftContext,
    layout,
    columnTotals,
    settings,
    minFrequency: visibleRange.start,
    maxFrequency: visibleRange.end,
    nyquist,
  });
  drawRightMarginal({ ctx: fftContext, layout, rowTotals, rowGeometry });

  const imageData = fftContext.createImageData(layout.heatmapWidth, layout.heatmapHeight);
  const pixels = imageData.data;

  for (let y = 0; y < layout.heatmapHeight; y += 1) {
    const rowIndex = Math.min(renderedRows.length - 1, rowGeometry.pixelRowIndices[y]);
    const row = renderedRows[rowIndex];

    for (let x = 0; x < layout.heatmapWidth; x += 1) {
      const binIndex = columnBins[x];
      const dbValue = row.renderedSpectrum[binIndex];
      const normalized = (dbValue - settings.minDb) / (settings.maxDb - settings.minDb);
      const clamped = Math.min(1, Math.max(0, normalized));
      const color = heatmapPalette[Math.round(clamped * 255)];
      const pixelIndex = (y * layout.heatmapWidth + x) * 4;

      pixels[pixelIndex] = color[0];
      pixels[pixelIndex + 1] = color[1];
      pixels[pixelIndex + 2] = color[2];
      pixels[pixelIndex + 3] = row.preview ? 180 : 255;
    }
  }

  fftContext.putImageData(imageData, layout.heatmapX, layout.heatmapY);
  heatmapDirty = false;
}

function initializeAnalyser() {
  const settings = getFftSettings();
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

  const fftSettings = getFftSettings();
  const sweepSettings = getSweepSettings();

  analyserNode.getFloatTimeDomainData(waveformData);
  analyserNode.getFloatFrequencyData(fftFrameData);
  waveformDirty = true;

  if (sweepSettings.enabled) {
    if (sweepStepStartTime === null) {
      startSweep(false);
    }

    accumulateCurrentStep(fftSettings.minDb);

    if (audioContext.currentTime - sweepStepStartTime >= sweepSettings.stepSeconds) {
      finalizeSweepStep();
      heatmapDirty = true;
    }
  } else {
    sweepCurrentFrequencyValue = getCurrentPhaseJumpDegrees();
  }
}

function displayTick() {
  updateControls();

  if (activeView === "waveform" && waveformDirty) {
    drawWaveform();
  }

  if (activeView === "heatmap" && heatmapDirty) {
    drawFftHeatmap();
  }
}

function processPhaseJumpOutput(event) {
  const leftChannel = event.outputBuffer.getChannelData(0);
  const rightChannel = event.outputBuffer.getChannelData(1);
  const sampleRate = event.outputBuffer.sampleRate;
  const jumpIntervalSamples = Math.max(1, Math.round(currentJumpIntervalSecondsValue * sampleRate));
  const phaseJumpRadians = (currentPhaseJumpDegreesValue * Math.PI) / 180;
  const phaseIncrement = (2 * Math.PI * currentCarrierFrequencyValue) / sampleRate;

  if (!Number.isFinite(samplesUntilPhaseJump) || samplesUntilPhaseJump <= 0) {
    samplesUntilPhaseJump = jumpIntervalSamples;
  }

  for (let sampleIndex = 0; sampleIndex < leftChannel.length; sampleIndex += 1) {
    let transitionGain = 1;
    if (boundaryTransitionSamplesRemaining > 0) {
      const elapsed = boundaryTransitionTotalSamples - boundaryTransitionSamplesRemaining;
      const halfSamples = Math.max(1, Math.floor(boundaryTransitionTotalSamples / 2));

      if (elapsed >= halfSamples && boundaryTransitionResetPending) {
        resetPhaseJumpCycle(true);
        boundaryTransitionResetPending = false;
      }

      if (elapsed < halfSamples) {
        const t = halfSamples <= 1 ? 1 : elapsed / (halfSamples - 1);
        transitionGain = Math.cos((Math.min(1, t) * Math.PI) / 2);
      } else {
        const secondHalfSamples = Math.max(1, boundaryTransitionTotalSamples - halfSamples);
        const t = secondHalfSamples <= 1 ? 1 : (elapsed - halfSamples) / (secondHalfSamples - 1);
        transitionGain = Math.sin((Math.min(1, t) * Math.PI) / 2);
      }

      boundaryTransitionSamplesRemaining -= 1;
    }

    if (!phaseJumpApplied && samplesUntilPhaseJump <= 0) {
      carrierPhase += phaseJumpRadians;
      phaseJumpApplied = true;
    }

    const sample = Math.sin(carrierPhase);
    leftChannel[sampleIndex] = sample * currentLeftGainValue * transitionGain;
    rightChannel[sampleIndex] = sample * currentRightGainValue * transitionGain;

    carrierPhase += phaseIncrement;
    if (carrierPhase >= Math.PI || carrierPhase <= -Math.PI) {
      carrierPhase = Math.atan2(Math.sin(carrierPhase), Math.cos(carrierPhase));
    }

    if (!phaseJumpApplied) {
      samplesUntilPhaseJump -= 1;
    }
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

    processorNode = audioContext.createScriptProcessor(1024, 0, 2);
    processorNode.onaudioprocess = processPhaseJumpOutput;

    sourceNode.connect(analyserNode);
    processorNode.connect(audioContext.destination);

    resetPhaseJumpCycle(true);
    boundaryTransitionSamplesRemaining = 0;
    boundaryTransitionTotalSamples = 0;
    boundaryTransitionResetPending = false;
    sweepCurrentFrequencyValue = getCurrentPhaseJumpDegrees();
    sweepStepStartTime = null;
    syncToneSettings();

    if (getSweepSettings().enabled) {
      startSweep(true);
    }

    analysisTimerId = window.setInterval(analysisTick, analysisIntervalMs);
    displayTimerId = window.setInterval(displayTick, displayIntervalMs);
    displayTick();

    startButton.disabled = true;
    stopButton.disabled = false;
    setStatus(getSweepSettings().enabled ? "Phase jump experiment running" : "Carrier running");
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

  if (processorNode) {
    processorNode.disconnect();
    processorNode.onaudioprocess = null;
    processorNode = null;
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
  sweepCurrentFrequencyValue = getCurrentPhaseJumpDegrees();
  resetCurrentStepAverage();

  waveformContext.clearRect(0, 0, waveformCanvas.width, waveformCanvas.height);
  fftContext.clearRect(0, 0, fftCanvas.width, fftCanvas.height);
  waveformDirty = true;
  heatmapDirty = true;
  drawWaveformGrid(waveformCanvas.width, waveformCanvas.height);
  drawFftHeatmap();
}

startButton.addEventListener("click", () => {
  void startAudio();
});

stopButton.addEventListener("click", () => {
  void stopAudio();
});

resetFftButton.addEventListener("click", () => {
  clearHeatmap(true);
});

restartSweepButton.addEventListener("click", () => {
  restartSweep();
});

exportCsvButton.addEventListener("click", () => {
  exportHeatmapCsv();
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
heatmapTab.addEventListener("click", () => {
  setActiveView("heatmap");
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

fftSizeSelect.addEventListener("change", applyFftSettings);
smoothingInput.addEventListener("input", applyFftSettings);
minDbInput.addEventListener("blur", commitDbInputs);
minDbInput.addEventListener("change", commitDbInputs);
maxDbInput.addEventListener("blur", commitDbInputs);
maxDbInput.addEventListener("change", commitDbInputs);
subtractColumnBackgroundInput.addEventListener("change", commitBackgroundInputs);
backgroundPercentileInput.addEventListener("blur", commitBackgroundInputs);
backgroundPercentileInput.addEventListener("change", commitBackgroundInputs);

freqScaleSelect.addEventListener("change", () => {
  commitVisibleRangeInputs();
});
displayStartInput.addEventListener("blur", commitVisibleRangeInputs);
displayStartInput.addEventListener("change", commitVisibleRangeInputs);
displayEndInput.addEventListener("blur", commitVisibleRangeInputs);
displayEndInput.addEventListener("change", commitVisibleRangeInputs);

sweepEnabledInput.addEventListener("change", () => {
  if (audioContext && sweepEnabledInput.checked) {
    commitSweepInputs();
    startSweep(true);
    setStatus("Phase jump experiment running");
  } else if (audioContext) {
    stopSweep();
    setStatus("Carrier running");
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
jumpIntervalSecondsInput.addEventListener("blur", commitSweepInputs);
jumpIntervalSecondsInput.addEventListener("change", commitSweepInputs);
sweepLogInput.addEventListener("change", commitSweepInputs);
sweepContinuousInput.addEventListener("change", commitSweepInputs);
sweepLoopInput.addEventListener("change", () => {
  refreshSweepSettings();
  updateControls();
  persistSettings();
});
sweepStepSecondsInput.addEventListener("blur", commitSweepInputs);
sweepStepSecondsInput.addEventListener("change", commitSweepInputs);

loadSettings();
reinitializeFftBuffers();
commitFrequencyInput();
commitSweepInputs();
commitVisibleRangeInputs();
commitDbInputs();
commitBackgroundInputs();
updateControls();
setActiveView(activeView);
drawWaveformGrid(waveformCanvas.width, waveformCanvas.height);
drawFftHeatmap();
