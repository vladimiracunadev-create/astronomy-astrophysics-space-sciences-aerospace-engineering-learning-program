// SPDX-License-Identifier: Apache-2.0
// Vista 3D del simulador: cámara orbital, proyección en perspectiva, órbitas, anillos, fases, sombras y etiquetas sobre <canvas>.
// Todas las posiciones se manejan en km, en el marco eclíptico J2000 de las efemérides. Nada se dibuja «a escala artística»:
// el factor de ampliación de tamaños es explícito y se muestra en pantalla; las distancias son siempre las reales.
import { esferaPixeles } from "./esferas.js";
import { UA_KM } from "./cuerpos.js";

const RAD = Math.PI / 180;
const norm = (a) => { const n = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / n, a[1] / n, a[2] / n]; };
const cruz = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const punto = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

export function formatoKm(km) {
  const a = Math.abs(km);
  if (a >= 1e9) return `${(km / UA_KM).toFixed(2)} UA`;
  if (a >= 1e6) return `${(km / 1e6).toFixed(2)} M km`;
  if (a >= 1000) return `${Math.round(km).toLocaleString("es-CL")} km`;
  if (a >= 1) return `${km.toFixed(1)} km`;
  return `${(km * 1000).toFixed(0)} m`;
}

function estrellas(n) {
  let s = 12345;
  const rnd = () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296;
  const out = [];
  for (let i = 0; i < n; i++) {
    const z = 2 * rnd() - 1, t = 2 * Math.PI * rnd(), r = Math.sqrt(1 - z * z);
    out.push({ d: [r * Math.cos(t), r * Math.sin(t), z], m: Math.pow(rnd(), 3) });
  }
  return out;
}

export class Vista {
  constructor(canvas, opciones = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.fov = (opciones.fov || 40) * RAD;
    this.objetos = [];
    this.porId = new Map();
    this.seguir = null;          // objeto que ocupa el centro de la cámara
    this.cam = { yaw: -0.9, pitch: 0.45, dist: opciones.dist || 1e6, distObj: opciones.dist || 1e6 };
    this.limites = opciones.limites || { min: 1e3, max: 1e10 };
    this.ampliacion = 1;         // factor de tamaño de cuerpos (ver `ampliable`)
    this.mostrarOrbitas = true; this.mostrarEtiquetas = true; this.mostrarAnillos = true;
    this.seleccionado = null;
    this.sol = null;             // {pos}
    this.alSeleccionar = opciones.alSeleccionar || (() => {});
    this.estrellas = estrellas(900);
    this.cajas = [];
    this._arrastre = null;
    this._enlazar();
    this._ajustar();
    new ResizeObserver(() => this._ajustar()).observe(canvas.parentElement || canvas);
  }

  añadir(o) {
    o.pos = o.pos || [0, 0, 0];
    this.objetos.push(o); this.porId.set(String(o.id), o);
    return o;
  }

  _ajustar() {
    const p = this.canvas.parentElement || this.canvas;
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    const w = Math.max(200, p.clientWidth), h = Math.max(200, p.clientHeight);
    this.canvas.width = Math.round(w * dpr); this.canvas.height = Math.round(h * dpr);
    this.canvas.style.width = w + "px"; this.canvas.style.height = h + "px";
    this.dpr = dpr; this.W = w; this.H = h;
    this.F = (h / 2) / Math.tan(this.fov / 2);
  }

