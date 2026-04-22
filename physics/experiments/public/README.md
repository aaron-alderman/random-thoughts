# Public Experiment App

This folder contains the browser-side files for the local audio and response experiments served by `../server.js`.

## Contents

- `index.html`, `app.js`, and `styles.css` are the main live-audio interface.
- `fft-heatmap-common.js` and `response-experiment-ui-common.js` provide shared display and chart helpers.
- `transient-*` pages and scripts run phase-jump and click-transient experiments.
- `tracked-response.*` records matched response across a sweep.
- `adaptive-response.*` implements the adaptive response-mapping experiment.

## Run

See `../README.md` for the Node server command and local URLs.
