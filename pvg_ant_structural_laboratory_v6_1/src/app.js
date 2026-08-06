// PVG–ANT Structural Laboratory v6.1 — comparison-layout UI.
import { factor, factText, firstPrimes } from './core/arithmetic.js';
import {
  directionsFor, smoothPoints, embed, distortion, coneChecks,
  CONE_THETA, REFERENCE_AXIS
} from './layout.js';

const $ = s => document.querySelector(s);
const cvs = $('#lattice'), ctx = cvs.getContext('2d');
const fmtN = n => n.toLocaleString('en-US');
const fmtR = (v, d = 4) => Number.isFinite(v) ? v.toFixed(d) : '—';

const state = {
  mode: 'cone', k: 9, N: 5000, sampleMode: 'logstrat',
  yaw: 0.5, pitch: -0.32, zoom: 1, auto: true, labels: 0, sel: -1,
  W: 1, H: 1, dpr: 1
};

let scene = null; // {primes, logP, points:[{n,exps,X,cat,color}], M, baseScale, distLegacy, distCone}

function axisColor(idx, k){ return `hsl(${Math.round(360 * idx / k)}, 68%, 52%)`; }

function categorize(exps){
  let om = 0, Om = 0, idx = -1, mx = 0;
  for (let t = 0; t < exps.length; t++) { const e = exps[t]; if (e > 0) { om++; idx = t; } Om += e; if (e > mx) mx = e; }
  if (Om === 0) return { cat: 'one', idx: -1 };
  if (Om === 1) return { cat: 'atom', idx };
  if (om === 1) return { cat: 'ppow', idx };
  if (mx <= 1) return { cat: 'sqfree', idx: -1 };
  return { cat: 'comp', idx: -1 };
}

function build(){
  const primes = firstPrimes(state.k);
  const { points, logP, aborted } = smoothPoints(primes, state.N, 2_000_000);
  const dirsLegacy = directionsFor('legacy', primes);
  const dirsCone = directionsFor('cone', primes);
  const dirs = state.mode === 'cone' ? dirsCone : dirsLegacy;

  let M = { x: 0, y: 0, z: 0 };
  const pts = points.map(p => {
    const X = embed(p.exps, primes, logP, dirs);
    const { cat, idx } = categorize(p.exps);
    M.x += X.x; M.y += X.y; M.z += X.z;
    let color;
    if (cat === 'atom' || cat === 'ppow') color = axisColor(idx, primes.length);
    else if (cat === 'sqfree') color = '#f2a13a';
    else if (cat === 'comp') color = '#9aa0a8';
    else color = '#888';
    return { n: p.n, exps: p.exps, X, cat, color };
  });
  const c = pts.length || 1;
  M = { x: M.x / c, y: M.y / c, z: M.z / c };
  let mR = 1e-3, yLo = Infinity, yHi = -Infinity;
  for (const p of pts) {
    const d = Math.hypot(p.X.x - M.x, p.X.y - M.y, p.X.z - M.z);
    if (d > mR) mR = d;
    if (p.X.y < yLo) yLo = p.X.y; if (p.X.y > yHi) yHi = p.X.y;
  }
  const baseScale = 0.42 * Math.min(state.W, state.H) / mR;

  const distLegacy = distortion(points, primes, logP, dirsLegacy, { cap: 400, sample: state.sampleMode });
  const distCone = distortion(points, primes, logP, dirsCone, { cap: 400, sample: state.sampleMode });

  scene = { primes, logP, points: pts, M, mR, baseScale, yLo, yHi, distLegacy, distCone, aborted };
  state.sel = -1;
  renderPanels();
  updHover();
  draw();
}

function proj(X){
  const M = scene.M;
  let x = X.x - M.x, y = X.y - M.y, z = X.z - M.z;
  const cY = Math.cos(state.yaw), sY = Math.sin(state.yaw);
  const x1 = x * cY + z * sY, z1 = -x * sY + z * cY;
  const cP = Math.cos(state.pitch), sP = Math.sin(state.pitch);
  const y2 = y * cP - z1 * sP, z2 = y * sP + z1 * cP;
  const sc = scene.baseScale * state.zoom;
  return { sx: state.W / 2 + x1 * sc, sy: state.H / 2 - y2 * sc, depth: z2 };
}

