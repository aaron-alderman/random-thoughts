# Audio Lab

Node-based local web app for Windows that:

- captures live audio from your microphone,
- displays the waveform,
- displays a realtime FFT,
- emits a sine wave through your speakers or headphones.

## Stack

- `server.js` is a tiny zero-dependency Node server.
- `public/app.js` uses browser audio APIs: `getUserMedia`, `AudioContext`, `OscillatorNode`, and `AnalyserNode`.
- `public/fft-heatmap-common.js` is the shared heatmap/display helper layer used by the main app and transient experiments.
- `public/response-experiment-ui-common.js` is the shared waveform/chart helper layer used by the tracked-response and adaptive-response experiments.
- `public/adaptive-response-model.js` holds the adaptive-response experiment's scheduler, measurement math, and running statistics, `public/adaptive-response-ui.js` owns the DOM and chart rendering, and `public/adaptive-response.js` is now a thinner audio/controller layer.
- `public/styles.css` provides the UI and canvas styling.
- `public/README.md` maps the browser-side experiment pages and shared helpers.

## Requirements

Install Node.js 20 or newer on Windows.

You can download it from [nodejs.org](https://nodejs.org/).

## Run

Open PowerShell in this folder and run:

```powershell
npm start
```

Then open:

```text
http://127.0.0.1:3000
```

Phase-jump transient experiment:

```text
http://127.0.0.1:3000/transient-phase.html
```

Click transient experiments:

```text
http://127.0.0.1:3000/transient-click-width.html
http://127.0.0.1:3000/transient-click-amplitude.html
http://127.0.0.1:3000/transient-click-count.html
http://127.0.0.1:3000/transient-click-spacing.html
```

Tracked response experiment:

```text
http://127.0.0.1:3000/tracked-response.html
```

Adaptive response experiment:

```text
http://127.0.0.1:3000/adaptive-response.html
```

## Use

1. Click `Start Audio`.
2. Allow microphone access in the browser.
3. Watch the waveform and FFT update live.
4. Enter the sine frequency directly as a numeric value in Hz.
5. Adjust amplitude and L/R balance with the sliders, and toggle the sine generator on or off.
6. Use `Enable sweep`, `Start frequency`, `End frequency`, `Number of steps`, and `Time per step` to run a bounded sweep, and turn on `Continuous sweep` if you want the tone to glide instead of jumping between steps.
7. The FFT panel is now a heatmap: each completed dwell interval becomes a new row.
8. Use `Reset Heatmap` to clear the recorded rows and start fresh from the current point.
9. Use `Export to CSV` to save the recorded heatmap rows, with one row per completed sweep step.
10. Use the advanced FFT controls to change size, smoothing, dB range, per-column background subtraction, linear vs log frequency scale, and the visible start/end frequency window.
11. All analysis and sweep options are saved in browser local storage and restored on refresh.

## Notes

- On Windows, Chrome or Edge are the safest choices for Web Audio and microphone access.
- The browser handles the audio capture and playback, so this approach avoids native Node audio-driver headaches.
- The sine output can be panned fully left or fully right if you want to drive only one speaker.
- The heatmap records one averaged FFT row per sweep step, so you can compare driven frequency against measured response across time.
- The heatmap x-axis shows response frequency, and the y-axis shows the driven sweep frequency for each recorded row.
- The heatmap also shows cumulative marginals: a top profile for total response per frequency column and a right-side profile for total response per sweep row.
- CSV export writes one record per completed sweep row, with the sweep frequency and all FFT response bins as columns.
- The sweep now runs from the configured start frequency to the configured end frequency, and can loop back to the start automatically.
- In continuous mode, the tone glides smoothly across the configured range while the heatmap still accumulates into the configured sweep bins.
- Sweep spacing can be linear or logarithmic; logarithmic spacing is usually the more natural choice for audio work.
- Display-only column background subtraction learns a low-percentile baseline for each response-frequency column across the committed heatmap rows, then subtracts that baseline from every displayed row without changing the stored/exported data. It activates once at least two committed rows exist.
- Automatic loop-back re-samples the same sweep frequencies and averages them into the existing heatmap rows; only `Reset Heatmap` or `Restart Sweep + Clear` wipes the stored rows.
- The older Python prototype is still in the folder, but the Node/web version is now the recommended path.
- `public/transient-phase.html` is a separate experiment page for fixed-carrier phase-jump transient testing, with the heatmap y-axis representing phase jump in degrees.
- In the phase-jump page, the jump is now a one-shot event per dwell interval after the configured delay, not a repeated phase-kick train.
- The click transient pages share the same FFT heatmap pipeline, but replace phase jumps with a simpler one-shot click train so the carrier can stay continuous.
- `public/transient-click-width.html` sweeps click width, `public/transient-click-amplitude.html` sweeps click amplitude, `public/transient-click-count.html` sweeps click count, and `public/transient-click-spacing.html` sweeps click spacing.
- In the click pages, the x-axis remains response frequency and the heatmap y-axis is whichever click parameter that page is sweeping.
- `public/tracked-response.html` sweeps the drive frequency and records the returned peak nearest that same frequency, charting both matched amplitude and full width at half maximum across the sweep.
- `public/tracked-response.html` also plots the signed peak offset, so you can see how far the matched return drifts away from the driven frequency across the sweep.
- The tracked-response peak match is constrained to stay within `±5 Hz` of the driven frequency.
- The tracked-response page includes an optional per-step settle window so the first part of each new frequency step can be ignored before measurements begin.
- `public/adaptive-response.html` is a separate response-mapping experiment built around an open-ended adaptive scheduler: `explore` inserts new midpoint frequencies in the intervals with the largest amplitude and uncertainty changes, then `refine` re-samples existing points to tighten the estimate where the response is strongest or noisiest.
- The adaptive response charts show running means with one-sigma uncertainty bands for amplitude, FWHM width, and peak offset, and the CSV export writes mean and standard deviation for each sampled frequency.
