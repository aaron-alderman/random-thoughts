# Audio Lab

Node-based local web app for Windows that:

- captures live audio from your microphone,
- displays the waveform,
- displays a realtime FFT,
- emits a sine wave through your speakers or headphones.

## Stack

- `server.js` is a tiny zero-dependency Node server.
- `public/app.js` uses browser audio APIs: `getUserMedia`, `AudioContext`, `OscillatorNode`, and `AnalyserNode`.
- `public/styles.css` provides the UI and canvas styling.

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
10. Use the advanced FFT controls to change size, smoothing, dB range, hot-frame rejection percentile, display-only hot-bin suppression, per-column background subtraction, linear vs log frequency scale, and the visible start/end frequency window.
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
- Hot-frame rejection stores the raw FFT frames for the current dwell interval only, then can reject the top percentile of high-power frames before committing that step's average.
- Display-only anomalous-bin suppression compares each response-frequency bin against that same bin's recent history for the row, and only changes the rendered heatmap, not the stored/exported data.
- Display-only column background subtraction learns a low-percentile baseline for each response-frequency column across the committed heatmap rows, then subtracts that baseline from every displayed row without changing the stored/exported data. It activates once at least two committed rows exist.
- To keep unattended runs bounded, the display-only per-bin history uses a limited recent visit history per row rather than unbounded storage.
- Automatic loop-back re-samples the same sweep frequencies and averages them into the existing heatmap rows; only `Reset Heatmap` or `Restart Sweep + Clear` wipes the stored rows.
- The older Python prototype is still in the folder, but the Node/web version is now the recommended path.
- `transient-phase.html` is a separate experiment page for fixed-carrier phase-jump transient testing, with the heatmap y-axis representing phase jump in degrees.
- In the phase-jump page, the jump is now a one-shot event per dwell interval after the configured delay, not a repeated phase-kick train.
- The click transient pages share the same FFT heatmap pipeline, but replace phase jumps with a simpler one-shot click train so the carrier can stay continuous.
- `transient-click-width.html` sweeps click width, `transient-click-amplitude.html` sweeps click amplitude, `transient-click-count.html` sweeps click count, and `transient-click-spacing.html` sweeps click spacing.
- In the click pages, the x-axis remains response frequency and the heatmap y-axis is whichever click parameter that page is sweeping.
