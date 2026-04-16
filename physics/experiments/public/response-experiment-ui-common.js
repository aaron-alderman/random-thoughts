(function attachResponseExperimentUiCommon(global) {
  const {
    formatFrequencyCompact,
    formatNumber,
    getFrequencyTickValues,
    getFrequencyX,
  } = global.FftHeatmapCommon;

  function formatDb(value) {
    return Number.isFinite(value) ? `${value.toFixed(1)} dB` : "n/a";
  }

  function formatHertz(value) {
    if (!Number.isFinite(value)) {
      return "n/a";
    }

    if (value >= 1000) {
      return formatFrequencyCompact(value);
    }

    return `${formatNumber(value, value >= 100 ? 0 : 1)} Hz`;
  }

  function formatOffset(value) {
    if (!Number.isFinite(value)) {
      return "n/a";
    }

    if (Math.abs(value) < 0.05) {
      return "0 Hz";
    }

    return `${value > 0 ? "+" : ""}${formatHertz(Math.abs(value))}`;
  }

  function drawWaveformGrid(context, width, height) {
    context.save();
    context.strokeStyle = "rgba(255, 255, 255, 0.08)";
    context.lineWidth = 1;

    for (let index = 1; index < 6; index += 1) {
      const y = (height / 6) * index;
      context.beginPath();
      context.moveTo(0, y);
      context.lineTo(width, y);
      context.stroke();
    }

    for (let index = 1; index < 8; index += 1) {
      const x = (width / 8) * index;
      context.beginPath();
      context.moveTo(x, 0);
      context.lineTo(x, height);
      context.stroke();
    }

    context.restore();
  }

  function drawWaveform(canvas, context, waveformData) {
    const { width, height } = canvas;
    context.clearRect(0, 0, width, height);
    drawWaveformGrid(context, width, height);

    context.strokeStyle = "#6ee7ff";
    context.lineWidth = 2;
    context.beginPath();

    for (let index = 0; index < waveformData.length; index += 1) {
      const x = (index / (waveformData.length - 1)) * width;
      const y = height * 0.5 - waveformData[index] * height * 0.42;
      if (index === 0) {
        context.moveTo(x, y);
      } else {
        context.lineTo(x, y);
      }
    }

    context.stroke();
  }

  function getMetricRange(rows, options) {
    const {
      meanKey,
      stdKey,
      fallbackMin,
      fallbackMax,
      includeZero = false,
      measurementTolerance = 1e-6,
      previewRow = null,
    } = options;
    let minValue = Number.POSITIVE_INFINITY;
    let maxValue = Number.NEGATIVE_INFINITY;

    for (const row of rows) {
      const mean = row[meanKey];
      const std = stdKey ? row[stdKey] : 0;
      if (!Number.isFinite(mean)) {
        continue;
      }
      minValue = Math.min(minValue, mean - (Number.isFinite(std) ? std : 0));
      maxValue = Math.max(maxValue, mean + (Number.isFinite(std) ? std : 0));
    }

    if (previewRow && Number.isFinite(previewRow[meanKey])) {
      const previewStd = stdKey ? previewRow[stdKey] : 0;
      minValue = Math.min(minValue, previewRow[meanKey] - (Number.isFinite(previewStd) ? previewStd : 0));
      maxValue = Math.max(maxValue, previewRow[meanKey] + (Number.isFinite(previewStd) ? previewStd : 0));
    }

    if (!Number.isFinite(minValue) || !Number.isFinite(maxValue)) {
      minValue = fallbackMin;
      maxValue = fallbackMax;
    }

    if (includeZero) {
      minValue = Math.min(minValue, 0);
      maxValue = Math.max(maxValue, 0);
    }

    if (Math.abs(maxValue - minValue) < measurementTolerance) {
      const padding = Math.max(1, Math.abs(maxValue) * 0.1);
      minValue -= padding;
      maxValue += padding;
    } else {
      const padding = (maxValue - minValue) * 0.12;
      minValue -= padding;
      maxValue += padding;
    }

    return { min: minValue, max: maxValue };
  }

  function getChartY(value, height, range) {
    const span = range.max - range.min || 1;
    return height - ((value - range.min) / span) * height;
  }

  function drawMetricChart({
    canvas,
    context,
    rows,
    previewRow = null,
    xAxis,
    padding,
    series,
    styles,
    yAxisLabel,
    formatValue,
    range,
    emptyLabel = "No response points yet",
  }) {
    const { width, height } = canvas;
    const plotWidth = Math.max(120, width - padding.left - padding.right);
    const plotHeight = Math.max(120, height - padding.top - padding.bottom);
    const plotX = padding.left;
    const plotY = padding.top;
    const scale = xAxis.log ? "log" : "linear";
    const minFrequency = xAxis.log ? Math.max(20, xAxis.startHz) : xAxis.startHz;
    const maxFrequency = Math.max(minFrequency + 0.1, xAxis.endHz);
    const xTicks = getFrequencyTickValues(scale, minFrequency, maxFrequency);
    const useBand = Boolean(series.stdKey);

    context.clearRect(0, 0, width, height);
    context.save();
    context.fillStyle = "rgba(255, 255, 255, 0.03)";
    context.strokeStyle = "rgba(255, 255, 255, 0.12)";
    context.lineWidth = 1;
    context.fillRect(plotX, plotY, plotWidth, plotHeight);
    context.strokeRect(plotX, plotY, plotWidth, plotHeight);
    context.font = "12px 'Segoe UI'";

    context.strokeStyle = "rgba(255, 255, 255, 0.08)";
    context.fillStyle = "rgba(238, 247, 255, 0.72)";

    for (const tickFrequency of xTicks) {
      const tickX = plotX + getFrequencyX(tickFrequency, plotWidth, scale, minFrequency, maxFrequency);
      context.beginPath();
      context.moveTo(tickX, plotY);
      context.lineTo(tickX, plotY + plotHeight);
      context.stroke();
      context.textAlign = tickX <= plotX + 2 ? "left" : tickX >= plotX + plotWidth - 2 ? "right" : "center";
      context.fillText(formatFrequencyCompact(tickFrequency), tickX, plotY + plotHeight + 18);
    }

    context.textAlign = "right";
    for (let index = 0; index < 5; index += 1) {
      const ratio = index / 4;
      const tickValue = range.max - (range.max - range.min) * ratio;
      const tickY = plotY + ratio * plotHeight;
      context.beginPath();
      context.moveTo(plotX, tickY);
      context.lineTo(plotX + plotWidth, tickY);
      context.stroke();
      context.fillText(formatValue(tickValue), plotX - 10, tickY + 4);
    }

    context.fillStyle = "rgba(238, 247, 255, 0.92)";
    context.textAlign = "center";
    context.fillText("Driven frequency", plotX + plotWidth / 2, height - 10);

    context.save();
    context.translate(20, plotY + plotHeight / 2);
    context.rotate(-Math.PI / 2);
    context.fillText(yAxisLabel, 0, 0);
    context.restore();

    if (rows.length === 0) {
      context.fillStyle = "rgba(238, 247, 255, 0.56)";
      context.fillText(emptyLabel, plotX + plotWidth / 2, plotY + plotHeight / 2);
      context.restore();
      return;
    }

    if (useBand) {
      context.fillStyle = styles.bandFillStyle;
      context.beginPath();

      for (let index = 0; index < rows.length; index += 1) {
        const row = rows[index];
        const x = plotX + getFrequencyX(row.frequency, plotWidth, scale, minFrequency, maxFrequency);
        const y = plotY + getChartY(row[series.meanKey] + row[series.stdKey], plotHeight, range);
        if (index === 0) {
          context.moveTo(x, y);
        } else {
          context.lineTo(x, y);
        }
      }

      for (let index = rows.length - 1; index >= 0; index -= 1) {
        const row = rows[index];
        const x = plotX + getFrequencyX(row.frequency, plotWidth, scale, minFrequency, maxFrequency);
        const y = plotY + getChartY(row[series.meanKey] - row[series.stdKey], plotHeight, range);
        context.lineTo(x, y);
      }

      context.closePath();
      context.fill();
    }

    context.strokeStyle = styles.strokeStyle;
    context.lineWidth = 2.5;
    context.beginPath();

    for (let index = 0; index < rows.length; index += 1) {
      const row = rows[index];
      const x = plotX + getFrequencyX(row.frequency, plotWidth, scale, minFrequency, maxFrequency);
      const y = plotY + getChartY(row[series.meanKey], plotHeight, range);
      if (index === 0) {
        context.moveTo(x, y);
      } else {
        context.lineTo(x, y);
      }
    }

    if (rows.length > 1) {
      context.stroke();
    }

    for (const row of rows) {
      const x = plotX + getFrequencyX(row.frequency, plotWidth, scale, minFrequency, maxFrequency);
      const y = plotY + getChartY(row[series.meanKey], plotHeight, range);
      const radius = row.preview ? 5 : 3.5;

      context.beginPath();
      context.fillStyle = row.preview ? styles.previewFillStyle : styles.strokeStyle;
      context.arc(x, y, radius, 0, Math.PI * 2);
      context.fill();
    }

    if (previewRow && !rows.includes(previewRow)) {
      const x = plotX + getFrequencyX(previewRow.frequency, plotWidth, scale, minFrequency, maxFrequency);
      const y = plotY + getChartY(previewRow[series.meanKey], plotHeight, range);
      context.beginPath();
      context.fillStyle = styles.previewFillStyle;
      context.arc(x, y, 5, 0, Math.PI * 2);
      context.fill();

      if (useBand) {
        context.beginPath();
        context.strokeStyle = styles.strokeStyle;
        context.lineWidth = 1.5;
        context.arc(x, y, 8, 0, Math.PI * 2);
        context.stroke();
      }
    }

    context.restore();
  }

  global.ResponseExperimentUiCommon = {
    drawMetricChart,
    drawWaveform,
    drawWaveformGrid,
    formatDb,
    formatHertz,
    formatOffset,
    getMetricRange,
  };
})(window);
