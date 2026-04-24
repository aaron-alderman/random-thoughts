// ============================================================
// FIELD DYNAMICS v6
//
// THE TASK:
//   Input node receives drive signal during DAY
//   Output node — spatially separated, placed by user —
//   should reproduce signal during NIGHT (dwell)
//   Measured by cross-correlation between
//   output signal during day and output signal during night
//
// WHAT IS NOT IN THIS FILE:
//   Rotating complex drive at input only during day
//   No global amplitude envelope
//   No hardcoded input positions
//   No hardcoded output positions
//
// DRIVE:
//   DRIVE_R/I are complex floats, default 0 every step
//   Set only for input node, only during day
//   Value is a complex rotating phase vector. The field receives Xr/Xi drive only at input.
//
// TIMESCALES — hard step counters:
//   X   — every step
//   S   — every 10 steps
//   α/β — every 100 steps
//
// OUTPUT:
//   Not designated — discovered
//   isOutput(i) = C[i] > tauC && R[i] < tauR
//                 && S[i] > tauS && no external drive
//   But for measurement we watch the user-placed output node
//   and measure correlation with input history
// ============================================================

const TWO_PI = Math.PI * 2;
let N = 32;
let running = true;
let step = 0;

// ── User-placed nodes ─────────────────────────────────────────
let inputNode  = -1;  // set by left-click
let outputNode = -1;  // set by right-click

// ── Parameters ────────────────────────────────────────────────
const P = {
  // Preset A — damped phase-transmission regime from observed working settings.
  alpha:    0.843,
  W:        0.0325,
  kAlign:   0.43,
  edgeGain: 8.00,
  retain:   0.60,
  phaseInertia: 1.25, // learned local phase velocity replay during night; weighted continuously by Sedge
  persistAlpha: 0.28, // memory-weighted damping relief during night so phase rotation remains visible
  omegaLearn:   0.12,
  edgeDecay:0.0008,
  beta:     0.485,
  phi:      0.00,
  triWeight:0.52,
  selfEx:   0.06,
  epsilon:  0.035,
  eta:      0.00,
  tauC:     0.45,
  driveAmp: 1.00,
  drivePer: 80,
  driveRamp: 32,
  dayLen:   400,
  nightLen: 400,
  corrThr:  0.5,
  warmup:   300,
};

// ── Field buffers ─────────────────────────────────────────────
let Xr, Xi, Xr2, Xi2;
let S,  S2;
let R,  C;
let AL, BL;          // local alpha, beta — updated every 100 steps
let ChF, ChS;        // fast/slow coherence history for homeostasis
let Sedge;           // learned directional edge memory, 8 per node
let Omega, PrevPhi;   // learned local phase velocity and previous phase
let PhaseDelta, DriveLock, ReplayMem, ReplayGain, ReplayAdv;
let DRIVE_R, DRIVE_I; // complex external drive — zeroed every step
let driveEnv = 0; // smoothed drive amplitude envelope

function initFields() {
  const sz = N * N;
  Xr=new Float32Array(sz); Xi=new Float32Array(sz);
  Xr2=new Float32Array(sz); Xi2=new Float32Array(sz);
  S=new Float32Array(sz);  S2=new Float32Array(sz);
  R=new Float32Array(sz);  C=new Float32Array(sz);
  AL=new Float32Array(sz); BL=new Float32Array(sz);
  ChF=new Float32Array(sz); ChS=new Float32Array(sz);
  Sedge=new Float32Array(sz*8);
  Omega=new Float32Array(sz); PrevPhi=new Float32Array(sz);
  PhaseDelta=new Float32Array(sz); DriveLock=new Float32Array(sz);
  ReplayMem=new Float32Array(sz); ReplayGain=new Float32Array(sz); ReplayAdv=new Float32Array(sz);
  DRIVE_R=new Float32Array(sz); DRIVE_I=new Float32Array(sz);

  // Initialize to a meaningful baseline — not near-zero
  // Field needs standing energy for propagation to work
  const baseline = 0.035;
  for (let i=0;i<sz;i++) {
    // Random phase, baseline magnitude
    const angle = Math.random() * TWO_PI;
    Xr[i] = baseline * Math.cos(angle) + (Math.random()-0.5)*0.01;
    Xi[i] = baseline * Math.sin(angle) + (Math.random()-0.5)*0.01;
    S[i]  = 0.1 + Math.random()*0.05;
    AL[i] = P.alpha;
    BL[i] = P.beta;
    PrevPhi[i] = Math.atan2(Xi[i], Xr[i]);
    Omega[i] = 0;
  }
  Sedge.fill(0.0);

  step=0;
  driveEnv=0;
  warmupDone=false;
  cycleMode='warmup'; cycleStepInPhase=0; cycleCount=0;
  inputHistory.length=0;
  inputNodeHistory.length=0;
  probeHistory.length=0;
  outputHistory.length=0;
  outputDayHistory.length=0;
  outputNightHistory.length=0;
  outputLockHistory.length=0;
  dwellSteps=0; bestDwell=0;
  peakCorr=0;
  corrValue=0;
  if (typeof updateNodeLabels === 'function') updateNodeLabels();
}

