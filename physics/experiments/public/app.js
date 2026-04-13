const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopButton");
const resetFftButton = document.getElementById("resetFftButton");
const toneEnabled = document.getElementById("toneEnabled");
const frequencyInput = document.getElementById("frequencyInput");
const amplitudeInput = document.getElementById("amplitudeInput");
const amplitudeValue = document.getElementById("amplitudeValue");
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
const freqScaleSelect = document.getElementById("freqScaleSelect");
const displayStartInput = document.getElementById("displayStartInput");
const displayEndInput = document.getElementById("displayEndInput");
const fftResolution = document.getElementById("fftResolution");
const fftRange = document.getElementById("fftRange");
const fftAverageCount = document.getElementById("fftAverageCount");
const fftVisibleBand = document.getElementById("fftVisibleBand");
const sweepEnabledInput = document.getElementById("sweepEnabledInput");
const sweepStartHzInput = document.getElementById("sweepStartHzInput");
const sweepEndHzInput = document.getElementById("sweepEndHzInput");
const sweepStepsInput = document.getElementById("sweepStepsInput");
const sweepLogInput = document.getElementById("sweepLogInput");
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
let analysisTimerId = null;
let displayTimerId = null;

const waveformBufferLength = 2048;
const waveformData = new Float32Array(waveformBufferLength);

let fftFrameData = new Float32Array(1024);
let currentStepAverageData = new Float32Array(1024);
let currentStepFrameCount = 0;
let heatmapRows = [];
let sweepCurrentFrequencyValue = 440;
let sweepStepStartTime = null;
let currentSweepFrequencies = [];
let currentSweepStepIndex = 0;

const defaultSampleRate = 48000;
const maxOscillatorFrequency = 20000;
const fftAxisPadding = { top: 12, right: 16, bottom: 34, left: 76 };
const heatmapPalette = buildHeatmapPalette();
const settingsStorageKey = "audio-lab-settings-v1";
const analysisIntervalMs = 100;
const displayIntervalMs = 400;
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
    fftSizeSelect: fftSizeSelect.value,
    smoothingInput: smoothingInput.value,
    minDbInput: minDbInput.value,
    maxDbInput: maxDbInput.value,
    freqScaleSelect: freqScaleSelect.value,
    displayStartInput: displayStartInput.value,
    displayEndInput: displayEndInput.value,
    sweepEnabledInput: sweepEnabledInput.checked,
    sweepStartHzInput: sweepStartHzInput.value,
    sweepEndHzInput: sweepEndHzInput.value,
    sweepStepsInput: sweepStepsInput.value,
    sweepLogInput: sweepLogInput.checked,
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
    if (typeof settings.fftSizeSelect === "string") fftSizeSelect.value = settings.fftSizeSelect;
    if (typeof settings.smoothingInput === "string") smoothingInput.value = settings.smoothingInput;
    if (typeof settings.minDbInput === "string") minDbInput.value = settings.minDbInput;
    if (typeof settings.maxDbInput === "string") maxDbInput.value = settings.maxDbInput;
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

  return {
    fftSize: Number(fftSizeSelect.value),
    smoothing: Number(smoothingInput.value),
    minDb,
    maxDb,
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

  amplitudeValue.textContent = `${amplitudeInput.value}%`;
  smoothingValue.textContent = fftSettings.smoothing.toFixed(2);
  fftRange.textContent = `${Math.round(fftSettings.minDb)} dB to ${Math.round(fftSettings.maxDb)} dB`;
  fftResolution.textContent = `${resolutionHz.toFixed(1)} Hz/bin`;
  fftAverageCount.textContent = `${currentStepFrameCount} frame${currentStepFrameCount === 1 ? "" : "s"}`;
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
  const frequency = isSweepActive() ? sweepCurrentFrequencyValue : getFrequencyValue();

  applyOscillatorFrequency(frequency);
  gainNode.gain.setValueAtTime(toneEnabled.checked ? amplitude : 0, now);
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

  updateControls();
  heatmapDirty = true;
  persistSettings();
}

