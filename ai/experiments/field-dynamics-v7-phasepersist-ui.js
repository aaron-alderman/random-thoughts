const cvField  = document.getElementById('cvField');
const cvSigIn  = document.getElementById('cvSigIn');
const cvSigOut = document.getElementById('cvSigOut');
const cvProbe  = document.getElementById('cvProbe');
const cvLock   = document.getElementById('cvLock');
const cxF  = cvField.getContext('2d');
const cxIn = cvSigIn.getContext('2d');
const cxOut= cvSigOut.getContext('2d');
const cxProbe = cvProbe.getContext('2d');
const cxLock = cvLock.getContext('2d');

function resizeAll() {
  const fw=document.getElementById('fieldWrap');
  const fr=fw.getBoundingClientRect();
  cvField.width=Math.floor(fr.width);
  cvField.height=Math.floor(fr.height);
  for (const cv of [cvSigIn,cvProbe,cvSigOut,cvLock]) {
    const p=cv.parentElement;
    cv.width=Math.floor(p.offsetWidth);
    cv.height=Math.floor(p.offsetHeight);
  }
}

function renderField() {
  const w=cvField.width, h=cvField.height;
  const cw=w/N, ch=h/N;

  // Render C as base — structure visible
  for (let y=0;y<N;y++) {
    for (let x=0;x<N;x++) {
      const i=y*N+x;
      const rawAngle=Math.atan2(Xi[i],Xr[i]);
      const angle=isDay() ? rawAngle-currentDrivePhase() : rawAngle;
      const mag=Math.sqrt(Xr[i]*Xr[i]+Xi[i]*Xi[i]);
      // During day, hue is drive-relative: phase-locked propagation stays visually stable;
      // background drift keeps changing color and is easier to distinguish.
      const hue=((angle/TWO_PI)*360+360)%360;
      const sat=35 + Math.min(55,S[i]*120);
      const lit=12 + Math.min(58,mag*85);
      cxF.fillStyle=`hsl(${hue},${sat}%,${lit}%)`;
      cxF.fillRect(x*cw,y*ch,cw+0.5,ch+0.5);
    }
  }

  // Warmup overlay
  if (isWarmup()) {
    const prog=cycleStepInPhase/P.warmup;
    cxF.fillStyle=`rgba(255,224,64,${0.15*(1-prog)})`;
    cxF.fillRect(0,0,w,h);
    cxF.fillStyle='rgba(255,224,64,0.5)';
    cxF.font='bold 22px Unbounded';
    cxF.fillText(`WARMUP ${Math.round(prog*100)}%`,8,h-8);
  }

  // Night overlay
  if (!isDay() && !isWarmup()) {
    const nightProg=Math.min(cycleStepInPhase/50,1);
    cxF.fillStyle=`rgba(12,34,92,${nightProg*0.22})`;
    cxF.fillRect(0,0,w,h);
  }

  // Input node marker
  if (inputNode>=0) {
    const [ix,iy]=nodeXY(inputNode);
    const px=ix*cw, py=iy*ch;
    cxF.strokeStyle=`rgba(255,138,61,${isDay()?1.0:0.75})`;
    cxF.lineWidth=5;
    cxF.shadowColor='rgba(255,138,61,0.9)';
    cxF.shadowBlur=8;
    cxF.strokeRect(px-2,py-2,cw+4,ch+4);
    cxF.shadowBlur=0;
    // Drive value as brightness fill
    const dmag=Math.sqrt(DRIVE_R[inputNode]*DRIVE_R[inputNode]+DRIVE_I[inputNode]*DRIVE_I[inputNode]);
    if (dmag>0) {
      cxF.fillStyle=`rgba(255,138,61,${Math.min(0.9,0.25+dmag*0.8)})`;
      cxF.fillRect(px,py,cw,ch);
    }
    // Update label position
    const lbl=document.getElementById('lblIn');
    lbl.style.display='block';
    lbl.style.left=(px+cw+2)+'px';
    lbl.style.top=py+'px';
  }

  // Output node marker
  if (outputNode>=0) {
    const [ox,oy]=nodeXY(outputNode);
    const px=ox*cw, py=oy*ch;
    // Color by correlation during night
    const corrAlpha=!isDay()?Math.max(0.3,corrValue):0.7;
    cxF.strokeStyle=`rgba(53,255,208,${Math.max(0.7,corrAlpha)})`;
    cxF.lineWidth=5;
    cxF.shadowColor='rgba(53,255,208,0.9)';
    cxF.shadowBlur=8;
    cxF.strokeRect(px-2,py-2,cw+4,ch+4);
    cxF.shadowBlur=0;
    const lbl=document.getElementById('lblOut');
    lbl.style.display='block';
    lbl.style.left=(px+cw+2)+'px';
    lbl.style.top=py+'px';
  }

  // One-hop probe marker
  const pn=probeNode();
  if (pn>=0 && pn!==inputNode && pn!==outputNode) {
    const [pxn,pyn]=nodeXY(pn);
    cxF.strokeStyle='rgba(255,233,106,0.9)'; cxF.lineWidth=2;
    cxF.strokeRect(pxn*cw+1,pyn*ch+1,cw-2,ch-2);
  }

  // Path line between input and output
  if (inputNode>=0 && outputNode>=0) {
    const [ix,iy]=nodeXY(inputNode);
    const [ox,oy]=nodeXY(outputNode);
    cxF.strokeStyle='rgba(181,156,255,0.45)';
    cxF.lineWidth=4;
    cxF.setLineDash([3,6]);
    cxF.beginPath();
    cxF.moveTo((ix+0.5)*cw,(iy+0.5)*ch);
    cxF.lineTo((ox+0.5)*cw,(oy+0.5)*ch);
    cxF.stroke();
    cxF.setLineDash([]);
  }
}