function idx(x,y) { x=(x+N)%N; y=(y+N)%N; return y*N+x; }
function nodeXY(i) { return [i%N, Math.floor(i/N)]; }

function setDefaultNodes() {
  inputNode  = idx(Math.floor(N/4),   Math.floor(N/2));
  outputNode = idx(Math.floor(N/4)+4, Math.floor(N/2));
  if (typeof updateNodeLabels === 'function') updateNodeLabels();
}

// ── Day / Night ───────────────────────────────────────────────
let cycleMode = 'warmup';    // 'warmup' | 'day' | 'night' | 'forceday' | 'forcenight'
let cycleStepInPhase = 0;
let cycleCount = 0;
let warmupDone = false;

function isDay() {
  if (cycleMode==='warmup')     return false; // no drive during warmup
  if (cycleMode==='forceday')   return true;
  if (cycleMode==='forcenight') return false;
  return cycleMode==='day';
}

function isWarmup() { return cycleMode==='warmup'; }

function advanceCycle() {
  if (cycleMode==='forceday' || cycleMode==='forcenight') return;

  cycleStepInPhase++;

  if (cycleMode==='warmup') {
    if (cycleStepInPhase >= P.warmup) {
      cycleMode='day'; cycleStepInPhase=0;
      warmupDone=true;
    }
    return;
  }

  if (cycleMode==='day' && cycleStepInPhase >= P.dayLen) {
    cycleMode='night'; cycleStepInPhase=0;
    onNightStart();
  } else if (cycleMode==='night' && cycleStepInPhase >= P.nightLen) {
    cycleMode='day'; cycleStepInPhase=0;
    cycleCount++;
    onDayStart();
  }
}

// ── Signal history for correlation ───────────────────────────
const HIST_LEN = 200;
const inputHistory  = [];      // external input drive trace, zero at night
const inputNodeHistory = [];  // internal state of the input node, for diagnostics if needed
const probeHistory = [];      // one-hop node toward output: confirms whether drive leaves input
const outputHistory = [];
const outputDayHistory = [];
const outputNightHistory = [];
const outputLockHistory = [];
let dwellSteps = 0;
let bestDwell  = 0;
let peakCorr   = 0;
let corrValue  = 0;

function onNightStart() {
  // Do not clear visible traces here. Clearing display histories made the
  // day/night boundary look like a physical discontinuity. Keep plots continuous;
  // only reset the memory-scoring buffers.
  outputDayHistory.length=0;
  outputNightHistory.length=0;
  dwellSteps=0;
  peakCorr=0;
  corrValue=0;
}

function onDayStart() {
  // Start a fresh day/night memory comparison, but leave visible traces intact.
  outputDayHistory.length=0;
  outputNightHistory.length=0;
  corrValue=0;
}

// Signed phase trace: rotating activity is visible here even when magnitude is flat.
// Using magnitude alone hides propagation because a phase oscillator can rotate at near-constant |X|.
function phaseTrace(i) {
  return Xr[i];
}

function currentDrivePhase() {
  return TWO_PI * (step % P.drivePer) / P.drivePer;
}

function driveLockedTrace(i) {
  if (i < 0) return 0;
  const ph=currentDrivePhase();
  // Positive/steady means the node is phase-locked to the drive.
  // This is useful as a metric, but raw Xr is the correct visual frequency trace.
  return Xr[i]*Math.cos(ph) + Xi[i]*Math.sin(ph);
}