function startSweep(resetRows = true) {
  const sweepSettings = getSweepSettings();
  currentSweepFrequencies = buildSweepFrequencies(sweepSettings);
  currentSweepStepIndex = 0;
  sweepCurrentFrequencyValue = currentSweepFrequencies[0];
  frequencyInput.value = formatNumber(
    sweepCurrentFrequencyValue,
    sweepCurrentFrequencyValue % 1 === 0 ? 0 : 1
  );
  sweepStepStartTime = audioContext ? audioContext.currentTime : null;

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
  resetCurrentStepAverage();
  currentSweepFrequencies = [];
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

function upsertHeatmapRow(frequency, spectrum, visitCount = 1) {
  const tolerance = 1e-6;
  const existingRow = heatmapRows.find((row) => Math.abs(row.frequency - frequency) <= tolerance);

  if (!existingRow) {
    heatmapRows.push({
      frequency,
      spectrum: spectrum.slice(),
      visits: visitCount,
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
}

function finalizeSweepStep() {
  if (currentStepFrameCount === 0) {
    sweepStepStartTime = audioContext ? audioContext.currentTime : null;
    return;
  }

  upsertHeatmapRow(sweepCurrentFrequencyValue, currentStepAverageData, 1);

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
      frequency: sweepCurrentFrequencyValue,
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

function drawHeatmapAxes(chartWidth, chartHeight, settings, minFrequency, maxFrequency, rows) {
  const xTicks = getFrequencyTickValues(settings.scale, minFrequency, maxFrequency);
  const yTickCount = Math.min(6, Math.max(rows.length, 2));

  fftContext.save();
  fftContext.translate(fftAxisPadding.left, fftAxisPadding.top);
  fftContext.strokeStyle = "rgba(255, 255, 255, 0.08)";
  fftContext.fillStyle = "rgba(238, 247, 255, 0.78)";
  fftContext.lineWidth = 1;
  fftContext.font = "12px 'Segoe UI'";

  for (const frequency of xTicks) {
    const x = getFrequencyX(frequency, chartWidth, settings.scale, minFrequency, maxFrequency);
    if (x <= 2) {
      fftContext.textAlign = "left";
    } else if (x >= chartWidth - 2) {
      fftContext.textAlign = "right";
    } else {
      fftContext.textAlign = "center";
    }
    fftContext.beginPath();
    fftContext.moveTo(x, 0);
    fftContext.lineTo(x, chartHeight);
    fftContext.stroke();
    fftContext.fillText(formatFrequencyCompact(frequency), x, chartHeight + 18);
  }

  fftContext.textAlign = "left";
  if (rows.length > 0) {
    for (let i = 0; i < yTickCount; i += 1) {
      const rowIndex = rows.length === 1 ? 0 : Math.round((i / (yTickCount - 1)) * (rows.length - 1));
      const y = rows.length === 1 ? chartHeight * 0.5 : (rowIndex / (rows.length - 1)) * chartHeight;
      fftContext.beginPath();
      fftContext.moveTo(0, y);
      fftContext.lineTo(chartWidth, y);
      fftContext.stroke();
      fftContext.fillText(formatFrequencyCompact(rows[rowIndex].frequency), 8, y + 4);
    }
  } else {
    fftContext.beginPath();
    fftContext.moveTo(0, chartHeight * 0.5);
    fftContext.lineTo(chartWidth, chartHeight * 0.5);
    fftContext.stroke();
    fftContext.fillText("No sweep rows yet", 8, chartHeight * 0.5 + 4);
  }

  fftContext.strokeStyle = "rgba(255, 255, 255, 0.18)";
  fftContext.beginPath();
  fftContext.moveTo(0, 0);
  fftContext.lineTo(0, chartHeight);
  fftContext.lineTo(chartWidth, chartHeight);
  fftContext.stroke();

  fftContext.fillStyle = "rgba(238, 247, 255, 0.92)";
  fftContext.textAlign = "center";
  fftContext.fillText("Response frequency", chartWidth / 2, chartHeight + 32);

  fftContext.save();
  fftContext.translate(18, chartHeight / 2);
  fftContext.rotate(-Math.PI / 2);
  fftContext.fillText("Driven sweep frequency", 0, 0);
  fftContext.restore();

  fftContext.restore();
}

function drawFftHeatmap() {
  const { width, height } = fftCanvas;
  const settings = getFftSettings();
  const visibleRange = getVisibleFrequencyRange(settings.scale);
  const rows = getDisplayRows();
  const chartWidth = width - fftAxisPadding.left - fftAxisPadding.right;
  const chartHeight = height - fftAxisPadding.top - fftAxisPadding.bottom;
  const nyquist = getNyquist();

  fftContext.clearRect(0, 0, width, height);
  drawHeatmapAxes(chartWidth, chartHeight, settings, visibleRange.start, visibleRange.end, rows);

  if (rows.length === 0) {
    return;
  }

  const columnBins = new Uint32Array(chartWidth);
  for (let x = 0; x < chartWidth; x += 1) {
    const frequency = getFrequencyForX(x, chartWidth, settings.scale, visibleRange.start, visibleRange.end);
    const binIndex = Math.min(
      rows[0].spectrum.length - 1,
      Math.max(0, Math.floor((frequency / nyquist) * rows[0].spectrum.length))
    );
    columnBins[x] = binIndex;
  }

  const imageData = fftContext.createImageData(chartWidth, chartHeight);
  const pixels = imageData.data;

  for (let y = 0; y < chartHeight; y += 1) {
    const rowIndex = Math.min(rows.length - 1, Math.floor((y / chartHeight) * rows.length));
    const row = rows[rowIndex];

    for (let x = 0; x < chartWidth; x += 1) {
      const binIndex = columnBins[x];
      const dbValue = row.spectrum[binIndex];
      const normalized = (dbValue - settings.minDb) / (settings.maxDb - settings.minDb);
      const clamped = Math.min(1, Math.max(0, normalized));
      const color = heatmapPalette[Math.round(clamped * 255)];
      const pixelIndex = (y * chartWidth + x) * 4;

      pixels[pixelIndex] = color[0];
      pixels[pixelIndex + 1] = color[1];
      pixels[pixelIndex + 2] = color[2];
      pixels[pixelIndex + 3] = row.preview ? 180 : 255;
    }
  }

  fftContext.putImageData(imageData, fftAxisPadding.left, fftAxisPadding.top);
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

    sourceNode.connect(analyserNode);
    oscillatorNode.connect(gainNode);
    gainNode.connect(audioContext.destination);

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

fftSizeSelect.addEventListener("change", applyFftSettings);
smoothingInput.addEventListener("input", applyFftSettings);
minDbInput.addEventListener("blur", commitDbInputs);
minDbInput.addEventListener("change", commitDbInputs);
maxDbInput.addEventListener("blur", commitDbInputs);
maxDbInput.addEventListener("change", commitDbInputs);

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
updateControls();
setActiveView(activeView);
drawWaveformGrid(waveformCanvas.width, waveformCanvas.height);
drawFftHeatmap();