function renderSignal(ctx, data, color, label, fixedScale=0) {
  const w=ctx.canvas.width, h=ctx.canvas.height;
  ctx.fillStyle='#050b13'; ctx.fillRect(0,0,w,h);
  ctx.strokeStyle='rgba(255,255,255,0.16)'; ctx.lineWidth=1;
  ctx.beginPath(); ctx.moveTo(0,h/2); ctx.lineTo(w,h/2); ctx.stroke();
  if (data.length<2) return;
  const maxAbs=fixedScale || Math.max(...data.map(v=>Math.abs(v)),0.001);
  ctx.strokeStyle=color; ctx.lineWidth=3; ctx.beginPath();
  for (let i=0;i<data.length;i++) {
    const x=(i/(HIST_LEN-1))*w;
    const y=h/2-(data[i]/maxAbs)*(h*0.42);
    i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);
  }
  ctx.stroke();
}

function setText(id, value) {
  const el=document.getElementById(id);
  if (el) el.textContent=value;
}

function labelDecimals(labelEl, sliderEl) {
  if (labelEl) {
    if (!labelEl.dataset.decimals) {
      const seed=(labelEl.textContent || '').trim() || sliderEl.step || '1';
      const m=seed.match(/\.(\d+)/);
      labelEl.dataset.decimals=m ? String(m[1].length) : '0';
    }
    return parseInt(labelEl.dataset.decimals, 10) || 0;
  }
  const step=sliderEl?.step || '1';
  const m=step.match(/\.(\d+)/);
  return m ? m[1].length : 0;
}

function formatSliderValue(sliderEl, labelEl, value) {
  const num=Number(value);
  if (!Number.isFinite(num)) return '—';
  return num.toFixed(labelDecimals(labelEl, sliderEl));
}

function fmtNum(v, digits=3) {
  return Number.isFinite(v) ? v.toFixed(digits) : '—';
}

function fmtSigned(v, digits=3) {
  return Number.isFinite(v) ? `${v>=0?'+':''}${v.toFixed(digits)}` : '—';
}

function fmtAngle(v) {
  return Number.isFinite(v) ? `${(v*180/Math.PI).toFixed(1)}°` : '—';
}

function fmtPeriodValue(v) {
  return Number.isFinite(v) ? `${Math.round(v)} st` : '—';
}

function updateNodeDebug(prefix, node) {
  if (!node.exists) {
    setText(`dbg${prefix}Mag`, '—');
    setText(`dbg${prefix}Phase`, '—');
    setText(`dbg${prefix}Delta`, '—');
    setText(`dbg${prefix}Lock`, '—');
    setText(`dbg${prefix}Omega`, '—');
    setText(`dbg${prefix}Mem`, '—');
    return;
  }
  setText(`dbg${prefix}Mag`, fmtNum(node.mag, 3));
  setText(`dbg${prefix}Phase`, fmtAngle(node.phase));
  setText(`dbg${prefix}Delta`, fmtSigned(node.phaseDelta, 4));
  setText(`dbg${prefix}Lock`, fmtSigned(node.driveLock, 3));
  setText(`dbg${prefix}Omega`, fmtSigned(node.omega, 4));
  setText(`dbg${prefix}Mem`, fmtNum(node.nodeMemory, 3));
}