function angleDiff(a,b) {
  let d=a-b;
  while (d > Math.PI) d -= TWO_PI;
  while (d < -Math.PI) d += TWO_PI;
  return d;
}
function nodeMemoryMean(i) {
  if (i < 0 || !Sedge) return 0;
  // Use strongest learned edge, not average over all 8 directions.
  // Averaging diluted path memory by 8x, making phase persistence almost invisible.
  let m=0;
  for (let e=0;e<8;e++) if (Sedge[i*8+e] > m) m = Sedge[i*8+e];
  return m;
}

function outputRawTrace(i) {
  return i < 0 ? 0 : Xr[i];
}
function magnitudeAt(i) {
  return i < 0 ? 0 : Math.sqrt(Xr[i]*Xr[i]+Xi[i]*Xi[i]);
}
function phaseAt(i) {
  return i < 0 ? NaN : Math.atan2(Xi[i], Xr[i]);
}
function omegaToPeriod(omega) {
  return Math.abs(omega) > 1e-6 ? TWO_PI / Math.abs(omega) : NaN;
}
function probeNode() {
  if (inputNode < 0 || outputNode < 0) return -1;
  const [ix,iy]=nodeXY(inputNode), [ox,oy]=nodeXY(outputNode);
  return idx(ix+Math.sign(ox-ix), iy+Math.sign(oy-iy));
}
function edgeIndexForStep(sx,sy) {
  for (let e=0;e<nb8.length;e++) if (nb8[e][0]===sx && nb8[e][1]===sy) return e;
  return -1;
}
function pathMemoryMean() {
  if (inputNode < 0 || outputNode < 0 || !Sedge) return 0;
  let [x,y]=nodeXY(inputNode); const [ox,oy]=nodeXY(outputNode);
  let sum=0, n=0, guard=N*2;
  while ((x!==ox || y!==oy) && guard-- > 0) {
    const sx=Math.sign(ox-x), sy=Math.sign(oy-y);
    const e=edgeIndexForStep(sx,sy);
    if (e<0) break;
    sum += Sedge[idx(x,y)*8+e]; n++;
    x=(x+sx+N)%N; y=(y+sy+N)%N;
  }
  return n ? sum/n : 0;
}
function pathNodeIndices() {
  if (inputNode < 0 || outputNode < 0) return [];
  const nodes=[inputNode];
  let [x,y]=nodeXY(inputNode); const [ox,oy]=nodeXY(outputNode);
  let guard=N*2;
  while ((x!==ox || y!==oy) && guard-- > 0) {
    x=(x+Math.sign(ox-x)+N)%N;
    y=(y+Math.sign(oy-y)+N)%N;
    nodes.push(idx(x,y));
  }
  return nodes;
}
function meanBy(nodes, getter) {
  if (!nodes.length) return 0;
  let sum=0;
  for (const i of nodes) sum += getter(i);
  return sum / nodes.length;
}
function getNodeDebug(i) {
  return {
    index: i,
    exists: i >= 0,
    mag: magnitudeAt(i),
    phase: phaseAt(i),
    phaseDelta: i >= 0 ? PhaseDelta[i] : 0,
    driveLock: i >= 0 ? DriveLock[i] : 0,
    omega: i >= 0 ? Omega[i] : 0,
    omegaPeriod: i >= 0 ? omegaToPeriod(Omega[i]) : NaN,
    nodeMemory: nodeMemoryMean(i),
    replayMem: i >= 0 ? ReplayMem[i] : 0,
    replayGain: i >= 0 ? ReplayGain[i] : 0,
    replayAdv: i >= 0 ? ReplayAdv[i] : 0,
    replayPeriod: i >= 0 ? omegaToPeriod(ReplayAdv[i]) : NaN,
  };
}
function getDebugSnapshot() {
  const pn=probeNode();
  const path=pathNodeIndices();
  const driveOmega=TWO_PI / Math.max(1, P.drivePer);
  return {
    cycleMode,
    cycleStepInPhase,
    cycleCount,
    day: isDay(),
    warmup: isWarmup(),
    driveEnv,
    drivePhase: currentDrivePhase(),
    driveOmega,
    drivePeriod: P.drivePer,
    corrValue,
    peakCorr,
    dwellSteps,
    bestDwell,
    input: getNodeDebug(inputNode),
    probe: getNodeDebug(pn),
    output: getNodeDebug(outputNode),
    path: {
      length: path.length,
      memoryMean: pathMemoryMean(),
      meanMag: meanBy(path, i => magnitudeAt(i)),
      meanPhaseDelta: meanBy(path, i => PhaseDelta[i]),
      meanDriveLock: meanBy(path, i => DriveLock[i]),
      meanOmega: meanBy(path, i => Omega[i]),
      meanReplayMem: meanBy(path, i => ReplayMem[i]),
      meanReplayGain: meanBy(path, i => ReplayGain[i]),
      meanReplayAdv: meanBy(path, i => ReplayAdv[i]),
    },
  };
}
function rms(data) { if (!data || data.length < 4) return 0; let s=0; for (const v of data) s+=v*v; return Math.sqrt(s/data.length); }
function estimatePeriod(data) {
  if (!data || data.length < 32) return NaN;
  let mean=0; for (const v of data) mean+=v; mean/=data.length;
  const crossings=[]; let prev=data[0]-mean;
  for (let i=1;i<data.length;i++) { const cur=data[i]-mean; if (prev < 0 && cur >= 0) crossings.push(i); prev=cur; }
  if (crossings.length < 3) return NaN;
  const gaps=[]; for (let i=1;i<crossings.length;i++) gaps.push(crossings[i]-crossings[i-1]);
  gaps.sort((a,b)=>a-b); return gaps[Math.floor(gaps.length/2)];
}
function fmtPeriod(v) { return Number.isFinite(v) ? Math.round(v).toString() : '—'; }