function line(A, B, col, w, dash){
  ctx.save(); ctx.strokeStyle = col; ctx.lineWidth = w; ctx.setLineDash(dash || []);
  ctx.beginPath(); ctx.moveTo(A.sx, A.sy); ctx.lineTo(B.sx, B.sy); ctx.stroke(); ctx.restore();
}
function label(s, x, y, col, f){
  ctx.save(); ctx.font = `${f || 12}px system-ui, sans-serif`;
  ctx.lineWidth = 3; ctx.strokeStyle = getCSS('--panel'); ctx.lineJoin = 'round';
  ctx.strokeText(s, x, y); ctx.fillStyle = col; ctx.fillText(s, x, y); ctx.restore();
}
function getCSS(v){ return getComputedStyle(document.documentElement).getPropertyValue(v).trim() || '#fff'; }

function draw(){
  if (!scene) return;
  ctx.clearRect(0, 0, state.W, state.H);
  const primes = scene.primes;
  const txt = getCSS('--text'), muted = getCSS('--muted');

  // visual reference axis (cone mode) — labelled explicitly as visual only.
  if (state.mode === 'cone') {
    const a = proj({ x: 0, y: scene.yHi + 0.4, z: 0 }), b = proj({ x: 0, y: scene.yLo - 0.3, z: 0 });
    line(b, a, muted, 1.4, [6, 5]);
    label('محور مرجعيّ بصريّ ↑ (الحجم/log n)', a.sx + 6, a.sy + 2, muted, 12);
  }

  // prime axis rays
  const O = proj({ x: 0, y: 0, z: 0 });
  const dirs = directionsFor(state.mode, primes);
  primes.forEach((p, i) => {
    const maxE = Math.max(2, Math.floor(Math.log(state.N) / Math.log(p)));
    const d = dirs[p], L = Math.log(p) * maxE;
    const ep = proj({ x: d.x * L, y: d.y * L, z: d.z * L });
    line(O, ep, axisColor(i, primes.length), 1.8);
    if (state.labels < 2) label('×' + p, ep.sx + 6, ep.sy + 4, axisColor(i, primes.length), 12);
  });

  // points
  const showKey = state.labels === 0, showAll = state.labels === 1 && scene.points.length <= 160;
  for (const p of scene.points) p._p = proj(p.X);
  const order = scene.points.length > 4000 ? scene.points : scene.points.slice().sort((u, v) => u._p.depth - v._p.depth);
  for (const p of order) {
    const pr = p._p;
    const rad = p.cat === 'atom' ? 5 : p.cat === 'one' ? 5 : p.cat === 'comp' ? 1.9 : p.cat === 'ppow' ? 3.3 : 2.5;
    if (p.cat === 'atom') { ctx.beginPath(); ctx.arc(pr.sx, pr.sy, rad + 3, 0, 7); ctx.fillStyle = 'rgba(245,179,1,.4)'; ctx.fill(); }
    ctx.beginPath(); ctx.arc(pr.sx, pr.sy, rad, 0, 7); ctx.fillStyle = p.cat === 'one' ? txt : p.color; ctx.fill();
    if ((showKey && (p.cat === 'atom' || p.cat === 'one' || p.n <= 30)) || showAll) label(String(p.n), pr.sx + rad + 2, pr.sy - 2, txt, 11);
  }
  if (state.sel >= 0 && state.sel < scene.points.length) {
    const q = scene.points[state.sel]._p;
    ctx.save(); ctx.strokeStyle = txt; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(q.sx, q.sy, 8, 0, 7); ctx.stroke(); ctx.restore();
    label(String(scene.points[state.sel].n), q.sx + 10, q.sy - 6, txt, 13);
  }
}