function updateDebugPanel(snap) {
  const total=snap.warmup ? P.warmup : (snap.day ? P.dayLen : P.nightLen);
  setText('dbgCycleMode', snap.cycleMode.toUpperCase());
  setText('dbgCycleStep', `${snap.cycleStepInPhase} / ${total}`);
  setText('dbgDriveEnv', fmtNum(snap.driveEnv, 3));
  setText('dbgDrivePhase', fmtAngle(snap.drivePhase));
  setText('dbgDriveOmega', `${fmtSigned(snap.driveOmega, 4)} | ${fmtPeriodValue(snap.drivePeriod)}`);
  setText('dbgCorr', fmtSigned(snap.corrValue, 3));
  setText('dbgPeakCorr', fmtSigned(snap.peakCorr, 3));
  setText('dbgDwell', `${snap.dwellSteps} / ${snap.bestDwell}`);

  if (snap.output.exists) {
    setText('dbgReplayOmega', fmtSigned(snap.output.omega, 4));
    setText('dbgReplayGain', fmtNum(snap.output.replayGain, 4));
    setText('dbgReplayMem', fmtNum(snap.output.replayMem, 3));
    setText('dbgReplayAdv', fmtSigned(snap.output.replayAdv, 5));
    setText('dbgReplayPeriod', fmtPeriodValue(snap.output.replayPeriod));
  } else {
    setText('dbgReplayOmega', '—');
    setText('dbgReplayGain', '—');
    setText('dbgReplayMem', '—');
    setText('dbgReplayAdv', '—');
    setText('dbgReplayPeriod', '—');
  }
  setText('dbgPathMemory', snap.path.length ? fmtNum(snap.path.memoryMean, 3) : '—');

  updateNodeDebug('Input', snap.input);
  updateNodeDebug('Probe', snap.probe);
  updateNodeDebug('Output', snap.output);

  if (!snap.path.length) {
    setText('dbgPathLen', '—');
    setText('dbgPathMag', '—');
    setText('dbgPathDelta', '—');
    setText('dbgPathLock', '—');
    setText('dbgPathOmega', '—');
    setText('dbgPathAdv', '—');
    return;
  }
  setText('dbgPathLen', String(snap.path.length));
  setText('dbgPathMag', fmtNum(snap.path.meanMag, 3));
  setText('dbgPathDelta', fmtSigned(snap.path.meanPhaseDelta, 4));
  setText('dbgPathLock', fmtSigned(snap.path.meanDriveLock, 3));
  setText('dbgPathOmega', fmtSigned(snap.path.meanOmega, 4));
  setText('dbgPathAdv', fmtSigned(snap.path.meanReplayAdv, 5));
}