// Cross-correlation at lag 0 between two arrays
function crossCorr(a, b) {
  const n = Math.min(a.length, b.length, HIST_LEN);
  if (n < 4) return 0;
  let sa=0, sb=0, saa=0, sbb=0, sab=0;
  for (let i=0;i<n;i++) {
    sa+=a[i]; sb+=b[i];
    saa+=a[i]*a[i]; sbb+=b[i]*b[i];
    sab+=a[i]*b[i];
  }
  const ma=sa/n, mb=sb/n;
  let num=0, da=0, db=0;
  for (let i=0;i<n;i++) {
    num+=(a[i]-ma)*(b[i]-mb);
    da+=(a[i]-ma)**2;
    db+=(b[i]-mb)**2;
  }
  const denom=Math.sqrt(da*db);
  return denom<1e-10 ? 0 : num/denom;
}

// ── Drive — set once per step for input node only ────────────
// Complex rotating drive. Phase is continuous; amplitude envelope ramps day/night.
function computeDrive() {
  DRIVE_R.fill(0); DRIVE_I.fill(0);
  if (inputNode < 0) { driveEnv = 0; return; }

  // The oscillator phase is continuous across day/night. Only the envelope
  // opens/closes smoothly, so returning to day does not inject a hard step.
  const targetEnv = isDay() ? 1 : 0;
  if (targetEnv === 0) {
    // At night the external drive is truly off. No residual damping tail.
    driveEnv = 0;
  } else {
    // Day onset ramps in to avoid a hard injection discontinuity.
    const ramp = Math.max(1, P.driveRamp || 1);
    driveEnv += (1 - driveEnv) / ramp;
    if (Math.abs(driveEnv - 1) < 1e-4) driveEnv = 1;
  }

  const phase = currentDrivePhase();
  const amp = P.driveAmp * driveEnv;
  DRIVE_R[inputNode] = amp * Math.cos(phase);
  DRIVE_I[inputNode] = amp * Math.sin(phase);
}