function renderPanels(){
  const primes = scene.primes;
  // axis legend
  $('#axisLegend').innerHTML = primes.map((p, i) =>
    `<span class="chip"><span class="dot" style="background:${axisColor(i, primes.length)}"></span>×${p}</span>`).join('');

  // distortion comparison table — item 10: partial enumeration invalidates the diagnostics.
  if (scene.aborted) {
    $('#distortionTable').innerHTML = `<div class="invalid">PARTIAL ENUMERATION — DIAGNOSTICS INVALID<br><span>تعداد DFS جزئيّ (استُنفدت الميزانية)؛ العيّنة لا تمثّل مجموعة الأعداد الناعمة المطلوبة. قلّل المجال أو عدد المحاور.</span></div>`;
  } else {
    const row = (lbl, key, d = 4) => `<tr><th>${lbl}</th><td>${fmtR(scene.distLegacy[key], d)}</td><td>${fmtR(scene.distCone[key], d)}</td></tr>`;
    const near = dd => dd.nearest ? `${dd.nearest.a}↔${dd.nearest.b} · d<sub>E</sub>=${fmtR(dd.nearest.dE, 4)} · ρ=${fmtR(dd.nearest.rho, 3)}` : '—';
    $('#distortionTable').innerHTML = `
      <table class="cmp"><thead><tr><th>المقياس</th><th>Legacy</th><th>Cone</th></tr></thead><tbody>
      <tr><th>العيّنة</th><td colspan="2">${scene.distCone.sampleMode} · ${fmtN(scene.distCone.sampleSize)} نقطة · ${fmtN(scene.distCone.pairs)} زوج (من ${fmtN(scene.points.length)} ناعمة)</td></tr>
      ${row('أصغر ρ', 'minRho')}
      ${row('شريحة ρ 5%', 'p5Rho')}
      ${row('وسيط ρ', 'medianRho')}
      ${row('أكبر ρ (≤ 1)', 'maxRho')}
      ${row('Spearman(d<sub>E</sub>, d<sub>log</sub>)', 'spearman')}
      <tr><th>تصادمات (d<sub>E</sub><${scene.distCone.epsilon})</th><td>${scene.distLegacy.collisions}</td><td>${scene.distCone.collisions}</td></tr>
      <tr><th>أقرب زوج في التضمين ℝ³</th><td>${near(scene.distLegacy)}</td><td>${near(scene.distCone)}</td></tr>
      </tbody></table>`;
  }

  // geometry self-checks
  const cc = coneChecks(state.k);
  const ok = b => b ? '<span class="ok">✓</span>' : '<span class="bad">✗</span>';
  $('#geoChecks').innerHTML =
    `فحوص الهندسة (Cone, k=${state.k}): |d<sub>j</sub>|=1 ${ok(cc.unit)} · d<sub>j</sub>·ŷ=cosθ ${ok(cc.polar)} · Σ أفقي≈0 ${ok(cc.horizontalSum)} · ρ<sub>max</sub>≤1 ${ok(scene.distCone.maxRho <= 1 + 1e-9 && scene.distLegacy.maxRho <= 1 + 1e-9)}`
    + (scene.aborted ? ' · <span class="bad">تعداد جزئيّ — التشخيصات مُعطَّلة</span>' : '');

  $('#pointCount').textContent = `${fmtN(scene.points.length)} عدداً ناعماً · ${primes.length} محوراً (أوّليّات حتى ${primes[primes.length - 1]})`;
}

function updHover(){
  const el = $('#hoverInfo');
  if (state.sel < 0 || !scene || state.sel >= scene.points.length) {
    el.textContent = 'مرّر أو انقر نقطةً لقراءة قيمتها ومتجهها ν. المحور المركزيّ مرجعٌ بصريّ فقط (الإحداثي الرأسيّ = cosθ·log n، لا log n حرفياً)، ولا كائن حسابيّ.';
    return;
  }
  const p = scene.points[state.sel], primes = scene.primes;
  const Om = p.exps.reduce((a, b) => a + b, 0), om = p.exps.filter(e => e > 0).length;
  el.innerHTML = `n = ${fmtN(p.n)} = ${factText(factor(p.n))} · ν over (${primes.join(',')}) = (${p.exps.join(',')}) · Ω=${Om}، ω=${om}`;
}

function hit(mx, my){
  let best = -1, bd = 13 * 13;
  for (let i = 0; i < scene.points.length; i++) {
    const pr = scene.points[i]._p; if (!pr) continue;
    const dx = pr.sx - mx, dy = pr.sy - my, d = dx * dx + dy * dy;
    if (d < bd) { bd = d; best = i; }
  }
  return best;
}