function updateDOM() {
  const snap=getDebugSnapshot();
  // Metrics
  const inV=inputNode>=0
    ?Math.sqrt(Xr[inputNode]*Xr[inputNode]+Xi[inputNode]*Xi[inputNode]):0;
  const outV=outputNode>=0
    ?Math.sqrt(Xr[outputNode]*Xr[outputNode]+Xi[outputNode]*Xi[outputNode]):0;
  let meanX=0; const sz=N*N;
  for (let i=0;i<sz;i++)
    meanX+=Math.sqrt(Xr[i]*Xr[i]+Xi[i]*Xi[i]);
  meanX/=sz;

  setText('sIn', inV.toFixed(3));
  setText('sOut', outV.toFixed(3));
  setText('sX', meanX.toFixed(3));
  setText('sCorr', snap.path.memoryMean.toFixed(3));
  setText('sT', String(step));
  setText('stepLbl', `T=${step}`);

  const pProbe=estimatePeriod(probeHistory);
  const pOut=estimatePeriod(outputHistory);
  const dayR=rms(outputDayHistory);
  const nightR=rms(outputNightHistory);
  setText('dDrivePer', String(P.drivePer));
  setText('dProbePer', fmtPeriod(pProbe));
  setText('dOutPer', fmtPeriod(pOut));
  setText('dLock', snap.path.memoryMean.toFixed(3));
  setText('dGain', dayR>1e-6?(nightR/dayR).toFixed(2):'—');
  setText('dCycles', String(cycleCount));

  // Phase chip
  const day=isDay();
  const wu=isWarmup();
  const phaseLabel=wu?'WARMUP':day?'DAY':'NIGHT';
  const phaseCls=wu?'chip warn':day?'chip day':'chip night';
  setText('chipPhase', phaseLabel);
  document.getElementById('chipPhase').className=phaseCls;

  // Dwell chip
  if (dwellSteps>0) {
    document.getElementById('chipDwell').textContent=`DWELL ${dwellSteps}`;
    document.getElementById('chipDwell').className='chip on';
  } else {
    document.getElementById('chipDwell').textContent='DWELL —';
    document.getElementById('chipDwell').className='chip';
  }

  // Corr chip
  const memNow=snap.path.memoryMean;
  setText('chipCorr', memNow>0.02?`MEM ${memNow.toFixed(2)}`:'MEM —');
  document.getElementById('chipCorr').className=
    memNow>0.02?'chip on':'chip';

  // Cycle progress
  const wu2=isWarmup();
  const total=wu2?P.warmup:(isDay()?P.dayLen:P.nightLen);
  const pct=(cycleStepInPhase/total)*100;
  const prog=document.getElementById('cycleProg');
  prog.style.width=pct+'%';
  prog.style.background=wu2?'rgba(255,224,64,0.4)':isDay()?'var(--day)':'var(--night)';

  updateDebugPanel(snap);
}

function updateNodeLabels() {
  if (inputNode>=0) {
    const [x,y]=nodeXY(inputNode);
    document.getElementById('mInPos').textContent=`(${x},${y})`;
  } else {
    document.getElementById('mInPos').textContent='—';
  }
  if (outputNode>=0) {
    const [x,y]=nodeXY(outputNode);
    document.getElementById('mOutPos').textContent=`(${x},${y})`;
  } else {
    document.getElementById('mOutPos').textContent='—';
  }
  if (inputNode>=0 && outputNode>=0) {
    const [ix,iy]=nodeXY(inputNode);
    const [ox,oy]=nodeXY(outputNode);
    const dist=Math.round(Math.sqrt((ix-ox)**2+(iy-oy)**2));
    document.getElementById('mDist').textContent=`${dist} nodes`;
  } else {
    document.getElementById('mDist').textContent='—';
  }
}

// ── Main loop ─────────────────────────────────────────────────
let lastT=0;
function loop(ts) {
  if (ts-lastT<1000/30) { requestAnimationFrame(loop); return; }
  lastT=ts;
  if (running) {
    update();
    updateDOM();
  }
  renderField();
  renderSignal(cxIn,  inputHistory,  'rgba(255,138,61,1.0)', '', Math.max(P.driveAmp,0.1));
  renderSignal(cxProbe, probeHistory, 'rgba(255,233,106,1.0)');
  renderSignal(cxOut, outputHistory, 'rgba(53,255,208,1.0)');
  renderSignal(cxLock, outputLockHistory, 'rgba(114,255,143,1.0)');
  requestAnimationFrame(loop);
}

// ── Controls ──────────────────────────────────────────────────
const CONTROL_BINDINGS = [
  ['slDriveAmp','vDriveAmp','driveAmp'],
  ['slDrivePer','vDrivePer','drivePer'],
  ['slDayLen',  'vDayLen',  'dayLen'],
  ['slNightLen','vNightLen','nightLen'],
  ['slCorrThr', 'vCorrThr', 'corrThr'],
  ['slAlpha',   'vAlpha',   'alpha'],
  ['slW',       'vW',       'W'],
  ['slKAlign',  'vKAlign',  'kAlign'],
  ['slEdgeGain','vEdgeGain','edgeGain'],
  ['slRetain',  'vRetain',  'retain'],
  ['slPhaseInertia','vPhaseInertia','phaseInertia'],
  ['slPersistAlpha','vPersistAlpha','persistAlpha'],
  ['slBeta',    'vBeta',    'beta'],
  ['slSelf',    'vSelf',    'selfEx'],
  ['slPhi',     'vPhi',     'phi'],
  ['slTri',     'vTri',     'triWeight'],
  ['slWarmup',  'vWarmup',  'warmup'],
  ['slEps',     'vEps',     'epsilon'],
  ['slOmegaLearn','vOmegaLearn','omegaLearn'],
  ['slEdgeDecay','vEdgeDecay','edgeDecay'],
  ['slEta',     'vEta',     'eta'],
  ['slTauC',    'vTauC',    'tauC'],
];