// ── Field update — X every step ───────────────────────────────
const nb8=[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]];
function updateX() {
  for (let y=0;y<N;y++) {
    for (let x=0;x<N;x++) {
      const i=idx(x,y);
      let sumR=0, sumI=0, psR=0, psI=0, an=0;
      let alignR=0, alignI=0;
      let retR=0, retI=0, memW=0;
      const si=S[i];
      const ps=P.phi*si;
      const cosP=Math.cos(ps), sinP=Math.sin(ps);

      for (let e=0;e<nb8.length;e++) {
        const [dx,dy]=nb8[e];
        const j=idx(x+dx,y+dy);
        const se=Sedge[i*8+e];
        const wij=P.W*(1+P.edgeGain*se);
        const edgePhase=ps + P.phi*se;
        const cE=Math.cos(edgePhase), sE=Math.sin(edgePhase);
        const eR=(cE*Xr[j]-sE*Xi[j]);
        const eI=(sE*Xr[j]+cE*Xi[j]);
        sumR+=wij*eR;
        sumI+=wij*eI;
        retR+=se*eR;
        retI+=se*eI;
        memW+=se;

        // Direct phase/vector alignment. This is intentionally separate from W.
        // W carries amplitude by neighbor summation; kAlign actively pulls local phase
        // toward neighbor phase so a driven node can entrain its first hop instead of
        // only appearing as a tiny ripple on a slow ambient mode.
        const mi=Math.sqrt(Xr[i]*Xr[i]+Xi[i]*Xi[i]);
        const mj=Math.sqrt(Xr[j]*Xr[j]+Xi[j]*Xi[j]);
        if (mj>1e-6) {
          const uiR = mi>1e-6 ? Xr[i]/mi : 1.0;
          const uiI = mi>1e-6 ? Xi[i]/mi : 0.0;
          const ujR = Xr[j]/mj, ujI = Xi[j]/mj;
          const sinD = uiR*ujI - uiI*ujR; // sin(phi_j - phi_i)
          const amp = Math.max(mi, 0.05);
          // Kuramoto tangent plus a small vector pull for near-zero passive nodes.
          alignR += (sinD * -uiI * amp + 0.35*(Xr[j]-Xr[i])) * (1+se);
          alignI += (sinD *  uiR * amp + 0.35*(Xi[j]-Xi[i])) * (1+se);
        }

        const m=mj;
        if (m>1e-6) { psR+=Xr[j]/m; psI+=Xi[j]/m; }
        an++;
      }
      // v6: no neighbor-count normalization; W is per-connection strength.

      // Triadic remainder
      let triRem=0;
      if (P.triWeight>0) {
        const j1=idx(x+1,y),j2=idx(x,y+1),j3=idx(x+1,y+1);
        const p0=Math.atan2(Xi[i],Xr[i]);
        const p1=Math.atan2(Xi[j1],Xr[j1]);
        const p2=Math.atan2(Xi[j2],Xr[j2]);
        const p3=Math.atan2(Xi[j3],Xr[j3]);
        const l1=Math.abs(((p1-p0)+(p2-p1)+(p0-p2)+Math.PI)%TWO_PI-Math.PI);
        const l2=Math.abs(((p3-p1)+(p2-p3)+(p1-p2)+Math.PI)%TWO_PI-Math.PI);
        triRem=(l1+l2)/TWO_PI;
      }

      const coh=Math.sqrt(psR*psR+psI*psI)/Math.max(an,1);
      C[i]=coh;
      R[i]=0.55*(1-coh)+0.45*triRem;

      // Coherence history — two timescales
      ChF[i]=0.85*ChF[i]+0.15*coh;
      ChS[i]=0.99*ChS[i]+0.01*coh;

      let al=AL[i]; const bl=BL[i];

      // At night, learned memory should reduce damping continuously.
      // Without this, phase inertia only rotates a vector that rapidly shrinks to invisibility.
      const memNode = (!isDay() && !isWarmup()) ? nodeMemoryMean(i) : 0;
      if (memNode > 0) al = Math.min(0.999, al + P.persistAlpha * P.retain * memNode);

      // Self-excitation — allows field to sustain non-zero equilibrium
      // Without this the field decays to zero and cannot propagate anything
      const selfBoost = P.selfEx * coh;

      // X update — drive is just a float added here
      // The field does not know what generated DRIVE_R/I
      const alignScale = an>0 ? P.kAlign/an : 0;
      // v7 memory: learned edges provide a weak recurrent push at night.
      // During day the external drive dominates; at night only existing Sedge can sustain/replay flow.
      const retainScale = (!isDay() && !isWarmup()) ? P.retain : 0;
      let nr=al*Xr[i]+sumR*(1+selfBoost)+alignScale*alignR+retainScale*retR-bl*R[i]*Xr[i]+DRIVE_R[i];
      let ni=al*Xi[i]+sumI*(1+selfBoost)+alignScale*alignI+retainScale*retI-bl*R[i]*Xi[i]+DRIVE_I[i];
      let replayMem=0, replayGain=0, adv=0;

      // v7 patch: dynamic memory, not a hard mask. During night, learned edge
      // strength continuously weights a learned local phase velocity. This lets
      // remembered structure keep rotating weakly instead of only staying saturated.
      if (!isDay() && !isWarmup()) {
        const memAvg = Math.max(nodeMemoryMean(i), an>0 ? memW/an : 0);
        replayMem = memAvg;
        replayGain = P.phaseInertia * P.retain * memAvg;
        adv = replayGain * Omega[i];
        if (Math.abs(adv) > 1e-6) {
          const ca=Math.cos(adv), sa=Math.sin(adv);
          const tr=nr, ti=ni;
          nr = ca*tr - sa*ti;
          ni = sa*tr + ca*ti;
        }
      }
      ReplayMem[i]=replayMem;
      ReplayGain[i]=replayGain;
      ReplayAdv[i]=adv;

      // Diagnostic boundary condition: during day, the input node is phase-clamped
      // to the external rotating drive. This separates true drive-frequency
      // propagation from the field's slower endogenous background modes.
      if (i===inputNode && isDay()) {
        nr = 0.15*nr + 0.85*DRIVE_R[i];
        ni = 0.15*ni + 0.85*DRIVE_I[i];
      }

      const m2=nr*nr+ni*ni;
      if (m2>4.0) { const sc=2.0/Math.sqrt(m2); nr*=sc; ni*=sc; }
      Xr2[i]=nr; Xi2[i]=ni;
    }
  }
  // Swap X
  let t;
  t=Xr;Xr=Xr2;Xr2=t;
  t=Xi;Xi=Xi2;Xi2=t;
}


