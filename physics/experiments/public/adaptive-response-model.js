(function attachAdaptiveResponseModel(global) {
  const defaultMeasurementTolerance = 1e-6;
  const defaultPeakOffsetLimitHz = 5;

  function clampNumber(value, min, max, fallback) {
    const numericValue = Number(value);
    if (!Number.isFinite(numericValue)) {
      return fallback;
    }
    return Math.min(max, Math.max(min, numericValue));
  }

  function createRunningStat() {
    return { count: 0, mean: 0, m2: 0 };
  }

  function updateRunningStat(stat, value) {
    stat.count += 1;
    const delta = value - stat.mean;
    stat.mean += delta / stat.count;
    const delta2 = value - stat.mean;
    stat.m2 += delta * delta2;
  }

  function getRunningStd(stat) {
    return stat.count > 1 ? Math.sqrt(stat.m2 / (stat.count - 1)) : 0;
  }

  function createAdaptivePoint(frequency, measurement) {
    const point = {
      frequency,
      visits: 0,
      amplitude: createRunningStat(),
      width: createRunningStat(),
      offset: createRunningStat(),
    };

    updateAdaptivePoint(point, measurement);
    return point;
  }

  function updateAdaptivePoint(point, measurement) {
    updateRunningStat(point.amplitude, measurement.amplitudeDb);
    updateRunningStat(point.width, measurement.widthHz);
    updateRunningStat(point.offset, measurement.peakOffsetHz);
    point.visits += 1;
  }

  function pointToRow(point) {
    return {
      frequency: point.frequency,
      visits: point.visits,
      amplitudeMeanDb: point.amplitude.mean,
      amplitudeStdDb: getRunningStd(point.amplitude),
      widthMeanHz: point.width.mean,
      widthStdHz: getRunningStd(point.width),
      offsetMeanHz: point.offset.mean,
      offsetStdHz: getRunningStd(point.offset),
    };
  }

  function measurementToRow(frequency, measurement, preview = false) {
    return {
      frequency,
      visits: 1,
      amplitudeMeanDb: measurement.amplitudeDb,
      amplitudeStdDb: 0,
      widthMeanHz: measurement.widthHz,
      widthStdHz: 0,
      offsetMeanHz: measurement.peakOffsetHz,
      offsetStdHz: 0,
      preview,
    };
  }

  function findPointIndex(points, frequency, measurementTolerance) {
    let low = 0;
    let high = points.length - 1;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      const difference = points[mid].frequency - frequency;

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

  function upsertAdaptiveMeasurement(points, frequency, measurement, measurementTolerance) {
    const search = findPointIndex(points, frequency, measurementTolerance);

    if (!search.found) {
      points.splice(search.index, 0, createAdaptivePoint(frequency, measurement));
      return { inserted: true, point: points[search.index] };
    }

    const point = points[search.index];
    updateAdaptivePoint(point, measurement);
    return { inserted: false, point };
  }

  function getAdaptiveMidpoint(leftFrequency, rightFrequency) {
    return (leftFrequency + rightFrequency) * 0.5;
  }

  function beginExploreSeason(state) {
    state.phase = "explore";
    state.explorePointsDone = 0;
  }

  function beginRefineSeason(state) {
    state.phase = "refine";
    state.refineVisitsDone = 0;
  }

  function getExploreIntervalScore(leftPoint, rightPoint, settings, measurementTolerance) {
    const intervalWidth = Math.max(measurementTolerance, rightPoint.frequency - leftPoint.frequency);
    const normalizedWidth = intervalWidth / Math.max(measurementTolerance, settings.endHz - settings.startHz);
    const widthBonus = Math.sqrt(normalizedWidth);
    const amplitudeGap = Math.abs(rightPoint.amplitude.mean - leftPoint.amplitude.mean);
    const uncertainty = getRunningStd(leftPoint.amplitude) + getRunningStd(rightPoint.amplitude);
    const interestingness = amplitudeGap * 2 + uncertainty * 6;
    return interestingness * widthBonus;
  }

  function selectExploreFrequency(state, settings, measurementTolerance) {
    if (state.explorePointsDone >= settings.explorePointsPerSeason && state.points.length > 1) {
      return null;
    }

    if (state.points.length === 0) {
      return settings.startHz;
    }

    if (state.points.length === 1) {
      return Math.abs(state.points[0].frequency - settings.startHz) <= measurementTolerance
        ? settings.endHz
        : settings.startHz;
    }

    let bestCandidate = null;

    for (let index = 0; index < state.points.length - 1; index += 1) {
      const leftPoint = state.points[index];
      const rightPoint = state.points[index + 1];
      const midpoint = getAdaptiveMidpoint(leftPoint.frequency, rightPoint.frequency);

      if (
        !Number.isFinite(midpoint) ||
        midpoint <= settings.startHz + measurementTolerance ||
        midpoint >= settings.endHz - measurementTolerance ||
        Math.abs(midpoint - leftPoint.frequency) <= measurementTolerance ||
        Math.abs(rightPoint.frequency - midpoint) <= measurementTolerance
      ) {
        continue;
      }

      const candidate = {
        frequency: midpoint,
        score: getExploreIntervalScore(leftPoint, rightPoint, settings, measurementTolerance),
      };

      if (!bestCandidate || candidate.score > bestCandidate.score + measurementTolerance) {
        bestCandidate = candidate;
      }
    }

    return bestCandidate ? bestCandidate.frequency : null;
  }

  function selectRefineFrequency(state, settings, analysisMinDb) {
    if (state.points.length === 0) {
      return null;
    }

    if (state.refineVisitsDone >= settings.refineVisitsPerSeason) {
      return null;
    }

    let bestPoint = null;
    let bestScore = Number.NEGATIVE_INFINITY;

    for (const point of state.points) {
      const amplitudeImportance = Math.max(0, point.amplitude.mean - analysisMinDb);
      const amplitudeStd = getRunningStd(point.amplitude);
      const widthStd = getRunningStd(point.width);
      const offsetStd = getRunningStd(point.offset);
      const visitPenalty = Math.sqrt(Math.max(1, point.visits));
      const score =
        (amplitudeImportance + amplitudeStd * 8 + widthStd * 0.08 + offsetStd * 2) / visitPenalty;

      if (score > bestScore) {
        bestScore = score;
        bestPoint = point;
      }
    }

    return bestPoint ? bestPoint.frequency : null;
  }

  function chooseNextAdaptiveFrequency(state, settings, analysisMinDb, measurementTolerance) {
    for (let guard = 0; guard < 4; guard += 1) {
      if (state.phase === "idle") {
        beginExploreSeason(state);
      }

      if (state.phase === "explore") {
        const frequency = selectExploreFrequency(state, settings, measurementTolerance);
        if (Number.isFinite(frequency)) {
          return frequency;
        }
        beginRefineSeason(state);
        continue;
      }

      if (state.phase === "refine") {
        const frequency = selectRefineFrequency(state, settings, analysisMinDb);
        if (Number.isFinite(frequency)) {
          return frequency;
        }
        beginExploreSeason(state);
      }
    }

    return null;
  }

  function findHalfPowerCrossing(spectrum, peakIndex, thresholdDb, resolutionHz, direction, measurementTolerance) {
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
        return (previousIndex + (currentIndex - previousIndex) * ratio) * resolutionHz;
      }

      previousIndex = currentIndex;
      previousValue = currentValue;
    }

    return Number.NaN;
  }

  function measureTrackedResponse({
    spectrum,
    drivenFrequency,
    sampleRate,
    peakOffsetLimitHz,
    measurementTolerance,
  }) {
    if (!spectrum || spectrum.length === 0 || !Number.isFinite(drivenFrequency) || !Number.isFinite(sampleRate)) {
      return null;
    }

    const resolutionHz = sampleRate / 2 / spectrum.length;
    const nearestIndex = Math.min(
      spectrum.length - 1,
      Math.max(0, Math.round(drivenFrequency / Math.max(resolutionHz, measurementTolerance)))
    );
    const searchRadiusBins = Math.max(
      1,
      Math.ceil(peakOffsetLimitHz / Math.max(resolutionHz, measurementTolerance))
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
      -peakOffsetLimitHz,
      peakOffsetLimitHz,
      0
    );
    const thresholdDb = amplitudeDb - 3;
    const leftCrossingHz = findHalfPowerCrossing(
      spectrum,
      peakIndex,
      thresholdDb,
      resolutionHz,
      -1,
      measurementTolerance
    );
    const rightCrossingHz = findHalfPowerCrossing(
      spectrum,
      peakIndex,
      thresholdDb,
      resolutionHz,
      1,
      measurementTolerance
    );
    const widthHz =
      Number.isFinite(leftCrossingHz) && Number.isFinite(rightCrossingHz)
        ? Math.max(resolutionHz, rightCrossingHz - leftCrossingHz)
        : resolutionHz;

    return {
      amplitudeDb,
      widthHz,
      peakFrequencyHz: drivenFrequency + peakOffsetHz,
      peakOffsetHz,
    };
  }

  function createAdaptiveResponseModel(config = {}) {
    const measurementTolerance = config.measurementTolerance ?? defaultMeasurementTolerance;
    const peakOffsetLimitHz = config.peakOffsetLimitHz ?? defaultPeakOffsetLimitHz;

    const state = {
      points: [],
      liveMeasurement: null,
      activeTargetFrequency: 440,
      dwellStartTime: null,
      phase: "idle",
      explorePointsDone: 0,
      refineVisitsDone: 0,
    };

    function scheduleTarget(frequency, now) {
      state.activeTargetFrequency = frequency;
      state.dwellStartTime = Number.isFinite(now) ? now : null;
      state.liveMeasurement = null;
      return frequency;
    }

    function getCurrentPointRow() {
      const search = findPointIndex(state.points, state.activeTargetFrequency, measurementTolerance);
      return search.found ? pointToRow(state.points[search.index]) : null;
    }

    function getLastPointRow() {
      return state.points.length > 0 ? pointToRow(state.points[state.points.length - 1]) : null;
    }

    function getPhaseProgressLabel(settings) {
      if (state.phase === "explore") {
        return `explore ${state.explorePointsDone}/${settings.explorePointsPerSeason}`;
      }
      if (state.phase === "refine") {
        return `refine ${state.refineVisitsDone}/${settings.refineVisitsPerSeason}`;
      }
      return state.phase;
    }

    function getTotalVisitCount() {
      return state.points.reduce((total, point) => total + point.visits, 0);
    }

    function getPreviewRow({ isRunning, settled, currentStepFrameCount, previewMeasurement }) {
      if (!isRunning) {
        return null;
      }

      const search = findPointIndex(state.points, state.activeTargetFrequency, measurementTolerance);
      const committedTargetRow = search.found ? { ...pointToRow(state.points[search.index]), preview: true } : null;

      if (!settled || currentStepFrameCount === 0) {
        return state.phase === "refine" ? committedTargetRow : null;
      }

      if (!previewMeasurement) {
        return state.phase === "refine" ? committedTargetRow : null;
      }

      if (state.phase === "refine") {
        return measurementToRow(state.activeTargetFrequency, previewMeasurement, true);
      }

      return search.found ? null : measurementToRow(state.activeTargetFrequency, previewMeasurement, true);
    }

    function getDisplayedMeasurement({ isRunning, previewRow }) {
      if (previewRow) {
        return previewRow;
      }

      if (state.liveMeasurement) {
        return measurementToRow(state.activeTargetFrequency, state.liveMeasurement, false);
      }

      if (isRunning) {
        const currentPointRow = getCurrentPointRow();
        if (currentPointRow) {
          return currentPointRow;
        }
      }

      return getLastPointRow();
    }

    return {
      buildSnapshot({ settings, isRunning, previewMeasurement, currentStepFrameCount, settled, manualFrequency }) {
        const previewRow = getPreviewRow({
          isRunning,
          settled,
          currentStepFrameCount,
          previewMeasurement,
        });

        return {
          committedRows: state.points.map(pointToRow),
          previewRow,
          displayedMeasurement: getDisplayedMeasurement({ isRunning, previewRow }),
          pointCount: state.points.length,
          totalVisitCount: getTotalVisitCount(),
          exportRowCount: state.points.length,
          activeTargetFrequency: isRunning ? state.activeTargetFrequency : manualFrequency,
          phaseLabel: isRunning ? getPhaseProgressLabel(settings) : "manual",
        };
      },

      clear({ manualFrequency } = {}) {
        state.points = [];
        state.liveMeasurement = null;
        state.phase = "idle";
        state.explorePointsDone = 0;
        state.refineVisitsDone = 0;
        state.dwellStartTime = null;
        if (Number.isFinite(manualFrequency)) {
          state.activeTargetFrequency = manualFrequency;
        }
      },

      commitMeasurement(measurement, { frequency }) {
        const result = upsertAdaptiveMeasurement(state.points, frequency, measurement, measurementTolerance);

        if (state.phase === "explore" && result.inserted) {
          state.explorePointsDone += 1;
        } else if (state.phase === "refine") {
          state.refineVisitsDone += 1;
        }

        state.liveMeasurement = null;
        return result;
      },

      chooseNextFrequency({ settings, analysisMinDb }) {
        return chooseNextAdaptiveFrequency(state, settings, analysisMinDb, measurementTolerance);
      },

      clearLiveMeasurement() {
        state.liveMeasurement = null;
      },

      getActiveTargetFrequency() {
        return state.activeTargetFrequency;
      },

      getCommittedRows() {
        return state.points.map(pointToRow);
      },

      getDwellStartTime() {
        return state.dwellStartTime;
      },

      getExportRows() {
        return state.points.map(pointToRow);
      },

      getPointCount() {
        return state.points.length;
      },

      getTotalVisitCount() {
        return getTotalVisitCount();
      },

      hasPoints() {
        return state.points.length > 0;
      },

      measureTrackedResponse({ spectrum, drivenFrequency, sampleRate }) {
        return measureTrackedResponse({
          spectrum,
          drivenFrequency,
          sampleRate,
          peakOffsetLimitHz,
          measurementTolerance,
        });
      },

      rescheduleCurrent(now) {
        state.dwellStartTime = Number.isFinite(now) ? now : null;
        state.liveMeasurement = null;
      },

      scheduleNext({ settings, analysisMinDb, now }) {
        const nextFrequency = chooseNextAdaptiveFrequency(state, settings, analysisMinDb, measurementTolerance);
        return Number.isFinite(nextFrequency) ? scheduleTarget(nextFrequency, now) : null;
      },

      scheduleTarget(frequency, now) {
        return scheduleTarget(frequency, now);
      },

      setActiveTargetFrequency(frequency) {
        state.activeTargetFrequency = frequency;
      },

      setLiveMeasurement(measurement) {
        state.liveMeasurement = measurement;
      },

      start({ settings, analysisMinDb, now, clearExisting = true, manualFrequency }) {
        if (clearExisting) {
          state.points = [];
          state.phase = "idle";
          state.explorePointsDone = 0;
          state.refineVisitsDone = 0;
        }

        if (Number.isFinite(manualFrequency)) {
          state.activeTargetFrequency = manualFrequency;
        }

        const nextFrequency = chooseNextAdaptiveFrequency(state, settings, analysisMinDb, measurementTolerance);
        return Number.isFinite(nextFrequency) ? scheduleTarget(nextFrequency, now) : null;
      },

      stop({ manualFrequency } = {}) {
        state.dwellStartTime = null;
        state.phase = "idle";
        state.liveMeasurement = null;
        if (Number.isFinite(manualFrequency)) {
          state.activeTargetFrequency = manualFrequency;
        }
      },
    };
  }

  global.AdaptiveResponseModel = {
    createAdaptiveResponseModel,
  };
})(window);
