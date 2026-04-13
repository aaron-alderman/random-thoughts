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
const rejectHotFramesInput = document.getElementById("rejectHotFramesInput");
const rejectPercentileInput = document.getElementById("rejectPercentileInput");
const renderRejectHotBinsInput = document.getElementById("renderRejectHotBinsInput");
const renderRejectPercentileInput = document.getElementById("renderRejectPercentileInput");
const subtractColumnBackgroundInput = document.getElementById("subtractColumnBackgroundInput");
const backgroundPercentileInput = document.getElementById("backgroundPercentileInput");
const freqScaleSelect = document.getElementById("freqScaleSelect");
const displayStartInput = document.getElementById("displayStartInput");
const displayEndInput = document.getElementById("displayEndInput");
const fftResolution = document.getElementById("fftResolution");
const fftRange = document.getElementById("fftRange");
const fftAverageCount = document.getElementById("fftAverageCount");
const fftFrameFilterStatus = document.getElementById("fftFrameFilterStatus");
const fftRenderFilterStatus = document.getElementById("fftRenderFilterStatus");
const fftBackgroundStatus = document.getElementById("fftBackgroundStatus");
const fftVisibleBand = document.getElementById("fftVisibleBand");
const sweepEnabledInput = document.getElementById("sweepEnabledInput");
const sweepStartHzInput = document.getElementById("sweepStartHzInput");
const sweepEndHzInput = document.getElementById("sweepEndHzInput");
const sweepStepsInput = document.getElementById("sweepStepsInput");
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
let currentStepFrames = [];
let currentStepFrameScores = [];
let heatmapRows = [];
let sweepCurrentFrequencyValue = 440;
let sweepStepStartTime = null;
let sweepPassStartTime = null;
let currentSweepFrequencies = [];
let currentSweepBoundaries = [];
let currentSweepStepIndex = 0;

const defaultSampleRate = 48000;
const maxOscillatorFrequency = 20000;
const fftAxisPadding = { top: 12, right: 16, bottom: 34, left: 76 };
const fftMarginalLayout = { topHeight: 56, rightWidth: 82, gap: 12 };
const heatmapPalette = buildHeatmapPalette();
const settingsStorageKey = "audio-lab-settings-v1";
const analysisIntervalMs = 100;
const displayIntervalMs = 400;
const maxRenderHistoryPerRow = 64;
const minFrameFilterFrames = 8;
const minRenderFilterVisits = 4;
let activeView = "heatmap";
let waveformDirty = true;
let heatmapDirty = true;

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
    rejectHotFramesInput: rejectHotFramesInput.checked,
    rejectPercentileInput: rejectPercentileInput.value,
    renderRejectHotBinsInput: renderRejectHotBinsInput.checked,
    renderRejectPercentileInput: renderRejectPercentileInput.value,
    subtractColumnBackgroundInput: subtractColumnBackgroundInput.checked,
    backgroundPercentileInput: backgroundPercentileInput.value,
    freqScaleSelect: freqScaleSelect.value,
    displayStartInput: displayStartInput.value,
    displayEndInput: displayEndInput.value,
    sweepEnabledInput: sweepEnabledInput.checked,
    sweepStartHzInput: sweepStartHzInput.value,
    sweepEndHzInput: sweepEndHzInput.value,
    sweepStepsInput: sweepStepsInput.value,
    sweepLogInput: sweepLogInput.checked,
    sweepContinuousInput: sweepContinuousInput.checked,
    sweepLoopInput: sweepLoopInput.checked,
    sweepStepSecondsInput: sweepStepSecondsInput.value,
  };
}

function persistSettings() {
  try {
    window.localStorage.setItem(settingsStorageKey, JSON.stringify(collectSettings()));
  } catch (error) {
    console.warn("Unable to save settings", error);
  }
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
    if (typeof settings.rejectHotFramesInput === "boolean") {
      rejectHotFramesInput.checked = settings.rejectHotFramesInput;
    }
    if (typeof settings.rejectPercentileInput === "string") {
      rejectPercentileInput.value = settings.rejectPercentileInput;
    }
    if (typeof settings.renderRejectHotBinsInput === "boolean") {
      renderRejectHotBinsInput.checked = settings.renderRejectHotBinsInput;
    }
    if (typeof settings.renderRejectPercentileInput === "string") {
      renderRejectPercentileInput.value = settings.renderRejectPercentileInput;
    }
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
    if (typeof settings.sweepLogInput === "boolean") sweepLogInput.checked = settings.sweepLogInput;
    if (typeof settings.sweepContinuousInput === "boolean") {
      sweepContinuousInput.checked = settings.sweepContinuousInput;
    }
    if (typeof settings.sweepLoopInput === "boolean") sweepLoopInput.checked = settings.sweepLoopInput;
    if (typeof settings.sweepStepSecondsInput === "string") {
      sweepStepSecondsInput.value = settings.sweepStepSecondsInput;
    }
  } catch (error) {
    console.warn("Unable to load settings", error);
  }
}

function clampNumber(value, min, max, fallback) {
  if (!Number.isFinite(value)) {
    return fallback;
  }

  return Math.min(max, Math.max(min, value));
}

function formatNumber(value, digits = 1) {
  return Number(value.toFixed(digits)).toString();
}