  _enlazar() {
    const c = this.canvas;
    const pts = new Map();
    c.addEventListener("pointerdown", (e) => {
      c.setPointerCapture(e.pointerId);
      pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
      this._arrastre = { x: e.clientX, y: e.clientY, mov: 0, d: pts.size === 2 ? this._distPts(pts) : 0 };
    });
    c.addEventListener("pointermove", (e) => {
      if (!pts.has(e.pointerId)) return;
      const p = pts.get(e.pointerId);
      if (pts.size === 2) {
        pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
        const d = this._distPts(pts);
        if (this._arrastre && this._arrastre.d) this.zoom(this._arrastre.d / d);
        if (this._arrastre) this._arrastre.d = d;
        return;
      }
      const dx = e.clientX - p.x, dy = e.clientY - p.y;
      pts.set(e.pointerId, { x: e.clientX, y: e.clientY });
      if (this._arrastre) this._arrastre.mov += Math.abs(dx) + Math.abs(dy);
      this.cam.yaw -= dx * 0.006;
      this.cam.pitch = Math.max(-1.5, Math.min(1.5, this.cam.pitch + dy * 0.006));
    });
    const fin = (e) => {
      const a = this._arrastre;
      pts.delete(e.pointerId);
      if (a && a.mov < 5 && pts.size === 0) this._clic(e);
      if (pts.size === 0) this._arrastre = null;
    };
    c.addEventListener("pointerup", fin);
    c.addEventListener("pointercancel", fin);
    c.addEventListener("wheel", (e) => { e.preventDefault(); this.zoom(Math.exp(e.deltaY * 0.0012)); }, { passive: false });
    c.addEventListener("dblclick", (e) => { const o = this._cercano(e); if (o) { this.seleccionar(o, true); } });
    c.tabIndex = 0;
    c.addEventListener("keydown", (e) => {
      const k = e.key;
      if (k === "+" || k === "=") this.zoom(0.8);
      else if (k === "-") this.zoom(1.25);
      else if (k === "ArrowLeft") this.cam.yaw += 0.1;
      else if (k === "ArrowRight") this.cam.yaw -= 0.1;
      else if (k === "ArrowUp") this.cam.pitch = Math.min(1.5, this.cam.pitch + 0.08);
      else if (k === "ArrowDown") this.cam.pitch = Math.max(-1.5, this.cam.pitch - 0.08);
      else return;
      e.preventDefault();
    });
  }
  _distPts(m) { const a = [...m.values()]; return Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y) || 1; }

  zoom(f) { this.cam.distObj = Math.min(this.limites.max, Math.max(this.limites.min, this.cam.distObj * f)); }

  _cercano(e) {
    const r = this.canvas.getBoundingClientRect();
    const x = e.clientX - r.left, y = e.clientY - r.top;
    let mejor = null, md = 18 * 18;
    for (const o of this.objetos) {
      if (!o._v || !o._v.visible || o.noSeleccionable) continue;
      const d = (o._v.sx - x) ** 2 + (o._v.sy - y) ** 2;
      const lim = Math.max(md, (o._v.rpx + 4) ** 2);
      if (d < lim && (mejor === null || d < mejor.d)) mejor = { o, d };
    }
    return mejor && mejor.o;
  }
  _clic(e) { const o = this._cercano(e); if (o) this.seleccionar(o); }

  seleccionar(o, centrar = false) {
    this.seleccionado = o;
    if (centrar) this.enfocar(o);
    this.alSeleccionar(o);
  }

  /** Centra la cámara en `o` con una distancia cómoda para ver su tamaño. */
  enfocar(o, distancia) {
    this.seguir = o;
    const r = o.radio || 1;
    this.cam.distObj = Math.min(this.limites.max, Math.max(this.limites.min, distancia || Math.max(r * 6, this.limites.min)));
  }

  // ---------------------------------------------------------------- proyección
  _baseCamara() {
    const { yaw, pitch, dist } = this.cam;
    const t = this.seguir ? this.seguir.pos : [0, 0, 0];
    const dir = [Math.cos(pitch) * Math.cos(yaw), Math.cos(pitch) * Math.sin(yaw), Math.sin(pitch)];
    const ojo = [t[0] + dir[0] * dist, t[1] + dir[1] * dist, t[2] + dir[2] * dist];
    const f = [-dir[0], -dir[1], -dir[2]];
    let r = cruz(f, [0, 0, 1]);
    if (Math.hypot(...r) < 1e-9) r = [1, 0, 0];
    r = norm(r);
    const u = cruz(r, f);
    this.b = { ojo, f, r, u, t: [-f[0], -f[1], -f[2]] };
  }
  proyectar(p) {
    const b = this.b;
    const d = [p[0] - b.ojo[0], p[1] - b.ojo[1], p[2] - b.ojo[2]];
    const z = punto(d, b.f);
    return { x: punto(d, b.r), y: punto(d, b.u), z };
  }
  pantalla(v) { return [this.W / 2 + (v.x * this.F) / v.z, this.H / 2 - (v.y * this.F) / v.z]; }

  // ---------------------------------------------------------------- dibujo
  dibujar(jdTdb) {
    const ctx = this.ctx;
    this.cam.dist += (this.cam.distObj - this.cam.dist) * 0.2;
    if (Math.abs(this.cam.dist / this.cam.distObj - 1) < 1e-4) this.cam.dist = this.cam.distObj;
    this._baseCamara();
    ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    ctx.fillStyle = "#02030a";
    ctx.fillRect(0, 0, this.W, this.H);
    this._fondo();

    const near = this.cam.dist * 1e-4;
    for (const o of this.objetos) {
      const v = this.proyectar(o.pos);
      const visible = v.z > near && !o.oculto;
      const factor = this._factorTamano(o);
      const rKm = (o.radio || 0) * factor;
      let sx = 0, sy = 0, rpx = 0;
      if (visible) { [sx, sy] = this.pantalla(v); rpx = (rKm * this.F) / v.z; }
      o._v = { vx: v, sx, sy, rpx, visible, z: v.z, rKm };
    }
    if (this.mostrarOrbitas) this._orbitas();

    const orden = this.objetos.filter((o) => o._v.visible).sort((a, b) => b._v.z - a._v.z);
    this.cajas = [];
    for (const o of orden) this._cuerpo(o);
    this._etiquetas(orden);
    this._marcadorSol();
    this._escala();
  }

  _factorTamano(o) {
    if (o.ampliable === false) return 1;
    return this.ampliacion;
  }

  _fondo() {
    const ctx = this.ctx, b = this.b;
    for (const e of this.estrellas) {
      const zf = punto(e.d, b.f);
      if (zf < 0.05) continue;
      const x = this.W / 2 + (punto(e.d, b.r) / zf) * this.F;
      const y = this.H / 2 - (punto(e.d, b.u) / zf) * this.F;
      if (x < 0 || y < 0 || x > this.W || y > this.H) continue;
      const a = 0.25 + 0.75 * e.m;
      ctx.fillStyle = `rgba(255,255,255,${a})`;
      const s = e.m > 0.7 ? 1.6 : 1;
      ctx.fillRect(x, y, s, s);
    }
  }

  _polilinea(pts, abierta = true) {
    // pts: Float64Array (x,y,z)*N en el marco de la escena. Recorta contra el plano cercano.
    const near = this.cam.dist * 1e-4;
    const p = new Path2D();
    let previo = null, dentro = false;
    const n = pts.length / 3;
    for (let i = 0; i < n; i++) {
      const v = this.proyectar([pts[i * 3], pts[i * 3 + 1], pts[i * 3 + 2]]);
      if (previo) {
        const a = previo, b = v;
        if (a.z > near && b.z > near) {
          const [x1, y1] = this.pantalla(a), [x2, y2] = this.pantalla(b);
          if (!dentro) { p.moveTo(x1, y1); dentro = true; }
          p.lineTo(x2, y2);
        } else if (a.z > near || b.z > near) {
          const t = (near - a.z) / (b.z - a.z);
          const c = { x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t, z: near };
          if (a.z > near) { const [x1, y1] = this.pantalla(a), [x2, y2] = this.pantalla(c); if (!dentro) p.moveTo(x1, y1); p.lineTo(x2, y2); dentro = false; }
          else { const [x1, y1] = this.pantalla(c), [x2, y2] = this.pantalla(b); p.moveTo(x1, y1); p.lineTo(x2, y2); dentro = true; }
        } else dentro = false;
      }
      previo = v;
    }
    return p;
  }

  _orbitas() {
    const ctx = this.ctx;
    ctx.lineWidth = 1;
    for (const o of this.objetos) {
      if (o.ocultarOrbita || o.oculto) continue;
      if (o.orbitaMinPx && o.orbitaRadioKm) {
        const cen = o.centroOrbita || [0, 0, 0];
        const vz = this.proyectar(cen).z;
        if (vz <= 0 || (o.orbitaRadioKm * this.F) / vz < o.orbitaMinPx) continue;
      }
      if (o.actualizarOrbita) o.actualizarOrbita();
      if (!o.orbita) continue;
      const sel = o === this.seleccionado;
      ctx.strokeStyle = sel ? "rgba(255,230,140,0.95)" : (o.colorOrbita || "rgba(130,170,220,0.35)");
      ctx.lineWidth = sel ? 1.6 : 1;
      ctx.stroke(this._polilinea(o.orbita));
    }
  }

  _luzHacia(o) {
    const s = this.sol ? this.sol.pos : [0, 0, 0];
    return norm([s[0] - o.pos[0], s[1] - o.pos[1], s[2] - o.pos[2]]);
  }

  _anillos(o, mitad) {
    // mitad: "atras" (más lejos de la cámara que el planeta) o "frente"
    const ctx = this.ctx, b = this.b;
    const pol = o.base ? o.base.z : [0, 0, 1];
    let u = cruz(pol, [0, 0, 1]);
    if (Math.hypot(...u) < 1e-6) u = [1, 0, 0];
    u = norm(u);
    const v = cruz(pol, u);
    const A = punto(u, b.f), B = punto(v, b.f);
    // profundidad d(θ) = A cosθ + B sinθ (>0: más lejos que el centro)
    const th0 = Math.atan2(-A, B); // d=0
    const mid = th0 + Math.PI / 2;
    const dm = A * Math.cos(mid) + B * Math.sin(mid);
    const lejos0 = dm > 0 ? th0 : th0 + Math.PI; // inicio de la mitad lejana
    const ini = mitad === "atras" ? lejos0 : lejos0 + Math.PI;
    const N = 72;
    ctx.save();
    for (const an of o.anillos) {
      const pa = [], pb = [];
      for (let k = 0; k <= N; k++) {
        const th = ini + (k / N) * Math.PI;
        const cs = Math.cos(th), sn = Math.sin(th);
        const dirv = [u[0] * cs + v[0] * sn, u[1] * cs + v[1] * sn, u[2] * cs + v[2] * sn];
        pa.push([o.pos[0] + dirv[0] * an.a, o.pos[1] + dirv[1] * an.a, o.pos[2] + dirv[2] * an.a]);
        pb.push([o.pos[0] + dirv[0] * an.b, o.pos[1] + dirv[1] * an.b, o.pos[2] + dirv[2] * an.b]);
      }
      const near = this.cam.dist * 1e-4;
      const A2 = pa.map((p) => this.proyectar(p)), B2 = pb.map((p) => this.proyectar(p));
      if (A2.some((q) => q.z <= near) || B2.some((q) => q.z <= near)) continue;
      ctx.beginPath();
      A2.forEach((q, i) => { const [x, y] = this.pantalla(q); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); });
      for (let i = B2.length - 1; i >= 0; i--) { const [x, y] = this.pantalla(B2[i]); ctx.lineTo(x, y); }
      ctx.closePath();
      const ancho = (an.b - an.a) * this.F / o._v.z;
      const color = o.colorAnillo || "225,205,160";
      if (ancho < 1.2) { ctx.strokeStyle = `rgba(${color},${Math.min(0.9, an.o + 0.2)})`; ctx.lineWidth = 1; ctx.stroke(); }
      else { ctx.fillStyle = `rgba(${color},${an.o})`; ctx.fill(); }
    }
    ctx.restore();
  }

  _cuerpo(o) {
    const ctx = this.ctx;
    const { sx, sy, rpx } = o._v;
    if (sx < -300 - rpx || sy < -300 - rpx || sx > this.W + 300 + rpx || sy > this.H + 300 + rpx) return;
    const luz = this._luzHacia(o);
    const apagado = o.eclipsado ? 1 - 0.88 * o.eclipsado : 1;
    if (o.anillos && this.mostrarAnillos && rpx > 2) this._anillos(o, "atras");

    if (o.autoluminoso && rpx < 3) {
      const g = ctx.createRadialGradient(sx, sy, 0, sx, sy, 10);
      g.addColorStop(0, "rgba(255,240,180,1)"); g.addColorStop(1, "rgba(255,200,80,0)");
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(sx, sy, 10, 0, 7); ctx.fill();
    } else if (rpx < 2.2) {
      ctx.globalAlpha = apagado;
      ctx.fillStyle = o.color || "#ccc";
      ctx.beginPath(); ctx.arc(sx, sy, Math.max(1.4, rpx), 0, 7); ctx.fill();
      ctx.globalAlpha = 1;
    } else if (rpx < 28 && !o.base) {
      this._esferaFase(o, sx, sy, rpx, luz, apagado);
    } else if (o.autoluminoso) {
      const g = ctx.createRadialGradient(sx, sy, rpx * 0.2, sx, sy, rpx * 1.8);
      g.addColorStop(0, "rgba(255,246,200,1)"); g.addColorStop(0.5, "rgba(255,214,110,0.9)"); g.addColorStop(1, "rgba(255,170,60,0)");
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(sx, sy, rpx * 1.8, 0, 7); ctx.fill();
    } else if (rpx < 28) {
      this._esferaFase(o, sx, sy, rpx, luz, apagado);
    } else {
      const b = this.b;
      ctx.globalAlpha = apagado;
      esferaPixeles(ctx, o, sx, sy, rpx, { r: b.r, u: b.u, t: b.t }, luz, o.base || { x: [1, 0, 0], y: [0, 1, 0], z: [0, 0, 1] });
      ctx.globalAlpha = 1;
    }
    if (o.anillos && this.mostrarAnillos && rpx > 2) this._anillos(o, "frente");
    if (o === this.seleccionado) {
      ctx.strokeStyle = "#ffe08a"; ctx.lineWidth = 1.4;
      ctx.beginPath(); ctx.arc(sx, sy, Math.max(8, rpx + 5), 0, 7); ctx.stroke();
    }
  }

  /** Disco con fase real: terminador = elipse de semieje menor |k| r (k = coseno ángulo Sol–cámara). */
  _esferaFase(o, sx, sy, r, luz, apagado) {
    const ctx = this.ctx, b = this.b;
    const xr = punto(luz, b.r), yr = punto(luz, b.u), k = punto(luz, b.t);
    const phi = Math.atan2(-yr, xr);
    ctx.save();
    ctx.translate(sx, sy); ctx.rotate(phi);
    ctx.globalAlpha = apagado;
    // lado nocturno
    ctx.fillStyle = "rgba(14,16,24,1)";
    const col = o.color || "#bbb";
    ctx.beginPath(); ctx.arc(0, 0, r, 0, 7); ctx.fill();
    // lado iluminado
    ctx.beginPath();
    ctx.arc(0, 0, r, -Math.PI / 2, Math.PI / 2, false);
    ctx.ellipse(0, 0, Math.max(1e-3, Math.abs(k)) * r, r, 0, Math.PI / 2, k >= 0 ? 1.5 * Math.PI : -Math.PI / 2, k < 0);
    ctx.closePath();
    const sxl = Math.sqrt(Math.max(0, 1 - k * k));
    const g = ctx.createRadialGradient(sxl * r * 0.55, 0, r * 0.05, 0, 0, r * 1.15);
    g.addColorStop(0, col); g.addColorStop(1, "rgba(30,30,36,1)");
    ctx.fillStyle = col;
    ctx.fill();
    ctx.globalCompositeOperation = "multiply";
    ctx.fillStyle = g; ctx.fill();
    ctx.restore();
  }

  _etiquetas(orden) {
    if (!this.mostrarEtiquetas) return;
    const ctx = this.ctx;
    ctx.font = "12px system-ui, sans-serif"; ctx.textBaseline = "middle";
    const lista = [...orden].filter((o) => o.etiqueta !== false).sort((a, b) => (b.prioridad || 0) - (a.prioridad || 0) || b._v.rpx - a._v.rpx);
    const ocupadas = [];
    let n = 0;
    for (const o of lista) {
      const { sx, sy, rpx } = o._v;
      if (sx < 0 || sy < 0 || sx > this.W || sy > this.H) continue;
      const forzada = o === this.seleccionado || o === this.seguir;
      if (!forzada && (o.prioridad || 0) < (this.umbralEtiquetas || 0)) continue;
      const txt = o.nombre;
      const w = ctx.measureText(txt).width;
      const x = sx + Math.max(6, rpx + 5), y = sy - 2;
      const caja = [x - 2, y - 8, x + w + 2, y + 8];
      if (!forzada && ocupadas.some((c) => !(caja[2] < c[0] || caja[0] > c[2] || caja[3] < c[1] || caja[1] > c[3]))) continue;
      if (!forzada && ++n > 60) break;
      ocupadas.push(caja);
      ctx.fillStyle = o === this.seleccionado ? "#ffe08a" : "rgba(220,230,245,0.88)";
      ctx.fillText(txt, x, y);
    }
  }

  _marcadorSol() {
    if (!this.sol || this.sol.ocultarFlecha) return;
    const v = this.proyectar(this.sol.pos);
    const ctx = this.ctx;
    const [sx, sy] = v.z > 0 ? this.pantalla(v) : [NaN, NaN];
    const dentro = v.z > 0 && sx > 20 && sy > 20 && sx < this.W - 20 && sy < this.H - 20;
    if (dentro) return;
    // flecha al borde en la dirección del Sol
    const ang = Math.atan2(-v.y, v.x);
    const cx = this.W / 2, cy = this.H / 2;
    const rx = this.W / 2 - 34, ry = this.H / 2 - 34;
    const t = 1 / Math.max(Math.abs(Math.cos(ang)) / rx, Math.abs(Math.sin(ang)) / ry);
    const x = cx + Math.cos(ang) * t, y = cy + Math.sin(ang) * t;
    ctx.save(); ctx.translate(x, y); ctx.rotate(ang);
    ctx.fillStyle = "#ffd45e"; ctx.beginPath(); ctx.moveTo(14, 0); ctx.lineTo(-6, -8); ctx.lineTo(-6, 8); ctx.closePath(); ctx.fill();
    ctx.restore();
    const d = Math.hypot(...this.sol.pos.map((q, i) => q - (this.seguir ? this.seguir.pos[i] : 0)));
    ctx.fillStyle = "#ffd45e"; ctx.font = "12px system-ui, sans-serif"; ctx.textAlign = "center";
    ctx.fillText(`☀ Sol · ${(d / UA_KM).toFixed(3)} UA`, x - Math.cos(ang) * 44, y - Math.sin(ang) * 22);
    ctx.textAlign = "start";
  }

  _escala() {
    const ctx = this.ctx;
    const pxKm = this.F / this.cam.dist;
    const objetivo = 110;
    const km = objetivo / pxKm;
    const e = Math.pow(10, Math.floor(Math.log10(km)));
    const m = km / e;
    const L = (m >= 5 ? 5 : m >= 2 ? 2 : 1) * e;
    const w = L * pxKm;
    const x = 18, y = this.H - 22;
    ctx.strokeStyle = "rgba(235,240,250,0.9)"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(x, y - 5); ctx.lineTo(x, y); ctx.lineTo(x + w, y); ctx.lineTo(x + w, y - 5); ctx.stroke();
    ctx.fillStyle = "rgba(235,240,250,0.95)"; ctx.font = "12px system-ui, sans-serif";
    ctx.fillText(`${formatoKm(L)} (a la profundidad del objetivo)`, x, y - 10);
  }
}