function resize(){
  state.dpr = Math.min(window.devicePixelRatio || 1, 2);
  const r = cvs.getBoundingClientRect();
  state.W = r.width; state.H = r.height;
  cvs.width = Math.round(state.W * state.dpr); cvs.height = Math.round(state.H * state.dpr);
  ctx.setTransform(state.dpr, 0, 0, state.dpr, 0, 0);
  if (scene) scene.baseScale = 0.42 * Math.min(state.W, state.H) / scene.mR;
}

// ---- interaction ----
let drag = false, lx = 0, ly = 0;
const rel = ev => { const r = cvs.getBoundingClientRect(); return [ev.clientX - r.left, ev.clientY - r.top]; };
cvs.addEventListener('pointerdown', ev => {
  const [mx, my] = rel(ev), h = scene ? hit(mx, my) : -1;
  if (h >= 0) { state.sel = h; updHover(); draw(); return; }
  drag = true; lx = ev.clientX; ly = ev.clientY; cvs.setPointerCapture(ev.pointerId); cvs.style.cursor = 'grabbing';
});
cvs.addEventListener('pointermove', ev => {
  if (drag) { state.yaw += (ev.clientX - lx) * 0.008; state.pitch = Math.max(-1.4, Math.min(1.4, state.pitch + (ev.clientY - ly) * 0.008)); lx = ev.clientX; ly = ev.clientY; draw(); return; }
  if (!scene) return;
  const [mx, my] = rel(ev), h = hit(mx, my);
  cvs.style.cursor = h >= 0 ? 'pointer' : 'grab';
  if (h >= 0 && h !== state.sel) { state.sel = h; updHover(); draw(); }
});
const up = () => { drag = false; cvs.style.cursor = 'grab'; };
cvs.addEventListener('pointerup', up); cvs.addEventListener('pointercancel', up);
cvs.addEventListener('wheel', ev => { ev.preventDefault(); state.zoom *= ev.deltaY < 0 ? 1.08 : 0.925; state.zoom = Math.max(0.3, Math.min(5, state.zoom)); draw(); }, { passive: false });

// ---- controls ----
$('#mode').addEventListener('change', e => { state.mode = e.target.value; build(); });
$('#kAxes').addEventListener('change', e => { state.k = +e.target.value; build(); });
$('#sampleMode').addEventListener('change', e => { state.sampleMode = e.target.value; build(); });
const slider = $('#rangeN'), out = $('#rangeOut');
const setRangeLabel = () => { out.textContent = 'n ≤ ' + fmtN(Math.round(Math.pow(10, +slider.value / 100))); };
slider.addEventListener('input', setRangeLabel);
slider.addEventListener('change', () => { state.N = Math.round(Math.pow(10, +slider.value / 100)); build(); });
$('#btnRotate').addEventListener('click', function(){ state.auto = !state.auto; this.textContent = state.auto ? 'إيقاف الدوران' : 'تشغيل الدوران'; });
$('#btnLabels').addEventListener('click', function(){ state.labels = (state.labels + 1) % 3; this.textContent = 'التسميات: ' + ['مفتاحية', 'الكل', 'بلا'][state.labels]; draw(); });
$('#btnReset').addEventListener('click', () => { state.yaw = 0.5; state.pitch = -0.32; state.zoom = 1; draw(); });
$('#btnExport').addEventListener('click', () => {
  if (!scene) return;
  const payload = {
    version: '6.1.0', generated_at: new Date().toISOString(),
    params: { mode: state.mode, k: state.k, N: state.N, sample_mode: state.sampleMode, primes: scene.primes, cone_theta_deg: CONE_THETA * 180 / Math.PI, reference_axis: REFERENCE_AXIS, vertical_coordinate: 'X_y(n) = cos(theta) * log n' },
    smooth_count: scene.points.length,
    distortion: { legacy: scene.distLegacy, cone: scene.distCone },
    cone_checks: coneChecks(state.k),
    ceiling: 'finite computational diagnostics; comparison layout experiment; no theorem, geometry-preservation, Goldbach, RH/GRH, or originality claim'
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob);
  a.download = `pvg-layout-distortion-${state.mode}-k${state.k}-N${state.N}.json`; a.click();
});

function loop(){ if (!drag && state.auto && scene) { state.yaw += 0.004; draw(); } requestAnimationFrame(loop); }
window.addEventListener('resize', () => { resize(); draw(); });

resize();
setRangeLabel();
build();
requestAnimationFrame(loop);
