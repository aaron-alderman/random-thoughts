(function () {
  function clampNumber(value, min, max, fallback) {
    if (!Number.isFinite(value)) {
      return fallback;
    }

    return Math.min(max, Math.max(min, value));
  }

  function formatNumber(value, digits) {
    return Number(value.toFixed(digits)).toString();
  }

  function formatFrequencyCompact(value) {
    if (value >= 1000) {
      return value >= 10000 ? `${formatNumber(value / 1000, 0)} kHz` : `${formatNumber(value / 1000, 1)} kHz`;
    }

    return value % 1 === 0 ? `${formatNumber(value, 0)} Hz` : `${formatNumber(value, 1)} Hz`;
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

  function createSettingsPersister(storageKey, collectSettings, delayMs) {
    let timerId = null;

    function persistNow() {
      if (timerId !== null) {
        window.clearTimeout(timerId);
        timerId = null;
      }

      try {
        window.localStorage.setItem(storageKey, JSON.stringify(collectSettings()));
      } catch (error) {
        console.warn("Unable to save settings", error);
      }
    }

    function persist() {
      if (timerId !== null) {
        window.clearTimeout(timerId);
      }

      timerId = window.setTimeout(persistNow, delayMs);
    }

    persist.flush = persistNow;
    return persist;
  }

  function findRowIndex(rows, frequency, tolerance) {
    let low = 0;
    let high = rows.length - 1;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      const difference = rows[mid].frequency - frequency;

      if (Math.abs(difference) <= tolerance) {
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

  function upsertHeatmapRow(rows, frequency, spectrum, visitCount, tolerance) {
    const search = findRowIndex(rows, frequency, tolerance);

    if (!search.found) {
      rows.splice(search.index, 0, {
        frequency,
        spectrum: spectrum.slice(),
        visits: visitCount,
      });
      return;
    }

    const existingRow = rows[search.index];
    const nextVisits = existingRow.visits + visitCount;
    for (let i = 0; i < existingRow.spectrum.length; i += 1) {
      existingRow.spectrum[i] =
        existingRow.spectrum[i] + ((spectrum[i] - existingRow.spectrum[i]) * visitCount) / nextVisits;
    }
    existingRow.visits = nextVisits;
  }

  function buildDisplayRows(rows, previewRow, tolerance) {
    if (!previewRow) {
      return rows;
    }

    const search = findRowIndex(rows, previewRow.frequency, tolerance);
    const nextRows = rows.slice();

    if (search.found) {
      nextRows[search.index] = previewRow;
      return nextRows;
    }

    nextRows.splice(search.index, 0, previewRow);
    return nextRows;
  }

  function buildColumnBackground(rows, percentile, minDb) {
    if (rows.length < 2) {
      return null;
    }

    const background = new Float32Array(rows[0].spectrum.length);
    for (let binIndex = 0; binIndex < background.length; binIndex += 1) {
      const values = new Array(rows.length);
      for (let rowIndex = 0; rowIndex < rows.length; rowIndex += 1) {
        values[rowIndex] = rows[rowIndex].spectrum[binIndex];
      }

      values.sort((left, right) => left - right);
      const baseline = computePercentile(values, percentile);
      background[binIndex] = Number.isFinite(baseline) ? baseline : minDb;
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

  function getHeatmapLayout(width, height, axisPadding, marginalLayout) {
    const plotWidth = Math.max(160, width - axisPadding.left - axisPadding.right);
    const plotHeight = Math.max(120, height - axisPadding.top - axisPadding.bottom);
    const heatmapWidth = Math.max(80, plotWidth - marginalLayout.rightWidth - marginalLayout.gap);
    const heatmapHeight = Math.max(80, plotHeight - marginalLayout.topHeight - marginalLayout.gap);

    return {
      heatmapX: axisPadding.left,
      heatmapY: axisPadding.top + marginalLayout.topHeight + marginalLayout.gap,
      heatmapWidth,
      heatmapHeight,
      topX: axisPadding.left,
      topY: axisPadding.top,
      topWidth: heatmapWidth,
      topHeight: marginalLayout.topHeight,
      rightX: axisPadding.left + heatmapWidth + marginalLayout.gap,
      rightY: axisPadding.top + marginalLayout.topHeight + marginalLayout.gap,
      rightWidth: marginalLayout.rightWidth,
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

  function buildHeatmapRowGeometry(rows, chartHeight, getRowY) {
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
      centers[rowIndex] = getRowY(rows[rowIndex].frequency, chartHeight);
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

  function buildHeatmapMarginals(renderedRows, columnBins) {
    const binCount = renderedRows.length > 0 ? renderedRows[0].renderedSpectrum.length : 0;
    const columnTotals = new Float32Array(binCount);
    const rowTotals = new Float32Array(renderedRows.length);

    for (let rowIndex = 0; rowIndex < renderedRows.length; rowIndex += 1) {
      const row = renderedRows[rowIndex];
      let rowTotal = 0;

      for (let binIndex = 0; binIndex < row.renderedSpectrum.length; binIndex += 1) {
        const dbValue = row.renderedSpectrum[binIndex];
        columnTotals[binIndex] += 10 ** (dbValue / 10);
      }

      for (let x = 0; x < columnBins.length; x += 1) {
        rowTotal += 10 ** (row.renderedSpectrum[columnBins[x]] / 10);
      }

      rowTotals[rowIndex] = rowTotal;
    }

    return { columnTotals, rowTotals };
  }

  function getMaxArrayValue(values, fallback) {
    let maxValue = fallback;

    for (let index = 0; index < values.length; index += 1) {
      if (values[index] > maxValue) {
        maxValue = values[index];
      }
    }

    return maxValue;
  }

  function drawHeatmapAxes(options) {
    const {
      ctx,
      layout,
      settings,
      minFrequency,
      maxFrequency,
      rows,
      rowGeometry,
      formatYAxisLabel,
      yAxisTitle,
      emptyLabel,
    } = options;
    const xTicks = getFrequencyTickValues(settings.scale, minFrequency, maxFrequency);
    const yTickCount = Math.min(6, Math.max(rows.length, 2));
    const yLabelX = -10;

    ctx.save();
    ctx.translate(layout.heatmapX, layout.heatmapY);
    ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
    ctx.fillStyle = "rgba(238, 247, 255, 0.78)";
    ctx.lineWidth = 1;
    ctx.font = "12px 'Segoe UI'";

    for (const frequency of xTicks) {
      const x = getFrequencyX(frequency, layout.heatmapWidth, settings.scale, minFrequency, maxFrequency);
      if (x <= 2) {
        ctx.textAlign = "left";
      } else if (x >= layout.heatmapWidth - 2) {
        ctx.textAlign = "right";
      } else {
        ctx.textAlign = "center";
      }
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, layout.heatmapHeight);
      ctx.stroke();
      ctx.fillText(formatFrequencyCompact(frequency), x, layout.heatmapHeight + 18);
    }

    ctx.textAlign = "right";
    if (rows.length > 0) {
      for (let i = 0; i < yTickCount; i += 1) {
        const rowIndex = rows.length === 1 ? 0 : Math.round((i / (yTickCount - 1)) * (rows.length - 1));
        const y = rowGeometry.centers[rowIndex];
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(layout.heatmapWidth, y);
        ctx.stroke();
        ctx.fillText(formatYAxisLabel(rows[rowIndex].frequency), yLabelX, y + 4);
      }
    } else {
      ctx.beginPath();
      ctx.moveTo(0, layout.heatmapHeight * 0.5);
      ctx.lineTo(layout.heatmapWidth, layout.heatmapHeight * 0.5);
      ctx.stroke();
      ctx.fillText(emptyLabel, yLabelX, layout.heatmapHeight * 0.5 + 4);
    }

    ctx.strokeStyle = "rgba(255, 255, 255, 0.18)";
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, layout.heatmapHeight);
    ctx.lineTo(layout.heatmapWidth, layout.heatmapHeight);
    ctx.stroke();

    ctx.fillStyle = "rgba(238, 247, 255, 0.92)";
    ctx.textAlign = "center";
    ctx.fillText("Response frequency", layout.heatmapWidth / 2, layout.heatmapHeight + 32);

    ctx.save();
    ctx.translate(18, layout.heatmapHeight / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText(yAxisTitle, 0, 0);
    ctx.restore();

    ctx.restore();
  }

  function drawTopMarginal(options) {
    const { ctx, layout, columnTotals, settings, minFrequency, maxFrequency, nyquist } = options;

    ctx.save();
    ctx.translate(layout.topX, layout.topY);
    ctx.strokeStyle = "rgba(255, 255, 255, 0.14)";
    ctx.fillStyle = "rgba(255, 255, 255, 0.03)";
    ctx.lineWidth = 1;
    ctx.font = "12px 'Segoe UI'";
    ctx.fillRect(0, 0, layout.topWidth, layout.topHeight);
    ctx.strokeRect(0, 0, layout.topWidth, layout.topHeight);
    ctx.fillStyle = "rgba(238, 247, 255, 0.72)";
    ctx.textAlign = "left";
    ctx.fillText("Column cumulative", 10, 14);

    if (columnTotals.length > 0) {
      const maxTotal = getMaxArrayValue(columnTotals, 1e-12);
      const chartTop = 22;
      const chartBottom = layout.topHeight - 6;
      const chartRange = Math.max(1, chartBottom - chartTop);
      const binWidthHz = nyquist / columnTotals.length;
      let started = false;

      ctx.fillStyle = "rgba(110, 231, 255, 0.18)";
      ctx.strokeStyle = "rgba(110, 231, 255, 0.92)";
      ctx.beginPath();
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
          ctx.moveTo(leftX, chartBottom);
          ctx.lineTo(leftX, y);
          started = true;
        } else {
          ctx.lineTo(leftX, y);
        }

        ctx.lineTo(rightX, y);
      }

      if (started) {
        ctx.lineTo(layout.topWidth, chartBottom);
        ctx.closePath();
        ctx.fill();
      }

      ctx.beginPath();
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
          ctx.moveTo(leftX, y);
          started = true;
        } else {
          ctx.lineTo(leftX, y);
        }
        ctx.lineTo(rightX, y);
      }

      if (started) {
        ctx.stroke();
      }
    }

    ctx.restore();
  }

  function drawRightMarginal(options) {
    const { ctx, layout, rowTotals, rowGeometry } = options;

    ctx.save();
    ctx.translate(layout.rightX, layout.rightY);
    ctx.strokeStyle = "rgba(255, 255, 255, 0.14)";
    ctx.fillStyle = "rgba(255, 255, 255, 0.03)";
    ctx.lineWidth = 1;
    ctx.font = "12px 'Segoe UI'";
    ctx.fillRect(0, 0, layout.rightWidth, layout.rightHeight);
    ctx.strokeRect(0, 0, layout.rightWidth, layout.rightHeight);

    ctx.save();
    ctx.translate(layout.rightWidth - 14, layout.rightHeight / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillStyle = "rgba(238, 247, 255, 0.72)";
    ctx.textAlign = "center";
    ctx.fillText("Row cumulative", 0, 0);
    ctx.restore();

    if (rowTotals.length > 0) {
      const maxTotal = getMaxArrayValue(rowTotals, 1e-12);
      const chartWidth = layout.rightWidth - 12;

      ctx.fillStyle = "rgba(255, 111, 145, 0.18)";
      ctx.strokeStyle = "rgba(255, 111, 145, 0.92)";
      ctx.beginPath();
      ctx.moveTo(0, 0);

      for (let rowIndex = 0; rowIndex < rowTotals.length; rowIndex += 1) {
        const y = rowGeometry.centers[rowIndex];
        const x = (rowTotals[rowIndex] / maxTotal) * chartWidth;
        ctx.lineTo(x, y);
      }

      ctx.lineTo(0, layout.rightHeight);
      ctx.closePath();
      ctx.fill();

      ctx.beginPath();
      for (let rowIndex = 0; rowIndex < rowTotals.length; rowIndex += 1) {
        const y = rowGeometry.centers[rowIndex];
        const x = (rowTotals[rowIndex] / maxTotal) * chartWidth;
        if (rowIndex === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      ctx.stroke();
    }

    ctx.restore();
  }

  function getOrBuildColumnBins(cache, options) {
    const { width, binCount, scale, minFrequency, maxFrequency, nyquist } = options;
    const key = `${width}|${binCount}|${scale}|${minFrequency}|${maxFrequency}|${nyquist}`;

    if (cache.key === key && cache.value) {
      return cache.value;
    }

    const columnBins = new Uint32Array(width);
    for (let x = 0; x < width; x += 1) {
      const frequency = getFrequencyForX(x, width, scale, minFrequency, maxFrequency);
      columnBins[x] = Math.min(binCount - 1, Math.max(0, Math.floor((frequency / nyquist) * binCount)));
    }

    cache.key = key;
    cache.value = columnBins;
    return columnBins;
  }

  window.FftHeatmapCommon = {
    buildColumnBackground,
    buildDisplayRows,
    buildHeatmapMarginals,
    buildHeatmapPalette,
    buildHeatmapRowGeometry,
    clampNumber,
    computePercentile,
    createSettingsPersister,
    drawHeatmapAxes,
    drawRightMarginal,
    drawTopMarginal,
    formatBalanceLabel,
    formatFrequencyCompact,
    formatNumber,
    getFrequencyForX,
    getFrequencyTickValues,
    getFrequencyX,
    getHeatmapLayout,
    getOrBuildColumnBins,
    subtractColumnBackground,
    upsertHeatmapRow,
  };
})();