// Learned phase velocity — every step, continuous and local.
function updatePhaseMemory() {
  const train = isDay() && !isWarmup();
  const dph = currentDrivePhase();
  const learn = Math.max(0, P.omegaLearn || 0);
  const forgetNight = 0.002;
  for (let i=0;i<N*N;i++) {
    const ph=Math.atan2(Xi[i],Xr[i]);
    const d=angleDiff(ph, PrevPhi[i]);
    PhaseDelta[i]=d;
    PrevPhi[i]=ph;
    const amp=Math.sqrt(Xr[i]*Xr[i]+Xi[i]*Xi[i]);
    const mem=nodeMemoryMean(i);
    const driveLock = amp>1e-6 ? (Xr[i]*Math.cos(dph)+Xi[i]*Math.sin(dph))/Math.max(amp,1e-6) : 0;
    DriveLock[i]=driveLock;
    if (train && amp>1e-5) {
      // Prefer phase velocity learned from drive-locked, memory-bearing regions.
      // Blend observed local phase advance with the known entraining drive advance;
      // the blend is still gated by actual local amplitude/lock, so non-entrained regions do not learn it.
      const gate=Math.min(1, amp/0.12) * Math.max(Math.abs(driveLock), mem);
      const driveOmega = TWO_PI / Math.max(1, P.drivePer);
      const targetOmega = 0.55*d + 0.45*driveOmega;
      Omega[i]=(1-learn*gate)*Omega[i] + (learn*gate)*targetOmega;
    } else if (!isWarmup()) {
      Omega[i]*=(1-forgetNight);
    }
  }
}

// ── S update — every 10 steps ─────────────────────────────────
function updateS() {
  for (let y=0;y<N;y++) {
    for (let x=0;x<N;x++) {
      const i=idx(x,y);
      let maxC=0, maxS=S[i];
      for (const [dx,dy] of [[-1,0],[1,0],[0,-1],[0,1]]) {
        const j=idx(x+dx,y+dy);
        if (C[j]>maxC) { maxC=C[j]; maxS=S[j]; }
      }
      S2[i]=Math.max(0.001,Math.min(1.0,
        (1-P.epsilon)*S[i]+P.epsilon*(C[i]-R[i])+0.02*(maxS-S[i])
      ));
    }
  }
  let t=S;S=S2;S2=t;
}

