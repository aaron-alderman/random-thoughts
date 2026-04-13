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

## Use

1. Click `Start Audio`.
2. Allow microphone access in the browser.
3. Watch the waveform and FFT update live.
4. Enter the sine frequency directly as a numeric value in Hz.
5. Adjust amplitude with the slider and toggle the sine generator on or off.
6. Use `Enable sweep`, `Start frequency`, `End frequency`, `Number of steps`, and `Time per step` to run a bounded stepped frequency sweep.
7. The FFT panel is now a heatmap: each completed dwell interval becomes a new row.
8. Use `Reset Heatmap` to clear the recorded rows and start fresh from the current point.
9. Use `Export to CSV` to save the recorded heatmap rows, with one row per completed sweep step.
10. Use the advanced FFT controls to change size, smoothing, dB range, hot-frame rejection percentile, display-only hot-bin suppression, linear vs log frequency scale, and the visible start/end frequency window.
11. All analysis and sweep options are saved in browser local storage and restored on refresh.

## Notes

- On Windows, Chrome or Edge are the safest choices for Web Audio and microphone access.
- The browser handles the audio capture and playback, so this approach avoids native Node audio-driver headaches.
- The heatmap records one averaged FFT row per sweep step, so you can compare driven frequency against measured response across time.
- The heatmap x-axis shows response frequency, and the y-axis shows the driven sweep frequency for each recorded row.
- CSV export writes one record per completed sweep row, with the sweep frequency and all FFT response bins as columns.
- The sweep now runs from the configured start frequency to the configured end frequency, and can loop back to the start automatically.
- Sweep spacing can be linear or logarithmic; logarithmic spacing is usually the more natural choice for audio work.
- Hot-frame rejection stores the raw FFT frames for the current dwell interval only, then can reject the top percentile of high-power frames before committing that step's average.
- Display-only anomalous-bin suppression compares each response-frequency bin against that same bin's recent history for the row, and only changes the rendered heatmap, not the stored/exported data.
- To keep unattended runs bounded, the display-only per-bin history uses a limited recent visit history per row rather than unbounded storage.
- Automatic loop-back re-samples the same sweep frequencies and averages them into the existing heatmap rows; only `Reset Heatmap` or `Restart Sweep + Clear` wipes the stored rows.
- The older Python prototype is still in the folder, but the Node/web version is now the recommended path.