function formatFrequencyCompact(value) {
  if (value >= 1000) {
    return `${formatNumber(value / 1000, value >= 10000 ? 0 : 1)} kHz`;
  }

  return `${formatNumber(value, value % 1 === 0 ? 0 : 1)} Hz`;
}

function formatBalanceLabel(value) {
  if (value <= -99) {
    return "Left only";
  }
  if (value >= 99) {
    return "Right only";
  }
  if (Math.abs(value) < 0.5) {
    return "Center";
  }

  const magnitude = Math.round(Math.abs(value));
  return value < 0 ? `${magnitude}% left` : `${magnitude}% right`;
}

function buildHeatmapPalette() {
  const stops = [
    { at: 0.0, color: [7, 17, 31] },
    { at: 0.25, color: [25, 86, 168] },
    { at: 0.5, color: [72, 208, 255] },
    { at: 0.75, color: [255, 201, 92] },
    { at: 1.0, color: [255, 91, 140] },
  ];

  const palette = new Array(256);
  for (let i = 0; i < 256; i += 1) {
    const value = i / 255;
    let left = stops[0];
    let right = stops[stops.length - 1];

    for (let j = 0; j < stops.length - 1; j += 1) {
      if (value >= stops[j].at && value <= stops[j + 1].at) {
        left = stops[j];
        right = stops[j + 1];
        break;
      }
    }

    const range = right.at - left.at || 1;
    const ratio = (value - left.at) / range;
    palette[i] = [
      Math.round(left.color[0] + (right.color[0] - left.color[0]) * ratio),
      Math.round(left.color[1] + (right.color[1] - left.color[1]) * ratio),
      Math.round(left.color[2] + (right.color[2] - left.color[2]) * ratio),
    ];
  }

  return palette;
}

function getSampleRate() {
  return audioContext ? audioContext.sampleRate : defaultSampleRate;
}

function getNyquist() {
  return getSampleRate() / 2;
}

function getFftSettings() {
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

  const rejectPercentile = Math.round(clampNumber(Number(rejectPercentileInput.value), 50, 100, 90));
  const renderRejectPercentile = Math.round(
    clampNumber(Number(renderRejectPercentileInput.value), 50, 100, 95)
  );
  const backgroundPercentile = Math.round(clampNumber(Number(backgroundPercentileInput.value), 0, 50, 20));

  return {
    fftSize: Number(fftSizeSelect.value),
    smoothing: Number(smoothingInput.value),
    minDb,
    maxDb,
    rejectHotFrames: rejectHotFramesInput.checked,
    rejectPercentile,
    renderRejectHotBins: renderRejectHotBinsInput.checked,
    renderRejectPercentile,
    subtractColumnBackground: subtractColumnBackgroundInput.checked,
    backgroundPercentile,
    scale: freqScaleSelect.value,
  };
}

function getSweepSettings() {
  let startHz = clampNumber(Number(sweepStartHzInput.value), 20, maxOscillatorFrequency, 440);
  let endHz = clampNumber(Number(sweepEndHzInput.value), 20, maxOscillatorFrequency, 880);

  if (startHz >= endHz) {
    endHz = Math.min(maxOscillatorFrequency, startHz + 0.1);
  }

  return {
    enabled: sweepEnabledInput.checked,
    startHz,
    endHz,
    steps: Math.round(clampNumber(Number(sweepStepsInput.value), 2, 20000, 50)),
    log: sweepLogInput.checked,
    continuous: sweepContinuousInput.checked,
    loop: sweepLoopInput.checked,
    stepSeconds: clampNumber(Number(sweepStepSecondsInput.value), 0.1, 86400, 60),
  };
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

  let start = Number(displayStartInput.value);
  let end = Number(displayEndInput.value);

  if (!Number.isFinite(start)) {
    start = minimumStart;
  }
  if (!Number.isFinite(end)) {
    end = Math.min(12000, nyquist);
  }

  start = Math.max(minimumStart, Math.min(start, nyquist - 1));
  end = Math.max(start + 1, Math.min(end, nyquist));

  return { start, end };
}

function getFrequencyValue() {
  return clampNumber(Number(frequencyInput.value), 20, maxOscillatorFrequency, 440);
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
  fftFrameFilterStatus.textContent = fftSettings.rejectHotFrames
    ? currentStepFrames.length >= minFrameFilterFrames
      ? `P${fftSettings.rejectPercentile} cutoff`
      : `Need ${minFrameFilterFrames} frames`
    : "Off";
  fftRenderFilterStatus.textContent = fftSettings.renderRejectHotBins
    ? heatmapRows.some(
        (row) => Array.isArray(row.visitSpectra) && row.visitSpectra.length >= minRenderFilterVisits
      )
      ? `Per-bin P${fftSettings.renderRejectPercentile}`
      : `Need ${minRenderFilterVisits} visits`
    : "Off";
  fftBackgroundStatus.textContent = fftSettings.subtractColumnBackground
    ? heatmapRows.length >= 2
      ? `Per-column P${fftSettings.backgroundPercentile}`
      : "Need 2 rows"
    : "Off";
  fftVisibleBand.textContent = `${formatFrequencyCompact(visibleRange.start)} to ${formatFrequencyCompact(
    visibleRange.end
  )}`;

  const displayedFrequency = isSweepActive() ? sweepCurrentFrequencyValue : getFrequencyValue();
  sweepCurrentFrequency.textContent = formatFrequencyCompact(displayedFrequency);
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
  currentStepFrames = [];
  currentStepFrameScores = [];
  updateControls();
}

