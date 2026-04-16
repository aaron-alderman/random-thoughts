(function attachAdaptiveResponseUi(global) {
  const { clampNumber, formatBalanceLabel, formatFrequencyCompact, formatNumber } = global.FftHeatmapCommon;
  const {
    drawMetricChart,
    drawWaveform,
    drawWaveformGrid,
    formatDb,
    formatHertz,
    formatOffset,
    getMetricRange,
  } = global.ResponseExperimentUiCommon;

  function createAdaptiveResponseUi(config = {}) {
    const measurementTolerance = config.measurementTolerance ?? 1e-6;
    const trackedPeakOffsetLimitHz = config.trackedPeakOffsetLimitHz ?? 5;
    const responseChartPadding = config.responseChartPadding ?? { top: 18, right: 18, bottom: 42, left: 84 };

    const elements = {
      startButton: document.getElementById("startButton"),
      stopButton: document.getElementById("stopButton"),
      resetResponseButton: document.getElementById("resetResponseButton"),
      toneEnabled: document.getElementById("toneEnabled"),
      frequencyInput: document.getElementById("frequencyInput"),
      amplitudeInput: document.getElementById("amplitudeInput"),
      amplitudeValue: document.getElementById("amplitudeValue"),
      balanceInput: document.getElementById("balanceInput"),
      balanceValue: document.getElementById("balanceValue"),
      statusText: document.getElementById("statusText"),
      waveformTab: document.getElementById("waveformTab"),
      responseTab: document.getElementById("responseTab"),
      waveformView: document.getElementById("waveformView"),
      responseView: document.getElementById("responseView"),
      waveformCanvas: document.getElementById("waveformCanvas"),
      amplitudeChartCanvas: document.getElementById("amplitudeChartCanvas"),
      widthChartCanvas: document.getElementById("widthChartCanvas"),
      offsetChartCanvas: document.getElementById("offsetChartCanvas"),
      fftSizeSelect: document.getElementById("fftSizeSelect"),
      smoothingInput: document.getElementById("smoothingInput"),
      smoothingValue: document.getElementById("smoothingValue"),
      minDbInput: document.getElementById("minDbInput"),
      maxDbInput: document.getElementById("maxDbInput"),
      adaptiveSweepEnabledInput: document.getElementById("adaptiveSweepEnabledInput"),
      sweepStartHzInput: document.getElementById("sweepStartHzInput"),
      sweepEndHzInput: document.getElementById("sweepEndHzInput"),
      explorePointsInput: document.getElementById("explorePointsInput"),
      sweepLogInput: document.getElementById("sweepLogInput"),
      refineVisitsInput: document.getElementById("refineVisitsInput"),
      sweepStepSecondsInput: document.getElementById("sweepStepSecondsInput"),
      sweepSettleSecondsInput: document.getElementById("sweepSettleSecondsInput"),
      restartSweepButton: document.getElementById("restartSweepButton"),
      exportCsvButton: document.getElementById("exportCsvButton"),
      adaptiveCurrentFrequency: document.getElementById("adaptiveCurrentFrequency"),
      adaptivePhaseValue: document.getElementById("adaptivePhaseValue"),
      sweepStepProgress: document.getElementById("sweepStepProgress"),
      adaptivePointCount: document.getElementById("adaptivePointCount"),
      adaptiveVisitCount: document.getElementById("adaptiveVisitCount"),
      fftResolution: document.getElementById("fftResolution"),
      trackedAmplitudeValue: document.getElementById("trackedAmplitudeValue"),
      trackedWidthValue: document.getElementById("trackedWidthValue"),
      trackedOffsetValue: document.getElementById("trackedOffsetValue"),
      fftAverageCount: document.getElementById("fftAverageCount"),
      exportStatusValue: document.getElementById("exportStatusValue"),
    };

    const waveformContext = elements.waveformCanvas.getContext("2d");
    const amplitudeChartContext = elements.amplitudeChartCanvas.getContext("2d");
    const widthChartContext = elements.widthChartCanvas.getContext("2d");
    const offsetChartContext = elements.offsetChartCanvas.getContext("2d");

    let activeView = "response";

    function setStatus(text) {
      elements.statusText.textContent = text;
    }

    function setAudioButtonState({ startDisabled, stopDisabled }) {
      elements.startButton.disabled = Boolean(startDisabled);
      elements.stopButton.disabled = Boolean(stopDisabled);
    }

    function getActiveView() {
      return activeView;
    }

    function setActiveView(view) {
      activeView = view === "waveform" ? "waveform" : "response";
      const showWaveform = activeView === "waveform";

      elements.waveformTab.classList.toggle("active", showWaveform);
      elements.waveformTab.setAttribute("aria-selected", String(showWaveform));
      elements.waveformView.classList.toggle("active", showWaveform);
      elements.waveformView.hidden = !showWaveform;

      elements.responseTab.classList.toggle("active", !showWaveform);
      elements.responseTab.setAttribute("aria-selected", String(!showWaveform));
      elements.responseView.classList.toggle("active", !showWaveform);
      elements.responseView.hidden = showWaveform;
    }

    function collectSettings() {
      return {
        activeView,
        toneEnabled: elements.toneEnabled.checked,
        frequencyInput: elements.frequencyInput.value,
        amplitudeInput: elements.amplitudeInput.value,
        balanceInput: elements.balanceInput.value,
        fftSizeSelect: elements.fftSizeSelect.value,
        smoothingInput: elements.smoothingInput.value,
        minDbInput: elements.minDbInput.value,
        maxDbInput: elements.maxDbInput.value,
        adaptiveSweepEnabledInput: elements.adaptiveSweepEnabledInput.checked,
        sweepStartHzInput: elements.sweepStartHzInput.value,
        sweepEndHzInput: elements.sweepEndHzInput.value,
        explorePointsInput: elements.explorePointsInput.value,
        sweepLogInput: elements.sweepLogInput.checked,
        refineVisitsInput: elements.refineVisitsInput.value,
        sweepStepSecondsInput: elements.sweepStepSecondsInput.value,
        sweepSettleSecondsInput: elements.sweepSettleSecondsInput.value,
      };
    }

    function loadSettings(settings) {
      if (!settings || typeof settings !== "object") {
        return;
      }

      if (typeof settings.activeView === "string") activeView = settings.activeView;
      if (typeof settings.toneEnabled === "boolean") elements.toneEnabled.checked = settings.toneEnabled;
      if (typeof settings.frequencyInput === "string") elements.frequencyInput.value = settings.frequencyInput;
      if (typeof settings.amplitudeInput === "string") elements.amplitudeInput.value = settings.amplitudeInput;
      if (typeof settings.balanceInput === "string") elements.balanceInput.value = settings.balanceInput;
      if (typeof settings.fftSizeSelect === "string") elements.fftSizeSelect.value = settings.fftSizeSelect;
      if (typeof settings.smoothingInput === "string") elements.smoothingInput.value = settings.smoothingInput;
      if (typeof settings.minDbInput === "string") elements.minDbInput.value = settings.minDbInput;
      if (typeof settings.maxDbInput === "string") elements.maxDbInput.value = settings.maxDbInput;
      if (typeof settings.adaptiveSweepEnabledInput === "boolean") {
        elements.adaptiveSweepEnabledInput.checked = settings.adaptiveSweepEnabledInput;
      }
      if (typeof settings.sweepStartHzInput === "string") elements.sweepStartHzInput.value = settings.sweepStartHzInput;
      if (typeof settings.sweepEndHzInput === "string") elements.sweepEndHzInput.value = settings.sweepEndHzInput;
      if (typeof settings.explorePointsInput === "string") elements.explorePointsInput.value = settings.explorePointsInput;
      if (typeof settings.sweepLogInput === "boolean") elements.sweepLogInput.checked = settings.sweepLogInput;
      if (typeof settings.refineVisitsInput === "string") elements.refineVisitsInput.value = settings.refineVisitsInput;
      if (typeof settings.sweepStepSecondsInput === "string") {
        elements.sweepStepSecondsInput.value = settings.sweepStepSecondsInput;
      }
      if (typeof settings.sweepSettleSecondsInput === "string") {
        elements.sweepSettleSecondsInput.value = settings.sweepSettleSecondsInput;
      }
    }

    function renderControls({
      analysisSettings,
      adaptiveSettings,
      snapshot,
      sampleRate,
      currentStepFrameCount,
      isRunning,
      elapsedSeconds,
    }) {
      const displayedMeasurement = snapshot.displayedMeasurement;

      elements.amplitudeValue.textContent = `${elements.amplitudeInput.value}%`;
      elements.balanceValue.textContent = formatBalanceLabel(
        clampNumber(Number(elements.balanceInput.value), -100, 100, 0)
      );
      elements.smoothingValue.textContent = analysisSettings.smoothing.toFixed(2);
      elements.fftResolution.textContent = `${(sampleRate / analysisSettings.fftSize).toFixed(1)} Hz/bin`;
      elements.trackedAmplitudeValue.textContent = displayedMeasurement
        ? formatDb(displayedMeasurement.amplitudeMeanDb)
        : "n/a";
      elements.trackedWidthValue.textContent = displayedMeasurement
        ? formatHertz(displayedMeasurement.widthMeanHz)
        : "n/a";
      elements.trackedOffsetValue.textContent = displayedMeasurement
        ? formatOffset(displayedMeasurement.offsetMeanHz)
        : "n/a";
      elements.fftAverageCount.textContent = `${currentStepFrameCount} frame${currentStepFrameCount === 1 ? "" : "s"}`;
      elements.exportStatusValue.textContent = `${snapshot.exportRowCount} row${snapshot.exportRowCount === 1 ? "" : "s"}`;
      elements.adaptivePointCount.textContent = `${snapshot.pointCount} point${snapshot.pointCount === 1 ? "" : "s"}`;
      elements.adaptiveVisitCount.textContent = `${snapshot.totalVisitCount} visit${snapshot.totalVisitCount === 1 ? "" : "s"}`;
      elements.exportCsvButton.disabled = snapshot.pointCount === 0;
      elements.adaptiveCurrentFrequency.textContent = formatFrequencyCompact(snapshot.activeTargetFrequency);
      elements.adaptivePhaseValue.textContent = snapshot.phaseLabel;

      if (isRunning) {
        elements.sweepStepProgress.textContent = `${elapsedSeconds.toFixed(1)} / ${adaptiveSettings.stepSeconds.toFixed(
          1
        )} s (${elapsedSeconds >= adaptiveSettings.settleSeconds ? "collect" : "settle"})`;
      } else {
        elements.sweepStepProgress.textContent = `${elapsedSeconds.toFixed(1)} / ${adaptiveSettings.stepSeconds.toFixed(
          1
        )} s`;
      }
    }

    function drawResponseCharts({ snapshot, analysisSettings, adaptiveSettings, sampleRate }) {
      const rows = snapshot.committedRows;
      const previewRow = snapshot.previewRow;
      const resolutionHz = sampleRate / analysisSettings.fftSize;

      drawMetricChart({
        canvas: elements.amplitudeChartCanvas,
        context: amplitudeChartContext,
        rows,
        previewRow,
        xAxis: adaptiveSettings,
        padding: responseChartPadding,
        series: { meanKey: "amplitudeMeanDb", stdKey: "amplitudeStdDb" },
        styles: {
          strokeStyle: "#6ee7ff",
          bandFillStyle: "rgba(110, 231, 255, 0.16)",
          previewFillStyle: "rgba(110, 231, 255, 0.5)",
        },
        yAxisLabel: "Matched amplitude",
        formatValue: formatDb,
        range: getMetricRange(rows, {
          meanKey: "amplitudeMeanDb",
          stdKey: "amplitudeStdDb",
          fallbackMin: analysisSettings.minDb,
          fallbackMax: analysisSettings.maxDb,
          previewRow,
          measurementTolerance,
        }),
        emptyLabel: "No committed points yet",
      });

      drawMetricChart({
        canvas: elements.widthChartCanvas,
        context: widthChartContext,
        rows,
        previewRow,
        xAxis: adaptiveSettings,
        padding: responseChartPadding,
        series: { meanKey: "widthMeanHz", stdKey: "widthStdHz" },
        styles: {
          strokeStyle: "#ff6f91",
          bandFillStyle: "rgba(255, 111, 145, 0.16)",
          previewFillStyle: "rgba(255, 111, 145, 0.5)",
        },
        yAxisLabel: "FWHM width",
        formatValue: formatHertz,
        range: getMetricRange(rows, {
          meanKey: "widthMeanHz",
          stdKey: "widthStdHz",
          fallbackMin: 0,
          fallbackMax: Math.max(50, resolutionHz * 6),
          includeZero: true,
          previewRow,
          measurementTolerance,
        }),
        emptyLabel: "No committed points yet",
      });

      drawMetricChart({
        canvas: elements.offsetChartCanvas,
        context: offsetChartContext,
        rows,
        previewRow,
        xAxis: adaptiveSettings,
        padding: responseChartPadding,
        series: { meanKey: "offsetMeanHz", stdKey: "offsetStdHz" },
        styles: {
          strokeStyle: "#f7d06f",
          bandFillStyle: "rgba(247, 208, 111, 0.16)",
          previewFillStyle: "rgba(247, 208, 111, 0.5)",
        },
        yAxisLabel: "Peak offset",
        formatValue: formatOffset,
        range: getMetricRange(rows, {
          meanKey: "offsetMeanHz",
          stdKey: "offsetStdHz",
          fallbackMin: -trackedPeakOffsetLimitHz,
          fallbackMax: trackedPeakOffsetLimitHz,
          includeZero: true,
          previewRow,
          measurementTolerance,
        }),
        emptyLabel: "No committed points yet",
      });
    }

    function clearPlots() {
      waveformContext.clearRect(0, 0, elements.waveformCanvas.width, elements.waveformCanvas.height);
      amplitudeChartContext.clearRect(0, 0, elements.amplitudeChartCanvas.width, elements.amplitudeChartCanvas.height);
      widthChartContext.clearRect(0, 0, elements.widthChartCanvas.width, elements.widthChartCanvas.height);
      offsetChartContext.clearRect(0, 0, elements.offsetChartCanvas.width, elements.offsetChartCanvas.height);
    }

    return {
      elements,
      clearPlots,
      collectSettings,
      drawResponseCharts,
      drawWaveform: (waveformData) => drawWaveform(elements.waveformCanvas, waveformContext, waveformData),
      drawWaveformGrid: (width, height) => drawWaveformGrid(waveformContext, width, height),
      getActiveView,
      loadSettings,
      renderControls,
      setActiveView,
      setAudioButtonState,
      setStatus,
    };
  }

  global.AdaptiveResponseUi = {
    createAdaptiveResponseUi,
  };
})(window);