function bsl(id,vid,key) {
  const el = document.getElementById(id);
  if (!el) return;
  el.addEventListener('input',function(){
    P[key]=parseFloat(this.value);
    if (vid) {
      const v = document.getElementById(vid);
      if (v) v.textContent = formatSliderValue(this, v, P[key]);
    }
  });
}

function syncControlsFromParams() {
  for (const [id, vid, key] of CONTROL_BINDINGS) {
    const el=document.getElementById(id);
    if (!el || !(key in P)) continue;
    el.value=String(P[key]);
    if (vid) {
      const label=document.getElementById(vid);
      if (label) label.textContent=formatSliderValue(el, label, P[key]);
    }
  }
}

for (const binding of CONTROL_BINDINGS) bsl(...binding);
syncControlsFromParams();

document.getElementById('btnRun').addEventListener('click',()=>{
  running=!running;
  const b=document.getElementById('btnRun');
  b.textContent=running?'⏸ Pause':'▶ Run';
  b.className=running?'active':'';
});
document.getElementById('btnReset').addEventListener('click',()=>{
  initFields();
  document.getElementById('btnFDay').className='';
  document.getElementById('btnFNight').className='';
  document.getElementById('btnAuto').className='active';
});

// Cycle mode
document.getElementById('btnFDay').addEventListener('click',()=>{
  cycleMode='forceday';
  document.getElementById('btnFDay').className='active';
  document.getElementById('btnFNight').className='';
  document.getElementById('btnAuto').className='';
});
document.getElementById('btnFNight').addEventListener('click',()=>{
  cycleMode='forcenight';
  document.getElementById('btnFDay').className='';
  document.getElementById('btnFNight').className='active';
  document.getElementById('btnAuto').className='';
  onNightStart();
});
document.getElementById('btnAuto').addEventListener('click',()=>{
  cycleMode='warmup'; cycleStepInPhase=0;
  document.getElementById('btnFDay').className='';
  document.getElementById('btnFNight').className='';
  document.getElementById('btnAuto').className='active';
});

// Grid
document.getElementById('btnG32').addEventListener('click',()=>{
  N=32; inputNode=-1; outputNode=-1; initFields(); setDefaultNodes();
  document.getElementById('btnFDay').className='';
  document.getElementById('btnFNight').className='';
  document.getElementById('btnAuto').className='active';
  document.getElementById('btnG32').className='active';
  document.getElementById('btnG64').className='';
});
document.getElementById('btnG64').addEventListener('click',()=>{
  N=64; inputNode=-1; outputNode=-1; initFields(); setDefaultNodes();
  document.getElementById('btnFDay').className='';
  document.getElementById('btnFNight').className='';
  document.getElementById('btnAuto').className='active';
  document.getElementById('btnG64').className='active';
  document.getElementById('btnG32').className='';
});

// Field clicks — place input/output nodes
cvField.addEventListener('click',(e)=>{
  const r=cvField.getBoundingClientRect();
  const x=Math.floor((e.clientX-r.left)/r.width*N);
  const y=Math.floor((e.clientY-r.top)/r.height*N);
  inputNode=idx(x,y);
  updateNodeLabels();
});

cvField.addEventListener('contextmenu',(e)=>{
  e.preventDefault();
  const r=cvField.getBoundingClientRect();
  const x=Math.floor((e.clientX-r.left)/r.width*N);
  const y=Math.floor((e.clientY-r.top)/r.height*N);
  outputNode=idx(x,y);
  updateNodeLabels();
});

window.addEventListener('resize',resizeAll);

setTimeout(()=>{
  resizeAll();
  initFields();
  // Default positions — user can move them
  // Input/output start close enough to diagnose propagation before long-path memory.
  // Move output farther right after a visible day signal appears.
  setDefaultNodes();
  requestAnimationFrame(loop);
},120);