function reinitializeFftBuffers() {
  const binCount = Number(fftSizeSelect.value) / 2;
  fftFrameData = new Float32Array(binCount);
  resetCurrentStepAverage();
}

function clearHeatmap(resetSweepTimer = false) {
  heatmapRows = [];
  resetCurrentStepAverage();

  if (resetSweepTimer && audioContext) {
    sweepStepStartTime = audioContext.currentTime;
    sweepPassStartTime = audioContext.currentTime;
  }

  updateControls();
  heatmapDirty = true;
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
  applyFftSettings();
  persistSettings();
}

function commitFrameFilterInputs() {
  const fftSettings = getFftSettings();
  rejectPercentileInput.value = String(fftSettings.rejectPercentile);
  renderRejectPercentileInput.value = String(fftSettings.renderRejectPercentile);
  backgroundPercentileInput.value = String(fftSettings.backgroundPercentile);
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function commitVisibleRangeInputs() {
  const visibleRange = getVisibleFrequencyRange(getFftSettings().scale);
  displayStartInput.value = formatNumber(visibleRange.start, visibleRange.start % 1 === 0 ? 0 : 1);
  displayEndInput.value = formatNumber(visibleRange.end, visibleRange.end % 1 === 0 ? 0 : 1);
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function commitSweepInputs() {
  const sweepSettings = getSweepSettings();
  sweepStartHzInput.value = formatNumber(sweepSettings.startHz, sweepSettings.startHz % 1 === 0 ? 0 : 1);
  sweepEndHzInput.value = formatNumber(sweepSettings.endHz, sweepSettings.endHz % 1 === 0 ? 0 : 1);
  sweepStepsInput.value = String(sweepSettings.steps);
  sweepStepSecondsInput.value = formatNumber(
    sweepSettings.stepSeconds,
    sweepSettings.stepSeconds % 1 === 0 ? 0 : 1
  );
  updateControls();
  persistSettings();
}

function applyFftSettings() {
  const settings = getFftSettings();

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

  rejectPercentileInput.value = String(settings.rejectPercentile);
  renderRejectPercentileInput.value = String(settings.renderRejectPercentile);
  backgroundPercentileInput.value = String(settings.backgroundPercentile);
  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function startSweep(resetRows = true) {
  const sweepSettings = getSweepSettings();
  currentSweepFrequencies = buildSweepFrequencies(sweepSettings);
  currentSweepBoundaries = buildSweepBoundaries(sweepSettings, currentSweepFrequencies);
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = currentSweepFrequencies[0];
  frequencyInput.value = formatNumber(
    sweepCurrentFrequencyValue,
    sweepCurrentFrequencyValue % 1 === 0 ? 0 : 1
  );
  sweepStepStartTime = audioContext ? audioContext.currentTime : null;
  sweepPassStartTime = audioContext ? audioContext.currentTime : null;

  if (resetRows) {
    heatmapRows = [];
  }

  resetCurrentStepAverage();
  syncToneSettings();
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
  sweepPassStartTime = null;
  resetCurrentStepAverage();
  currentSweepFrequencies = [];
  currentSweepBoundaries = [];
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = getFrequencyValue();
  syncToneSettings();
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

  const committedSpectrum = buildCommittedStepSpectrum();
  upsertHeatmapRow(getActiveSweepRowFrequency(), committedSpectrum, 1);
  return true;
}

function upsertHeatmapRow(frequency, spectrum, visitCount = 1) {
  const tolerance = 1e-6;
  const existingRow = heatmapRows.find((row) => Math.abs(row.frequency - frequency) <= tolerance);

  if (!existingRow) {
    heatmapRows.push({
      frequency,
      spectrum: spectrum.slice(),
      visits: visitCount,
      visitSpectra: [spectrum.slice()],
    });
    heatmapRows.sort((left, right) => left.frequency - right.frequency);
    return;
  }

  const nextVisits = existingRow.visits + visitCount;
  for (let i = 0; i < existingRow.spectrum.length; i += 1) {
    existingRow.spectrum[i] =
      existingRow.spectrum[i] + ((spectrum[i] - existingRow.spectrum[i]) * visitCount) / nextVisits;
  }
  existingRow.visits = nextVisits;
  if (!Array.isArray(existingRow.visitSpectra)) {
    existingRow.visitSpectra = [];
  }
  existingRow.visitSpectra.push(spectrum.slice());
  if (existingRow.visitSpectra.length > maxRenderHistoryPerRow) {
    existingRow.visitSpectra.shift();
  }
}

function computePercentile(sortedValues, percentile) {
  if (sortedValues.length === 0) {
    return Number.NaN;
  }

  const rank = (percentile / 100) * (sortedValues.length - 1);
  const lowerIndex = Math.floor(rank);
  const upperIndex = Math.ceil(rank);

  if (lowerIndex === upperIndex) {
    return sortedValues[lowerIndex];
  }

  const weight = rank - lowerIndex;
  return sortedValues[lowerIndex] + (sortedValues[upperIndex] - sortedValues[lowerIndex]) * weight;
}

function buildCommittedStepSpectrum() {
  const fftSettings = getFftSettings();

  if (
    !fftSettings.rejectHotFrames ||
    currentStepFrames.length === 0 ||
    currentStepFrames.length < minFrameFilterFrames
  ) {
    return currentStepAverageData.slice();
  }

  const sortedScores = [...currentStepFrameScores].sort((left, right) => left - right);
  const threshold = computePercentile(sortedScores, fftSettings.rejectPercentile);
  const keptFrames = [];

  for (let index = 0; index < currentStepFrameScores.length; index += 1) {
    if (currentStepFrameScores[index] <= threshold) {
      keptFrames.push(currentStepFrames[index]);
    }
  }

  if (keptFrames.length === 0) {
    return currentStepAverageData.slice();
  }

  const spectrum = new Float32Array(fftFrameData.length);
  spectrum.fill(fftSettings.minDb);

  for (let frameIndex = 0; frameIndex < keptFrames.length; frameIndex += 1) {
    const frame = keptFrames[frameIndex];
    const sampleCount = frameIndex + 1;
    for (let binIndex = 0; binIndex < frame.length; binIndex += 1) {
      spectrum[binIndex] += (frame[binIndex] - spectrum[binIndex]) / sampleCount;
    }
  }

  return spectrum;
}

function buildRenderedSpectrum(row, fftSettings) {
  if (
    !fftSettings.renderRejectHotBins ||
    !Array.isArray(row.visitSpectra) ||
    row.visitSpectra.length < minRenderFilterVisits
  ) {
    return row.spectrum;
  }

  const rendered = new Float32Array(row.spectrum.length);
  const history = row.visitSpectra;

  for (let binIndex = 0; binIndex < rendered.length; binIndex += 1) {
    const values = new Array(history.length);
    for (let visitIndex = 0; visitIndex < history.length; visitIndex += 1) {
      values[visitIndex] = history[visitIndex][binIndex];
    }

    values.sort((left, right) => left - right);
    const threshold = computePercentile(values, fftSettings.renderRejectPercentile);

    let keptSum = 0;
    let keptCount = 0;
    for (let visitIndex = 0; visitIndex < history.length; visitIndex += 1) {
      const value = history[visitIndex][binIndex];
      if (value <= threshold) {
        keptSum += value;
        keptCount += 1;
      }
    }

    if (keptCount === 0) {
      rendered[binIndex] = row.spectrum[binIndex];
    } else {
      rendered[binIndex] = keptSum / keptCount;
    }
  }

  return rendered;
}

function buildColumnBackground(rows, fftSettings) {
  if (
    !fftSettings.subtractColumnBackground ||
    rows.length < 2
  ) {
    return null;
  }

  const background = new Float32Array(rows[0].renderedSpectrum.length);
  for (let binIndex = 0; binIndex < background.length; binIndex += 1) {
    const values = new Array(rows.length);
    for (let rowIndex = 0; rowIndex < rows.length; rowIndex += 1) {
      values[rowIndex] = rows[rowIndex].renderedSpectrum[binIndex];
    }

    values.sort((left, right) => left - right);
    const baseline = computePercentile(values, fftSettings.backgroundPercentile);
    background[binIndex] = Number.isFinite(baseline) ? baseline : fftSettings.minDb;
  }

  return background;
}

function subtractColumnBackground(spectrum, background, minDb) {
  if (!background) {
    return spectrum;
  }

  const floorPower = 10 ** (minDb / 10);
  const adjustedSpectrum = new Float32Array(spectrum.length);

  for (let binIndex = 0; binIndex < spectrum.length; binIndex += 1) {
    const signalPower = 10 ** (spectrum[binIndex] / 10);
    const backgroundPower = 10 ** (background[binIndex] / 10);
    const residualPower = Math.max(floorPower, signalPower - backgroundPower);
    adjustedSpectrum[binIndex] = 10 * Math.log10(residualPower);
  }

  return adjustedSpectrum;
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

  frequencyInput.value = formatNumber(
    sweepCurrentFrequencyValue,
    sweepCurrentFrequencyValue % 1 === 0 ? 0 : 1
  );
  sweepStepStartTime = audioContext.currentTime;
  resetCurrentStepAverage();
  syncToneSettings();
}

function advanceContinuousSweep(currentTime, sweepSettings) {
  const totalDuration = sweepSettings.stepSeconds * currentSweepFrequencies.length;
  if (!Number.isFinite(totalDuration) || totalDuration <= 0) {
    return;
  }

  if (sweepPassStartTime === null) {
    sweepPassStartTime = currentTime;
  }

  const elapsedPass = Math.max(0, currentTime - sweepPassStartTime);
  const progress = Math.min(1, elapsedPass / totalDuration);
  const frequency = getSweepFrequencyAtProgress(sweepSettings, progress);
  const targetIndex = getSweepBinIndex(frequency);

  while (currentSweepStepIndex < targetIndex) {
    commitCurrentSweepBin();
    currentSweepStepIndex += 1;
    sweepStepStartTime = currentTime;
    resetCurrentStepAverage();
    heatmapDirty = true;
  }

  sweepCurrentFrequencyValue = frequency;
  applyOscillatorFrequency(frequency);

  if (elapsedPass >= totalDuration) {
    commitCurrentSweepBin();
    heatmapDirty = true;

    if (sweepSettings.loop) {
      currentSweepStepIndex = 0;
      sweepPassStartTime = currentTime;
      sweepStepStartTime = currentTime;
      sweepCurrentFrequencyValue = currentSweepFrequencies[0];
      resetCurrentStepAverage();
      syncToneSettings();
    } else {
      sweepEnabledInput.checked = false;
      stopSweep();
      setStatus(`Sweep completed at ${formatFrequencyCompact(sweepSettings.endHz)}`);
    }
  }
}

function accumulateCurrentStep(minDb) {
  const frame = new Float32Array(fftFrameData.length);
  let powerSum = 0;

  currentStepFrameCount += 1;

  for (let i = 0; i < fftFrameData.length; i += 1) {
    const sample = Number.isFinite(fftFrameData[i]) ? fftFrameData[i] : minDb;
    frame[i] = sample;
    powerSum += 10 ** (sample / 10);
    const previous = currentStepAverageData[i];
    currentStepAverageData[i] = previous + (sample - previous) / currentStepFrameCount;
  }

  currentStepFrames.push(frame);
  currentStepFrameScores.push(powerSum / fftFrameData.length);
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

function getHeatmapLayout(width, height) {
  const plotWidth = Math.max(160, width - fftAxisPadding.left - fftAxisPadding.right);
  const plotHeight = Math.max(120, height - fftAxisPadding.top - fftAxisPadding.bottom);
  const heatmapWidth = Math.max(80, plotWidth - fftMarginalLayout.rightWidth - fftMarginalLayout.gap);
  const heatmapHeight = Math.max(80, plotHeight - fftMarginalLayout.topHeight - fftMarginalLayout.gap);

  return {
    heatmapX: fftAxisPadding.left,
    heatmapY: fftAxisPadding.top + fftMarginalLayout.topHeight + fftMarginalLayout.gap,
    heatmapWidth,
    heatmapHeight,
    topX: fftAxisPadding.left,
    topY: fftAxisPadding.top,
    topWidth: heatmapWidth,
    topHeight: fftMarginalLayout.topHeight,
    rightX: fftAxisPadding.left + heatmapWidth + fftMarginalLayout.gap,
    rightY: fftAxisPadding.top + fftMarginalLayout.topHeight + fftMarginalLayout.gap,
    rightWidth: fftMarginalLayout.rightWidth,
    rightHeight: heatmapHeight,
  };
}

function getFrequencyForX(x, width, scale, minFrequency, maxFrequency) {
  if (scale === "log") {
    const logMin = Math.log10(minFrequency);
    const logMax = Math.log10(maxFrequency);
    const ratio = width <= 1 ? 0 : x / (width - 1);
    return 10 ** (logMin + (logMax - logMin) * ratio);
  }

  const ratio = width <= 1 ? 0 : x / (width - 1);
  return minFrequency + (maxFrequency - minFrequency) * ratio;
}

function getFrequencyX(frequency, width, scale, minFrequency, maxFrequency) {
  const safeFrequency = Math.min(maxFrequency, Math.max(minFrequency, frequency));

  if (scale === "log") {
    const logMin = Math.log10(minFrequency);
    const logMax = Math.log10(maxFrequency);
    const logValue = Math.log10(safeFrequency);
    return ((logValue - logMin) / (logMax - logMin)) * width;
  }

  return ((safeFrequency - minFrequency) / (maxFrequency - minFrequency)) * width;
}

function getSweepScaleSettings(rows) {
  const sweepSettings = getSweepSettings();
  const fallbackMin = sweepSettings.log ? Math.max(20, sweepSettings.startHz) : sweepSettings.startHz;
  let minFrequency = fallbackMin;
  let maxFrequency = sweepSettings.endHz;

  if (rows.length > 0) {
    minFrequency = rows[0].frequency;
    maxFrequency = rows[rows.length - 1].frequency;
  }

  if (sweepSettings.log) {
    minFrequency = Math.max(20, minFrequency);
  }
  if (minFrequency >= maxFrequency) {
    maxFrequency = minFrequency + 0.1;
  }

  return {
    minFrequency,
    maxFrequency,
    log: sweepSettings.log,
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

function buildHeatmapRowGeometry(rows, chartHeight, scaleSettings) {
  const centers = new Float32Array(rows.length);
  const pixelRowIndices = new Uint32Array(chartHeight);

  if (rows.length === 0) {
    return { centers, pixelRowIndices };
  }

  if (rows.length === 1) {
    centers[0] = chartHeight * 0.5;
    pixelRowIndices.fill(0);
    return { centers, pixelRowIndices };
  }

  for (let rowIndex = 0; rowIndex < rows.length; rowIndex += 1) {
    centers[rowIndex] = getSweepY(rows[rowIndex].frequency, chartHeight, scaleSettings);
  }

  const boundaries = new Float32Array(rows.length + 1);
  boundaries[0] = 0;
  boundaries[rows.length] = chartHeight;
  for (let rowIndex = 1; rowIndex < rows.length; rowIndex += 1) {
    boundaries[rowIndex] = (centers[rowIndex - 1] + centers[rowIndex]) * 0.5;
  }

  let boundaryIndex = 1;
  for (let y = 0; y < chartHeight; y += 1) {
    const yCenter = y + 0.5;
    while (boundaryIndex < boundaries.length - 1 && yCenter >= boundaries[boundaryIndex]) {
      boundaryIndex += 1;
    }
    pixelRowIndices[y] = boundaryIndex - 1;
  }

  return { centers, pixelRowIndices };
}

function getNiceLinearTickStep(range) {
  const roughStep = range / 5;
  const magnitude = 10 ** Math.floor(Math.log10(Math.max(roughStep, 1)));
  const normalized = roughStep / magnitude;

  if (normalized <= 1) {
    return magnitude;
  }
  if (normalized <= 2) {
    return 2 * magnitude;
  }
  if (normalized <= 5) {
    return 5 * magnitude;
  }

  return 10 * magnitude;
}

function getFrequencyTickValues(scale, minFrequency, maxFrequency) {
  if (scale === "log") {
    const ticks = [];
    const startExponent = Math.floor(Math.log10(Math.max(1, minFrequency)));
    const endExponent = Math.ceil(Math.log10(maxFrequency));
    const multipliers = [1, 2, 5];

    for (let exponent = startExponent; exponent <= endExponent; exponent += 1) {
      const base = 10 ** exponent;
      for (const multiplier of multipliers) {
        const tick = multiplier * base;
        if (tick >= minFrequency && tick <= maxFrequency) {
          ticks.push(tick);
        }
      }
    }

    return ticks;
  }

  const step = getNiceLinearTickStep(maxFrequency - minFrequency);
  const firstTick = Math.ceil(minFrequency / step) * step;
  const ticks = [];

  for (let tick = firstTick; tick <= maxFrequency; tick += step) {
    ticks.push(tick);
  }

  return ticks;
}

function getDisplayRows() {
  const rows = heatmapRows.map((row) => ({ ...row, spectrum: row.spectrum.slice() }));

  if (isSweepActive() && currentStepFrameCount > 0) {
    const previewRow = {
      frequency: getActiveSweepRowFrequency(),
      spectrum: currentStepAverageData,
      preview: true,
    };
    const existingIndex = rows.findIndex((row) => Math.abs(row.frequency - previewRow.frequency) <= 1e-6);

    if (existingIndex >= 0) {
      rows[existingIndex] = previewRow;
    } else {
      rows.push(previewRow);
      rows.sort((left, right) => left.frequency - right.frequency);
    }
  }

  return rows;
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
    "sweep_frequency_hz",
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
  anchor.download = `audio-lab-heatmap-${timestamp}.csv`;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
  setStatus(`Exported ${heatmapRows.length} heatmap row${heatmapRows.length === 1 ? "" : "s"} to CSV`);
}

function drawHeatmapAxes(layout, settings, minFrequency, maxFrequency, rows, rowGeometry) {
  const xTicks = getFrequencyTickValues(settings.scale, minFrequency, maxFrequency);
  const yTickCount = Math.min(6, Math.max(rows.length, 2));
  const yLabelX = -10;

  fftContext.save();
  fftContext.translate(layout.heatmapX, layout.heatmapY);
  fftContext.strokeStyle = "rgba(255, 255, 255, 0.08)";
  fftContext.fillStyle = "rgba(238, 247, 255, 0.78)";
  fftContext.lineWidth = 1;
  fftContext.font = "12px 'Segoe UI'";

  for (const frequency of xTicks) {
    const x = getFrequencyX(frequency, layout.heatmapWidth, settings.scale, minFrequency, maxFrequency);
    if (x <= 2) {
      fftContext.textAlign = "left";
    } else if (x >= layout.heatmapWidth - 2) {
      fftContext.textAlign = "right";
    } else {
      fftContext.textAlign = "center";
    }
    fftContext.beginPath();
    fftContext.moveTo(x, 0);
    fftContext.lineTo(x, layout.heatmapHeight);
    fftContext.stroke();
    fftContext.fillText(formatFrequencyCompact(frequency), x, layout.heatmapHeight + 18);
  }

  fftContext.textAlign = "right";
  if (rows.length > 0) {
    for (let i = 0; i < yTickCount; i += 1) {
      const rowIndex = rows.length === 1 ? 0 : Math.round((i / (yTickCount - 1)) * (rows.length - 1));
      const y = rowGeometry.centers[rowIndex];
      fftContext.beginPath();
      fftContext.moveTo(0, y);
      fftContext.lineTo(layout.heatmapWidth, y);
      fftContext.stroke();
      fftContext.fillText(formatFrequencyCompact(rows[rowIndex].frequency), yLabelX, y + 4);
    }
  } else {
    fftContext.beginPath();
    fftContext.moveTo(0, layout.heatmapHeight * 0.5);
    fftContext.lineTo(layout.heatmapWidth, layout.heatmapHeight * 0.5);
    fftContext.stroke();
    fftContext.fillText("No sweep rows yet", yLabelX, layout.heatmapHeight * 0.5 + 4);
  }

  fftContext.strokeStyle = "rgba(255, 255, 255, 0.18)";
  fftContext.beginPath();
  fftContext.moveTo(0, 0);
  fftContext.lineTo(0, layout.heatmapHeight);
  fftContext.lineTo(layout.heatmapWidth, layout.heatmapHeight);
  fftContext.stroke();

  fftContext.fillStyle = "rgba(238, 247, 255, 0.92)";
  fftContext.textAlign = "center";
  fftContext.fillText("Response frequency", layout.heatmapWidth / 2, layout.heatmapHeight + 32);

  fftContext.save();
  fftContext.translate(18, layout.heatmapHeight / 2);
  fftContext.rotate(-Math.PI / 2);
  fftContext.fillText("Driven sweep frequency", 0, 0);
  fftContext.restore();

  fftContext.restore();
}

function buildHeatmapMarginals(renderedRows, columnBins) {
  const binCount = renderedRows.length > 0 ? renderedRows[0].renderedSpectrum.length : 0;
  const columnTotals = new Float32Array(binCount);
  const rowTotals = new Float32Array(renderedRows.length);

  for (let rowIndex = 0; rowIndex < renderedRows.length; rowIndex += 1) {
    const row = renderedRows[rowIndex];
    let rowTotal = 0;

    for (let binIndex = 0; binIndex < row.renderedSpectrum.length; binIndex += 1) {
      const dbValue = row.renderedSpectrum[binIndex];
      const power = 10 ** (dbValue / 10);
      columnTotals[binIndex] += power;
    }

    for (let x = 0; x < columnBins.length; x += 1) {
      const dbValue = row.renderedSpectrum[columnBins[x]];
      const power = 10 ** (dbValue / 10);
      rowTotal += power;
    }

    rowTotals[rowIndex] = rowTotal;
  }

  return { columnTotals, rowTotals };
}

function drawTopMarginal(layout, columnTotals, settings, minFrequency, maxFrequency, nyquist) {
  fftContext.save();
  fftContext.translate(layout.topX, layout.topY);
  fftContext.strokeStyle = "rgba(255, 255, 255, 0.14)";
  fftContext.fillStyle = "rgba(255, 255, 255, 0.03)";
  fftContext.lineWidth = 1;
  fftContext.font = "12px 'Segoe UI'";
  fftContext.fillRect(0, 0, layout.topWidth, layout.topHeight);
  fftContext.strokeRect(0, 0, layout.topWidth, layout.topHeight);
  fftContext.fillStyle = "rgba(238, 247, 255, 0.72)";
  fftContext.textAlign = "left";
  fftContext.fillText("Column cumulative", 10, 14);

  if (columnTotals.length > 0) {
    const maxTotal = Math.max(...columnTotals, 1e-12);
    const chartTop = 22;
    const chartBottom = layout.topHeight - 6;
    const chartRange = Math.max(1, chartBottom - chartTop);
    const binWidthHz = nyquist / columnTotals.length;
    let started = false;

    fftContext.fillStyle = "rgba(110, 231, 255, 0.18)";
    fftContext.strokeStyle = "rgba(110, 231, 255, 0.92)";
    fftContext.beginPath();
    for (let binIndex = 0; binIndex < columnTotals.length; binIndex += 1) {
      const leftFrequency = binIndex * binWidthHz;
      const rightFrequency = (binIndex + 1) * binWidthHz;

      if (rightFrequency < minFrequency || leftFrequency > maxFrequency) {
        continue;
      }

      const leftX = Math.max(
        0,
        Math.min(layout.topWidth, getFrequencyX(leftFrequency, layout.topWidth, settings.scale, minFrequency, maxFrequency))
      );
      const rightX = Math.max(
        0,
        Math.min(layout.topWidth, getFrequencyX(rightFrequency, layout.topWidth, settings.scale, minFrequency, maxFrequency))
      );
      const y = chartBottom - (columnTotals[binIndex] / maxTotal) * chartRange;

      if (!started) {
        fftContext.moveTo(leftX, chartBottom);
        fftContext.lineTo(leftX, y);
        started = true;
      } else {
        fftContext.lineTo(leftX, y);
      }

      fftContext.lineTo(rightX, y);
    }

    if (started) {
      fftContext.lineTo(layout.topWidth, chartBottom);
      fftContext.closePath();
      fftContext.fill();
    }

    fftContext.beginPath();
    started = false;
    for (let binIndex = 0; binIndex < columnTotals.length; binIndex += 1) {
      const leftFrequency = binIndex * binWidthHz;
      const rightFrequency = (binIndex + 1) * binWidthHz;

      if (rightFrequency < minFrequency || leftFrequency > maxFrequency) {
        continue;
      }

      const leftX = Math.max(
        0,
        Math.min(layout.topWidth, getFrequencyX(leftFrequency, layout.topWidth, settings.scale, minFrequency, maxFrequency))
      );
      const rightX = Math.max(
        0,
        Math.min(layout.topWidth, getFrequencyX(rightFrequency, layout.topWidth, settings.scale, minFrequency, maxFrequency))
      );
      const y = chartBottom - (columnTotals[binIndex] / maxTotal) * chartRange;

      if (!started) {
        fftContext.moveTo(leftX, y);
        started = true;
      } else {
        fftContext.lineTo(leftX, y);
      }
      fftContext.lineTo(rightX, y);
    }

    if (started) {
      fftContext.stroke();
    }
  }

  fftContext.restore();
}

function drawRightMarginal(layout, rowTotals, rowGeometry) {
  fftContext.save();
  fftContext.translate(layout.rightX, layout.rightY);
  fftContext.strokeStyle = "rgba(255, 255, 255, 0.14)";
  fftContext.fillStyle = "rgba(255, 255, 255, 0.03)";
  fftContext.lineWidth = 1;
  fftContext.font = "12px 'Segoe UI'";
  fftContext.fillRect(0, 0, layout.rightWidth, layout.rightHeight);
  fftContext.strokeRect(0, 0, layout.rightWidth, layout.rightHeight);

  fftContext.save();
  fftContext.translate(layout.rightWidth - 14, layout.rightHeight / 2);
  fftContext.rotate(-Math.PI / 2);
  fftContext.fillStyle = "rgba(238, 247, 255, 0.72)";
  fftContext.textAlign = "center";
  fftContext.fillText("Row cumulative", 0, 0);
  fftContext.restore();

  if (rowTotals.length > 0) {
    const maxTotal = Math.max(...rowTotals, 1e-12);
    const chartWidth = layout.rightWidth - 12;

    fftContext.fillStyle = "rgba(255, 111, 145, 0.18)";
    fftContext.strokeStyle = "rgba(255, 111, 145, 0.92)";
    fftContext.beginPath();
    fftContext.moveTo(0, 0);

    for (let rowIndex = 0; rowIndex < rowTotals.length; rowIndex += 1) {
      const y = rowGeometry.centers[rowIndex];
      const x = (rowTotals[rowIndex] / maxTotal) * chartWidth;
      if (rowIndex === 0) {
        fftContext.lineTo(x, y);
      } else {
        fftContext.lineTo(x, y);
      }
    }

    fftContext.lineTo(0, layout.rightHeight);
    fftContext.closePath();
    fftContext.fill();

    fftContext.beginPath();
    for (let rowIndex = 0; rowIndex < rowTotals.length; rowIndex += 1) {
      const y = rowGeometry.centers[rowIndex];
      const x = (rowTotals[rowIndex] / maxTotal) * chartWidth;
      if (rowIndex === 0) {
        fftContext.moveTo(x, y);
      } else {
        fftContext.lineTo(x, y);
      }
    }
    fftContext.stroke();
  }

  fftContext.restore();
}

function drawFftHeatmap() {
  const { width, height } = fftCanvas;
  const settings = getFftSettings();
  const visibleRange = getVisibleFrequencyRange(settings.scale);
  const layout = getHeatmapLayout(width, height);
  const rows = getDisplayRows();
  const committedRenderedRows = heatmapRows.map((row) => ({
    ...row,
    renderedSpectrum: buildRenderedSpectrum(row, settings),
  }));
  const columnBackground = buildColumnBackground(committedRenderedRows, settings);
  const renderedRows = rows.map((row) => ({
    ...row,
    renderedSpectrum: subtractColumnBackground(
      buildRenderedSpectrum(row, settings),
      columnBackground,
      settings.minDb
    ),
  }));
  const sweepScaleSettings = getSweepScaleSettings(renderedRows);
  const rowGeometry = buildHeatmapRowGeometry(renderedRows, layout.heatmapHeight, sweepScaleSettings);
  const nyquist = getNyquist();

  fftContext.clearRect(0, 0, width, height);
  drawHeatmapAxes(layout, settings, visibleRange.start, visibleRange.end, renderedRows, rowGeometry);

  if (renderedRows.length === 0) {
    return;
  }

  const columnBins = new Uint32Array(layout.heatmapWidth);
  for (let x = 0; x < layout.heatmapWidth; x += 1) {
    const frequency = getFrequencyForX(
      x,
      layout.heatmapWidth,
      settings.scale,
      visibleRange.start,
      visibleRange.end
    );
    const binIndex = Math.min(
      renderedRows[0].renderedSpectrum.length - 1,
      Math.max(0, Math.floor((frequency / nyquist) * renderedRows[0].renderedSpectrum.length))
    );
    columnBins[x] = binIndex;
  }

  const { columnTotals, rowTotals } = buildHeatmapMarginals(renderedRows, columnBins);
  drawTopMarginal(layout, columnTotals, settings, visibleRange.start, visibleRange.end, nyquist);
  drawRightMarginal(layout, rowTotals, rowGeometry);

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

    if (sweepSettings.continuous) {
      advanceContinuousSweep(audioContext.currentTime, sweepSettings);
      if (!sweepEnabledInput.checked) {
        return;
      }
      accumulateCurrentStep(fftSettings.minDb);
    } else {
      accumulateCurrentStep(fftSettings.minDb);

      if (audioContext.currentTime - sweepStepStartTime >= sweepSettings.stepSeconds) {
        finalizeSweepStep();
        heatmapDirty = true;
      }
    }
  } else {
    sweepCurrentFrequencyValue = getFrequencyValue();
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
  sweepCurrentFrequencyValue = getFrequencyValue();
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
rejectHotFramesInput.addEventListener("change", commitFrameFilterInputs);
rejectPercentileInput.addEventListener("blur", commitFrameFilterInputs);
rejectPercentileInput.addEventListener("change", commitFrameFilterInputs);
renderRejectHotBinsInput.addEventListener("change", commitFrameFilterInputs);
renderRejectPercentileInput.addEventListener("blur", commitFrameFilterInputs);
renderRejectPercentileInput.addEventListener("change", commitFrameFilterInputs);
subtractColumnBackgroundInput.addEventListener("change", commitFrameFilterInputs);
backgroundPercentileInput.addEventListener("blur", commitFrameFilterInputs);
backgroundPercentileInput.addEventListener("change", commitFrameFilterInputs);

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
commitFrameFilterInputs();
updateControls();
setActiveView(activeView);
drawWaveformGrid(waveformCanvas.width, waveformCanvas.height);
drawFftHeatmap();
