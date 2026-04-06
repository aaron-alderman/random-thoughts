// ── HERO CANVAS ─────────────────────────────────────
(function() {
  const canvas = document.getElementById('heroCanvas');
  const ctx = canvas.getContext('2d');
  let W, H, pts = [], t = 0;

  function resize() {
    W = canvas.width = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
    pts = [];
    // Generate muqarnas-like points in a dome pattern
    for (let r = 0; r < 12; r++) {
      const n = Math.max(1, Math.round(6 * r));
      for (let i = 0; i < n; i++) {
        const angle = (2 * Math.PI * i) / n;
        const radius = (r / 11) * Math.min(W, H) * 0.42;
        pts.push({
          x: W/2 + radius * Math.cos(angle),
          y: H/2 + radius * Math.sin(angle),
          r: r, n: n, i: i,
          phase: Math.random() * Math.PI * 2,
          speed: 0.003 + Math.random() * 0.004
        });
      }
    }
  }

  function draw() {
    t += 0.008;
    ctx.clearRect(0, 0, W, H);

    // Background gradient
    const bg = ctx.createRadialGradient(W/2, H/2, 0, W/2, H/2, Math.max(W,H)*0.6);
    bg.addColorStop(0, '#0d1520');
    bg.addColorStop(1, '#080a0e');
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, W, H);

    // Draw connections
    for (let i = 0; i < pts.length; i++) {
      for (let j = i+1; j < pts.length; j++) {
        const p = pts[i], q = pts[j];
        const dx = p.x - q.x, dy = p.y - q.y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        const threshold = Math.min(W,H) * 0.08;
        if (dist < threshold) {
          const alpha = (1 - dist/threshold) * 0.25;
          const phase = Math.sin(t + p.phase) * 0.5 + 0.5;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = `rgba(${Math.round(40+phase*160)},${Math.round(100+phase*80)},${Math.round(60+phase*40)},${alpha})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }

    // Draw nodes
    for (const p of pts) {
      const pulse = Math.sin(t * p.speed * 200 + p.phase) * 0.5 + 0.5;
      const isCenter = p.r === 0;
      const r = isCenter ? 4 : 1.5 + p.r * 0.15;
      ctx.beginPath();
      ctx.arc(p.x, p.y, r, 0, Math.PI*2);
      if (isCenter) {
        ctx.fillStyle = `rgba(200,146,42,${0.6 + pulse*0.4})`;
      } else {
        const alpha = 0.2 + pulse * 0.5 * (1 - p.r/11);
        ctx.fillStyle = `rgba(58,184,184,${alpha})`;
      }
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  resize();
  draw();
})();

// ── MUQARNAS CANVAS ─────────────────────────────────
(function() {
  const canvas = document.getElementById('muqarnasCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;

  function drawMuqarnas(n) {
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    const cx = W/2, cy = H * 0.65;
    const tiers = Math.min(n, 8);

    for (let tier = 0; tier < tiers; tier++) {
      const y = cy - tier * (H * 0.07);
      const w = W * 0.85 * (1 - tier/tiers * 0.7);
      const h = H * 0.065;
      const cells = Math.max(1, tiers - tier);
      const cw = w / cells;

      for (let c = 0; c < cells; c++) {
        const x = cx - w/2 + c * cw;
        const alpha = 0.3 + (tier/tiers) * 0.5;
        const lightness = 0.2 + (tier/tiers) * 0.4;

        // Cell face
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + cw, y);
        ctx.lineTo(x + cw * 0.85, y - h);
        ctx.lineTo(x + cw * 0.15, y - h);
        ctx.closePath();
        ctx.fillStyle = `rgba(${Math.round(30+lightness*80)},${Math.round(50+lightness*60)},${Math.round(80+lightness*40)},${alpha})`;
        ctx.fill();
        ctx.strokeStyle = `rgba(200,146,42,${0.3 + tier/tiers * 0.4})`;
        ctx.lineWidth = 0.5;
        ctx.stroke();

        // Niche detail
        if (cw > 20) {
          ctx.beginPath();
          ctx.arc(x + cw/2, y - h * 0.3, cw * 0.15, Math.PI, 0);
          ctx.strokeStyle = `rgba(58,184,184,${0.3 + tier/tiers * 0.3})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    // Apex glow
    const g = ctx.createRadialGradient(cx, cy - tiers * H * 0.07, 0, cx, cy - tiers * H * 0.07, 30);
    g.addColorStop(0, 'rgba(200,146,42,0.4)');
    g.addColorStop(1, 'rgba(200,146,42,0)');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);
  }

  let frame = 0, n = 1;
  function animate() {
    frame++;
    if (frame % 50 === 0 && n < 9) n++;
    if (n >= 9 && frame % 200 === 0) n = 1;
    drawMuqarnas(n);
    requestAnimationFrame(animate);
  }
  animate();
})();

// ── PERCEPTION CANVAS ───────────────────────────────
(function() {
  const canvas = document.getElementById('perceptionCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;

  let res = 2, increasing = true, t = 0;

  function draw() {
    t++;
    if (t % 30 === 0) {
      if (increasing) { res = Math.min(res + 1, 32); if (res >= 32) increasing = false; }
      else { res = Math.max(res - 1, 2); if (res <= 2) increasing = true; }
    }

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    const cellW = W / res;
    const cellH = H / res;

    for (let x = 0; x < res; x++) {
      for (let y = 0; y < res; y++) {
        const cx = (x + 0.5) / res;
        const cy = (y + 0.5) / res;
        const d = Math.sqrt((cx-0.5)**2 + (cy-0.5)**2) * 2;
        const angle = Math.atan2(cy-0.5, cx-0.5);
        const v = Math.sin(d * 6 + angle * 2) * 0.5 + 0.5;
        const r = Math.round(20 + v * 40);
        const g = Math.round(50 + v * 80);
        const b = Math.round(80 + v * 100);
        ctx.fillStyle = `rgb(${r},${g},${b})`;
        ctx.fillRect(x * cellW, y * cellH, cellW - 0.5, cellH - 0.5);
      }
    }

    // Resolution label
    ctx.fillStyle = 'rgba(200,146,42,0.8)';
    ctx.font = '10px JetBrains Mono, monospace';
    ctx.fillText(`${res}×${res}`, 8, 18);

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── SYMMETRY CANVAS ─────────────────────────────────
(function() {
  const canvas = document.getElementById('symmetryCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  const cx = W/2, cy = H/2;

  let n = 4, t = 0;

  function draw() {
    t++;
    if (t % 80 === 0) {
      n = n < 64 ? n * 2 : 4;
    }

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    const R = 90;

    // Draw symmetry lines
    for (let i = 0; i < n; i++) {
      const angle = (2 * Math.PI * i) / n;
      const x = cx + R * Math.cos(angle);
      const y = cy + R * Math.sin(angle);

      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(x, y);
      const alpha = Math.min(0.8, 8/n);
      ctx.strokeStyle = `rgba(58,184,184,${alpha})`;
      ctx.lineWidth = 1;
      ctx.stroke();

      // Node on circle
      ctx.beginPath();
      ctx.arc(x, y, Math.max(1, 4 - Math.log2(n)), 0, Math.PI*2);
      ctx.fillStyle = `rgba(200,146,42,${alpha * 1.5})`;
      ctx.fill();
    }

    // Outer circle
    ctx.beginPath();
    ctx.arc(cx, cy, R, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba(200,146,42,0.3)';
    ctx.lineWidth = 0.5;
    ctx.stroke();

    // Center
    ctx.beginPath();
    ctx.arc(cx, cy, 3, 0, Math.PI*2);
    ctx.fillStyle = 'rgba(200,146,42,0.9)';
    ctx.fill();

    // Label
    ctx.fillStyle = 'rgba(200,146,42,0.7)';
    ctx.font = '10px JetBrains Mono, monospace';
    ctx.fillText(n < 64 ? `D${n}` : 'SO(2)', 8, 18);

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── ORIENTATION CANVAS ──────────────────────────────
(function() {
  const canvas = document.getElementById('orientCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  let t = 0;

  function draw() {
    t += 0.02;
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    // Bottom half: grid (position)
    ctx.save();
    ctx.beginPath();
    ctx.rect(0, H/2, W, H/2);
    ctx.clip();
    const step = 20;
    for (let x = 0; x < W; x += step) {
      for (let y = H/2; y < H; y += step) {
        ctx.beginPath();
        ctx.arc(x, y, 1.5, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(58,184,184,0.4)';
        ctx.fill();
      }
    }
    ctx.restore();

    // Top half: orientation field
    ctx.save();
    ctx.beginPath();
    ctx.rect(0, 0, W, H/2);
    ctx.clip();
    const cx = W/2, cy = H/2;
    const gstep = 24;
    for (let x = gstep/2; x < W; x += gstep) {
      for (let y = gstep/2; y < H/2; y += gstep) {
        const angle = Math.atan2(y - cy, x - cx) + t * 0.3;
        const len = 10;
        const ex = x + Math.cos(angle) * len;
        const ey = y + Math.sin(angle) * len;
        const d = Math.sqrt((x-cx)**2 + (y-cy)**2) / (Math.min(W,H)*0.5);
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(ex, ey);
        ctx.strokeStyle = `rgba(200,146,42,${0.6 - d*0.3})`;
        ctx.lineWidth = 1.2;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(x, y, 1.5, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(200,146,42,0.5)';
        ctx.fill();
      }
    }
    ctx.restore();

    // Dividing line
    ctx.beginPath();
    ctx.moveTo(0, H/2);
    ctx.lineTo(W, H/2);
    ctx.strokeStyle = 'rgba(200,146,42,0.4)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Labels
    ctx.fillStyle = 'rgba(58,184,184,0.6)';
    ctx.font = '9px JetBrains Mono, monospace';
    ctx.fillText('(x,y) position', 8, H - 10);
    ctx.fillStyle = 'rgba(200,146,42,0.6)';
    ctx.fillText('SO(2) orientation', 8, H/2 - 8);

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── QUATERNION CANVAS ───────────────────────────────
(function() {
  const canvas = document.getElementById('quatCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  const cx = W/2, cy = H/2;
  let t = 0;

  function draw() {
    t += 0.015;
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    // Draw S³ projection as concentric rotating rings
    const rings = 6;
    for (let r = 0; r < rings; r++) {
      const radius = 20 + r * 15;
      const phase = t * (1 + r * 0.2);
      const alpha = 0.15 + (r/rings) * 0.3;

      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, Math.PI*2);
      ctx.strokeStyle = `rgba(58,184,184,${alpha})`;
      ctx.lineWidth = 0.8;
      ctx.stroke();

      // Rotating point on ring
      const px = cx + radius * Math.cos(phase);
      const py = cy + radius * Math.sin(phase);
      ctx.beginPath();
      ctx.arc(px, py, 2.5, 0, Math.PI*2);
      ctx.fillStyle = `rgba(200,146,42,${0.5 + (r/rings)*0.5})`;
      ctx.fill();
    }

    // Unit sphere circle (normalized)
    ctx.beginPath();
    ctx.arc(cx, cy, 90, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba(200,146,42,0.5)';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.stroke();
    ctx.setLineDash([]);

    // |q| arrow collapsing to unit
    const scale = 0.6 + 0.4 * Math.abs(Math.sin(t * 0.5));
    const qx = cx + 90 * scale * Math.cos(t);
    const qy = cy + 90 * scale * Math.sin(t);
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(qx, qy);
    ctx.strokeStyle = `rgba(200,146,42,0.7)`;
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(qx, qy, 4, 0, Math.PI*2);
    ctx.fillStyle = 'rgba(200,146,42,0.9)';
    ctx.fill();

    // Labels
    ctx.fillStyle = 'rgba(200,146,42,0.6)';
    ctx.font = '9px JetBrains Mono, monospace';
    ctx.fillText('SU(2)', cx + 92, cy - 5);
    ctx.fillStyle = 'rgba(200,146,42,0.4)';
    ctx.fillText('q/|q|', 8, 18);

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── OCTONION CANVAS ─────────────────────────────────
(function() {
  const canvas = document.getElementById('octCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  const cx = W/2, cy = H/2;
  let t = 0, highlighted = -1;

  // 7 imaginary units arranged in circle
  const pts = [];
  for (let i = 0; i < 7; i++) {
    const angle = (2*Math.PI*i/7) - Math.PI/2;
    pts.push({ x: cx + 80*Math.cos(angle), y: cy + 80*Math.sin(angle), label: `e${i+1}` });
  }

  // Fano plane triples
  const triples = [
    [0,1,3],[1,2,4],[2,3,5],[3,4,6],[4,5,0],[5,6,1],[6,0,2]
  ];

  function draw() {
    t += 0.01;
    if (Math.floor(t * 0.3) !== Math.floor((t-0.01) * 0.3)) {
      highlighted = Math.floor(Math.random() * 7);
    }

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    // Draw triples as triangles
    triples.forEach((triple, idx) => {
      const isHit = triple.includes(highlighted);
      const alpha = isHit ? 0.3 : 0.08;
      ctx.beginPath();
      ctx.moveTo(pts[triple[0]].x, pts[triple[0]].y);
      ctx.lineTo(pts[triple[1]].x, pts[triple[1]].y);
      ctx.lineTo(pts[triple[2]].x, pts[triple[2]].y);
      ctx.closePath();
      ctx.fillStyle = `rgba(58,184,184,${alpha})`;
      ctx.fill();
      ctx.strokeStyle = `rgba(58,184,184,${alpha * 3})`;
      ctx.lineWidth = 0.8;
      ctx.stroke();
    });

    // Draw nodes
    pts.forEach((p, i) => {
      const isHit = i === highlighted;
      const pulse = Math.sin(t * 3 + i) * 0.5 + 0.5;
      ctx.beginPath();
      ctx.arc(p.x, p.y, isHit ? 7 : 4, 0, Math.PI*2);
      ctx.fillStyle = isHit ? 'rgba(200,146,42,0.9)' : `rgba(58,184,184,${0.4 + pulse*0.3})`;
      ctx.fill();
      ctx.fillStyle = 'rgba(200,200,200,0.7)';
      ctx.font = '8px JetBrains Mono, monospace';
      ctx.fillText(p.label, p.x - 8, p.y - 8);
    });

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── FANO CANVAS ─────────────────────────────────────
(function() {
  const canvas = document.getElementById('fanoCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  const cx = W/2, cy = H/2;
  let t = 0, activeTriple = 0;

  // 6 outer + 1 center
  const outer = [];
  for (let i = 0; i < 6; i++) {
    const a = (2*Math.PI*i/6) - Math.PI/2;
    outer.push({ x: cx + 85*Math.cos(a), y: cy + 85*Math.sin(a) });
  }
  const center = { x: cx, y: cy };
  const allPts = [...outer, center]; // 0-5 outer, 6 center

  // 7 lines of Fano plane (adapted to 7 points)
  const fanoLines = [
    [0,1,6],[1,2,6],[2,3,6],[3,4,6],[4,5,6],[5,0,6],[0,2,4]
  ];

  function draw() {
    t += 0.008;
    if (Math.floor(t * 0.4) !== Math.floor((t-0.008)*0.4)) {
      activeTriple = (activeTriple + 1) % fanoLines.length;
    }

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    // Outer circle
    ctx.beginPath();
    ctx.arc(cx, cy, 85, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba(42,138,138,0.15)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Inner incircle
    ctx.beginPath();
    ctx.arc(cx, cy, 42, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba(42,138,138,0.1)';
    ctx.lineWidth = 0.5;
    ctx.stroke();

    // Draw all lines
    fanoLines.forEach((line, idx) => {
      const isActive = idx === activeTriple;
      ctx.beginPath();
      if (line.includes(6)) {
        // Lines through center: draw as segments
        const a = allPts[line[0] === 6 ? line[1] : line[0]];
        const b = allPts[line[2] === 6 ? line[1] : line[2]];
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(cx, cy);
        ctx.lineTo(b.x, b.y);
      } else {
        // Triangle
        ctx.moveTo(allPts[line[0]].x, allPts[line[0]].y);
        ctx.lineTo(allPts[line[1]].x, allPts[line[1]].y);
        ctx.lineTo(allPts[line[2]].x, allPts[line[2]].y);
        ctx.closePath();
      }
      ctx.strokeStyle = isActive ? 'rgba(200,146,42,0.8)' : 'rgba(58,184,184,0.2)';
      ctx.lineWidth = isActive ? 1.5 : 0.8;
      ctx.stroke();
      if (isActive && !line.includes(6)) {
        ctx.fillStyle = 'rgba(200,146,42,0.08)';
        ctx.fill();
      }
    });

    // Draw points
    allPts.forEach((p, i) => {
      const isInActive = fanoLines[activeTriple].includes(i);
      const isCenter = i === 6;
      ctx.beginPath();
      ctx.arc(p.x, p.y, isCenter ? 6 : isInActive ? 6 : 4, 0, Math.PI*2);
      ctx.fillStyle = isCenter
        ? 'rgba(200,146,42,0.9)'
        : isInActive
          ? 'rgba(200,146,42,0.8)'
          : 'rgba(58,184,184,0.5)';
      ctx.fill();

      ctx.fillStyle = 'rgba(200,200,200,0.6)';
      ctx.font = '9px JetBrains Mono, monospace';
      const lx = i === 6 ? p.x + 9 : p.x + (p.x-cx)/Math.abs(p.x-cx||1)*9;
      const ly = i === 6 ? p.y : p.y + (p.y-cy)/Math.abs(p.y-cy||1)*9;
      ctx.fillText(i === 6 ? 'e₇' : `e${i+1}`, lx-6, ly+3);
    });

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── G2 CANVAS ───────────────────────────────────────
(function() {
  const canvas = document.getElementById('g2Canvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  const cx = W/2, cy = H/2;
  let t = 0;

  function draw() {
    t += 0.012;
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    // G2 acts on R7 - show as rotating structure in projection
    const layers = 7;
    for (let l = 0; l < layers; l++) {
      const angle0 = (2*Math.PI*l/layers) + t * (l%2===0 ? 1 : -1) * 0.2;
      const R = 30 + l*9;

      ctx.beginPath();
      const pts2 = [];
      for (let i = 0; i <= 7; i++) {
        const a = angle0 + (2*Math.PI*i/7);
        pts2.push([cx + R*Math.cos(a), cy + R*Math.sin(a)]);
      }
      ctx.moveTo(pts2[0][0], pts2[0][1]);
      for (let i = 1; i < pts2.length; i++) ctx.lineTo(pts2[i][0], pts2[i][1]);
      ctx.closePath();
      const alpha = 0.08 + (l/layers)*0.15;
      ctx.strokeStyle = `rgba(58,184,184,${alpha})`;
      ctx.lineWidth = 0.8;
      ctx.stroke();
    }

    // The preserved 3-form phi as 3 interlocking rings
    for (let i = 0; i < 3; i++) {
      const a = (2*Math.PI*i/3) + t * 0.15;
      const rx = cx + 25*Math.cos(a);
      const ry = cy + 25*Math.sin(a);
      ctx.beginPath();
      ctx.arc(rx, ry, 35, 0, Math.PI*2);
      ctx.strokeStyle = `rgba(200,146,42,0.25)`;
      ctx.lineWidth = 1.2;
      ctx.stroke();
    }

    // Central invariant point
    const glow = ctx.createRadialGradient(cx, cy, 0, cx, cy, 20);
    glow.addColorStop(0, 'rgba(200,146,42,0.6)');
    glow.addColorStop(1, 'rgba(200,146,42,0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H);

    ctx.beginPath();
    ctx.arc(cx, cy, 5, 0, Math.PI*2);
    ctx.fillStyle = 'rgba(200,146,42,1)';
    ctx.fill();

    // Label
    ctx.fillStyle = 'rgba(200,146,42,0.7)';
    ctx.font = 'bold 14px Cinzel, serif';
    ctx.fillText('G₂', 8, 20);
    ctx.fillStyle = 'rgba(58,184,184,0.5)';
    ctx.font = '9px JetBrains Mono, monospace';
    ctx.fillText('dim = 14', 8, 34);

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── BRIDGE CANVAS ───────────────────────────────────
(function() {
  const canvas = document.getElementById('bridgeCanvas');
  const ctx = canvas.getContext('2d');
  const W = 240, H = 240;
  const cx = W/2, cy = H/2;
  let t = 0;

  function draw() {
    t += 0.01;
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1117';
    ctx.fillRect(0, 0, W, H);

    // Left: algebra side (discrete dots)
    const dotGrid = 5;
    const spacing = 28;
    const startX = 20, startY = 60;
    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 3; j++) {
        const x = startX + i * spacing * 0.8;
        const y = startY + j * spacing;
        const pulse = Math.sin(t*2 + i + j) * 0.5 + 0.5;
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, Math.PI*2);
        ctx.fillStyle = `rgba(58,184,184,${0.3+pulse*0.5})`;
        ctx.fill();
      }
    }

    // Right: geometry side (smooth arc)
    ctx.beginPath();
    for (let a = -Math.PI*0.6; a <= Math.PI*0.6; a += 0.05) {
      const R = 60;
      const x = W - 70 + R * Math.cos(a) * 0.3;
      const y = cy + R * Math.sin(a);
      if (a === -Math.PI*0.6) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.strokeStyle = 'rgba(200,146,42,0.6)';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Bridge arc connecting the two
    const bridgeY = cy;
    const x1 = 110, x2 = 155;
    ctx.beginPath();
    ctx.moveTo(x1, bridgeY - 20);
    ctx.bezierCurveTo(x1 + 15, bridgeY - 45, x2 - 15, bridgeY - 45, x2, bridgeY - 20);
    ctx.strokeStyle = 'rgba(200,146,42,0.4)';
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.beginPath();
    ctx.moveTo(x1, bridgeY + 20);
    ctx.bezierCurveTo(x1 + 15, bridgeY + 45, x2 - 15, bridgeY + 45, x2, bridgeY + 20);
    ctx.strokeStyle = 'rgba(58,184,184,0.4)';
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.stroke();
    ctx.setLineDash([]);

    // Phi symbol in bridge
    const phaseX = (x1+x2)/2;
    const glow = ctx.createRadialGradient(phaseX, cy, 0, phaseX, cy, 25);
    glow.addColorStop(0, 'rgba(200,146,42,0.3)');
    glow.addColorStop(1, 'rgba(200,146,42,0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H);

    ctx.fillStyle = 'rgba(200,146,42,0.9)';
    ctx.font = 'italic 18px EB Garamond, serif';
    ctx.textAlign = 'center';
    ctx.fillText('φ', phaseX, cy + 6);
    ctx.textAlign = 'left';

    // Labels
    ctx.font = '9px JetBrains Mono, monospace';
    ctx.fillStyle = 'rgba(58,184,184,0.6)';
    ctx.fillText('algebra', 14, H - 10);
    ctx.fillStyle = 'rgba(200,146,42,0.6)';
    ctx.fillText('geometry', W - 70, H - 10);

    requestAnimationFrame(draw);
  }
  draw();
})();

// ── SCROLL REVEAL ────────────────────────────────────
const steps = document.querySelectorAll('.step');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
steps.forEach(s => revealObs.observe(s));

const others = document.querySelectorAll('.arc-wrap, .analogy, .ext-card, .bridge-header, .final, .extensions');
const genObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });
others.forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
  genObs.observe(el);
});