// Edge memory — every 10 steps with S. Local Hebbian-style reinforcement.
function updateSedge() {
  // v7: edge memory learns only from successful driven daytime propagation.
  // It is not allowed to train during warmup or night, which prevents ambient modes
  // from becoming the memory trace.
  const forgetting = P.edgeDecay || 0;
  const train = isDay() && !isWarmup() && P.epsilon > 0;
  const dph=currentDrivePhase();
  const anneal = 1 / (1 + cycleCount * 0.12);

  for (let y=0;y<N;y++) {
    for (let x=0;x<N;x++) {
      const i=idx(x,y);
      const pi=Math.atan2(Xi[i],Xr[i]);
      const ai=Math.sqrt(Xr[i]*Xr[i]+Xi[i]*Xi[i]);
      const driveI = ai>1e-6 ? Math.abs((Xr[i]*Math.cos(dph)+Xi[i]*Math.sin(dph))/ai) : 0;

      for (let e=0;e<nb8.length;e++) {
        const [dx,dy]=nb8[e];
        const j=idx(x+dx,y+dy);
        const pj=Math.atan2(Xi[j],Xr[j]);
        const aj=Math.sqrt(Xr[j]*Xr[j]+Xi[j]*Xi[j]);
        const old=Sedge[i*8+e];

        let next = old * (1 - forgetting);
        if (train) {
          const coh01=0.5*(Math.cos(pj-pi)+1.0);
          const driveJ = aj>1e-6 ? Math.abs((Xr[j]*Math.cos(dph)+Xi[j]*Math.sin(dph))/aj) : 0;
          const ampGate = Math.min(1, (ai*aj) / 0.04); // only reinforce edges carrying real signal
          const driveGate = driveI * driveJ * ampGate;
          const rem=(1-coh01)+0.10*Math.abs(ai-aj);
          const plastic=P.epsilon*anneal*(1-old)*driveGate;
          next += plastic*(coh01-rem-0.03*old);
        }
        Sedge[i*8+e]=Math.max(0,Math.min(1,next));
      }
    }
  }
}
// ── α/β homeostasis — every 100 steps ────────────────────────
function updateHomeostasis() {
  for (let i=0;i<N*N;i++) {
    const fastErr=ChF[i]-P.tauC;
    const slowErr=ChS[i]-P.tauC;
    // Only act when fast and slow agree — not a transient
    if (fastErr*slowErr>0) {
      const err=fastErr;
      const etaEff=P.eta*(1+5*err*err); // adaptive — stronger when far from target
      AL[i]=Math.max(0.88,Math.min(0.995,AL[i]-etaEff*err*0.5));
      BL[i]=Math.max(0.02,Math.min(0.5, BL[i]+etaEff*err*1.0));
    }
  }
}

// ── Main update ───────────────────────────────────────────────
function update() {
  computeDrive();   // set complex drive buffer — input node only, day only
  updateX();        // every step
  updatePhaseMemory(); // every step: learn/replay phase velocity state

  if (step%10  ===0) { updateS(); updateSedge(); } // every 10
  if (step%100 ===0) updateHomeostasis();  // every 100

  advanceCycle();

  // Record traces. The visible input plot is the external drive, not the input node's internal oscillator.
  // This avoids a false impression that the drive remains on at night.
  if (inputNode>=0) {
    const driveV=DRIVE_R[inputNode];
    inputHistory.push(driveV);
    if (inputHistory.length>HIST_LEN) inputHistory.shift();

    const iv=phaseTrace(inputNode);
    inputNodeHistory.push(iv);
    if (inputNodeHistory.length>HIST_LEN) inputNodeHistory.shift();
  }
  if (outputNode>=0) {
    const pn=probeNode();
    const pv=pn>=0 ? outputRawTrace(pn) : 0;
    probeHistory.push(pv);
    if (probeHistory.length>HIST_LEN) probeHistory.shift();
    const ov=outputRawTrace(outputNode);
    const lv=driveLockedTrace(outputNode);
    outputHistory.push(ov);
    if (outputHistory.length>HIST_LEN) outputHistory.shift();
    outputLockHistory.push(lv);
    if (outputLockHistory.length>HIST_LEN) outputLockHistory.shift();
    if (isDay() && !isWarmup()) {
      outputDayHistory.push(ov);
      if (outputDayHistory.length>HIST_LEN) outputDayHistory.shift();
    } else if (!isDay() && !isWarmup()) {
      outputNightHistory.push(ov);
      if (outputNightHistory.length>HIST_LEN) outputNightHistory.shift();
    }
  }

  // Measure memory during night: output-day pattern vs output-night pattern.
  if (!isDay() && !isWarmup() && outputNode>=0) {
    corrValue=crossCorr(outputDayHistory, outputNightHistory);
    peakCorr=Math.max(peakCorr, corrValue);
    if (corrValue>P.corrThr) {
      dwellSteps++;
      bestDwell=Math.max(bestDwell, dwellSteps);
    } else {
      dwellSteps=0;
    }
  }

  step++;
}

// ── Rendering ─────────────────────────────────────────────────
