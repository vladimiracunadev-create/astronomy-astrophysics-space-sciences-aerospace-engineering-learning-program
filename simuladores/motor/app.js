// SPDX-License-Identifier: Apache-2.0
// Constructor genérico de simuladores: carga las efemérides, crea la escena, el panel de datos y los controles de tiempo.
import { cargarSistema } from "./efemerides.js";
import { anguloRotacionTerrestre, Reloj, JD_UTC_INICIO, JD_UTC_FIN, formatoUtc, valorInputUtc, jdUtcDesdeInput, jdUtcDesdeMs, msDesdeJdUtc, limitar, jdTdbDesdeUtc } from "./tiempo.js";
import { Vista, formatoKm } from "./vista.js";
import { SOL, PLANETAS, LUNA, COLOR_SATELITE, ANILLOS, UA_KM, C_KM_S, baseDelCuerpo, elementos } from "./cuerpos.js";
import { barraNavegacion } from "./navegacion.js";
import { crearGeometria } from "./eclipses.js";

const VELOCIDADES = [
  ["Tiempo real (1×)", 1], ["1 min / s", 60], ["10 min / s", 600], ["1 h / s", 3600], ["6 h / s", 21600],
  ["1 día / s", 86400], ["7 días / s", 604800], ["30 días / s", 2592000], ["1 año / s", 31557600],
];
const PASOS = [["1 minuto", 60], ["1 hora", 3600], ["1 día", 86400], ["7 días", 604800], ["30 días", 2592000], ["1 año", 31557600]];
const PERIODO_PLANETA_D = { "199": 87.969, "299": 224.701, "399": 365.256, "499": 686.98, "599": 4332.59, "699": 10759.22, "799": 30688.5, "899": 60182, "9": 90560, "2000001": 1680 };
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const nrm = (a) => Math.hypot(a[0], a[1], a[2]);
const fmt = (x, d = 0) => x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d });
const RAD = Math.PI / 180;

function elipse(r, v, mu, N = 160) {
  const rn = nrm(r), v2 = dot(v, v);
  const h = [r[1] * v[2] - r[2] * v[1], r[2] * v[0] - r[0] * v[2], r[0] * v[1] - r[1] * v[0]];
  const rv = dot(r, v);
  const e = [((v2 - mu / rn) * r[0] - rv * v[0]) / mu, ((v2 - mu / rn) * r[1] - rv * v[1]) / mu, ((v2 - mu / rn) * r[2] - rv * v[2]) / mu];
  const en = nrm(e);
  if (en >= 0.995) return null;
  const hn = nrm(h), p = (hn * hn) / mu;
  const ex = en > 1e-9 ? [e[0] / en, e[1] / en, e[2] / en] : [r[0] / rn, r[1] / rn, r[2] / rn];
  const hh = [h[0] / hn, h[1] / hn, h[2] / hn];
  const q = [hh[1] * ex[2] - hh[2] * ex[1], hh[2] * ex[0] - hh[0] * ex[2], hh[0] * ex[1] - hh[1] * ex[0]];
  const out = new Float64Array((N + 1) * 3);
  for (let i = 0; i <= N; i++) {
    const nu = (i / N) * 2 * Math.PI, rr = p / (1 + en * Math.cos(nu));
    const c = Math.cos(nu) * rr, s = Math.sin(nu) * rr;
    out[i * 3] = c * ex[0] + s * q[0]; out[i * 3 + 1] = c * ex[1] + s * q[1]; out[i * 3 + 2] = c * ex[2] + s * q[2];
  }
  return { puntos: out, a: p / (1 - en * en), e: en };
}

function html(strings, ...v) { return strings.reduce((a, s, i) => a + s + (v[i] ?? ""), ""); }

export async function iniciar(cfg) {
  const raiz = document.getElementById("app");
  raiz.innerHTML = "";
  const cab = document.createElement("header");
  cab.className = "cabecera";
  cab.innerHTML = `<h1>${cfg.titulo}</h1>`;
  cab.appendChild(barraNavegacion(cfg.clave));
  document.body.insertBefore(cab, raiz);

  raiz.className = "app";
  raiz.innerHTML = html`
    <section class="escena" aria-label="Escena 3D del ${cfg.titulo}">
      <canvas id="lienzo" aria-label="Vista tridimensional. Arrastre para girar, rueda para acercar, doble clic para enfocar un cuerpo."></canvas>
      <div class="hud"><div class="fecha" id="fecha" aria-live="off"></div><div class="sub" id="sub"></div></div>
      <div class="cargando" id="cargando"><div>Cargando efemérides oficiales de JPL Horizons…</div><progress id="prog" max="1" value="0"></progress><small id="cargaTxt"></small></div>
      <div class="barra" id="barra">
        <div class="grupo" role="group" aria-label="Control del tiempo">
          <button id="bIni" title="Ir al 1 de enero de 2027" aria-label="Ir al inicio">⏮</button>
          <button id="bAtras" title="Retroceder un paso" aria-label="Retroceder un paso">◀</button>
          <button id="bPlay" title="Reproducir / pausar (barra espaciadora)" aria-label="Reproducir">▶</button>
          <button id="bAdel" title="Avanzar un paso" aria-label="Avanzar un paso">▶|</button>
          <button id="bFin" title="Ir al 31 de diciembre de 2050" aria-label="Ir al final">⏭</button>
          <button id="bInv" title="Invertir el sentido del tiempo" aria-pressed="false" aria-label="Invertir sentido">⇄</button>
        </div>
        <div class="grupo"><label for="sVel" class="etq">Velocidad</label><select id="sVel"></select></div>
        <div class="grupo"><label for="sPaso" class="etq">Paso</label><select id="sPaso"></select></div>
        <div class="grupo"><label for="iFecha" class="etq">Fecha UTC</label><input type="datetime-local" id="iFecha" min="2027-01-01T00:00" max="2050-12-31T23:59"><button id="bIr">Ir</button></div>
      </div>
    </section>
    <aside class="lateral" aria-label="Datos y controles">
      <h2>Cuerpo seleccionado</h2>
      <div class="ficha" id="ficha" aria-live="polite"></div>
      <h2>Vista</h2>
      <div class="grupo" style="display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center">
        <label class="chk"><input type="checkbox" id="cOrb" checked> Órbitas</label>
        <label class="chk"><input type="checkbox" id="cEtq" checked> Etiquetas</label>
        ${cfg.anillos ? '<label class="chk"><input type="checkbox" id="cAni" checked> Anillos</label>' : ""}
      </div>
      <div style="margin-top:6px"><label for="sAmp" class="etq">Tamaño de los cuerpos </label>
        <select id="sAmp"></select></div>
      <p class="aviso" id="avisoEscala"></p>
      <div id="atajos" style="display:flex;flex-wrap:wrap;gap:6px"></div>
      <h2 id="tCuerpos">Cuerpos</h2>
      <div style="display:flex;gap:6px;flex-wrap:wrap"><input type="search" id="buscar" placeholder="Buscar…" aria-label="Buscar cuerpo" style="flex:1;min-width:120px">
        <select id="orden" aria-label="Ordenar"><option value="dist">Por distancia</option><option value="radio">Por tamaño</option><option value="nombre">Por nombre</option></select></div>
      <div class="lista" id="lista" role="listbox" aria-label="Lista de cuerpos"></div>
      ${cfg.eclipses ? '<h2>Eclipses 2027–2050</h2><p class="aviso">Calculados aquí con la geometría de conos a partir de las efemérides; clic para ir al máximo.</p><div id="eclipses"></div>' : ""}
      ${cfg.eventos ? '<h2>Fenómenos 2027–2050</h2><div id="eventos"></div>' : ""}
      <details><summary>Datos, modelo y tolerancias</summary><div id="meta" class="aviso"></div></details>
      <p class="aviso">Posiciones: NASA/JPL Horizons (DE440 y efemérides de satélites), interpoladas aquí. Texturas ilustrativas, salvo la de Marte (mapa de imágenes Viking procesadas por el USGS; NASA/JPL-Caltech) y la de Plutón (mosaico de New Horizons: NASA, JHUAPL, SwRI, LPI, USGS; monocromo, el tercio sur no se fotografió). Documentación: <a href="documentacion/README.html">documentación de los simuladores</a>.</p>
    </aside>`;

  const $ = (id) => document.getElementById(id);
  const lienzo = $("lienzo");
  const reloj = new Reloj(JD_UTC_INICIO);
  reloj.velocidad = cfg.velocidad || 3600;

  // ---------------------------------------------------------------- carga de datos
  let sol, sis;
  try {
    const base = "datos";
    const tareas = cfg.clave === "sol" ? ["sol", "tierra"] : ["sol", cfg.clave];
    const prog = [0, 0];
    const mostrar = () => { $("prog").value = (prog[0] + prog[1]) / 2; };
    const r = await Promise.all(tareas.map((n, i) => cargarSistema(n, base, (f) => { prog[i] = f; mostrar(); $("cargaTxt").textContent = `${n}.bin`; })));
    sol = r[0]; sis = r[1];
  } catch (e) {
    const c = $("cargando"); c.classList.add("error");
    c.innerHTML = `<div><strong>No se pudieron cargar las efemérides.</strong></div><div>${e.message}</div><small>Si abre este archivo con file://, sirva la carpeta con un servidor HTTP (por ejemplo <code>python -m http.server</code>) o use la versión publicada en GitHub Pages.</small>`;
    return;
  }
  $("cargando").remove();

  // ---------------------------------------------------------------- escena
  const vista = new Vista(lienzo, { dist: cfg.distInicial, limites: { min: 1.5, max: cfg.distMax || 3e10 }, alSeleccionar: (o) => seleccionar(o) });
  const esSol = cfg.clave === "sol";
  const pid = cfg.planetaId;       // planeta central (null en el Sistema Solar)
  const solObj = vista.añadir({ id: "10", nombre: "Sol", radio: SOL.radio, color: SOL.color, autoluminoso: true, textura: "sol", prioridad: 1000, ampliable: false, tipo: "estrella", base: baseDelCuerpo(SOL.polo, 2461406.5), fisico: SOL });
  vista.sol = solObj;
  vista.sol.ocultarFlecha = esSol;
  const objetos = [];

  function crearPlaneta(id, ampliable) {
    const f = PLANETAS[id];
    const o = vista.añadir({ id, nombre: f.nombre, radio: f.radio, aplan: f.aplan, color: f.color, textura: { "199": "mercurio", "299": "venus", "399": "tierra", "499": "marte", "599": "jupiter", "699": "saturno", "799": "urano", "899": "neptuno" }[id] || "#b8b3aa",
      prioridad: 500, ampliable, tipo: f.enano ? "planeta enano" : "planeta", fisico: f, tabla: sol.cuerpo(id), atmosfera: id === "399" ? { c: [70, 130, 255], k: 0.9 } : id === "299" ? { c: [255, 220, 150], k: 0.6 } : id === "499" ? { c: [230, 160, 110], k: 0.15 } : null });
    if (ANILLOS[id]) { o.anillos = ANILLOS[id]; o.colorAnillo = id === "699" ? "226,206,160" : id === "799" ? "200,210,220" : id === "899" ? "190,200,230" : "190,160,130"; }
    return o;
  }

  const lunas = [];
  if (esSol) {
    for (const id of Object.keys(PLANETAS)) {
      const o = crearPlaneta(id, true);
      o.centroOrbita = [0, 0, 0];
      o.orbitaMinPx = 6; o.orbitaRadioKm = Math.cbrt(SOL.gm * Math.pow((PERIODO_PLANETA_D[id] * 86400) / (2 * Math.PI), 2)); // semieje mayor kepleriano inicial
      o.actualizarOrbita = function () {
        const jd = reloj.jdTdb;
        if (this._orbJd !== undefined && Math.abs(jd - this._orbJd) < 20) return;
        const t = this.tabla, r = t.pos(jd), v = t.vel(jd);
        const el = elipse(r, v, SOL.gm + (this.fisico.gm || 0));
        if (el) { this.orbita = el.puntos; this.orbitaRadioKm = el.a; }
        this._orbJd = jd;
      };
      objetos.push(o);
    }
    // Luna: sigue a la Tierra (visible al acercarse)
    const tierraSis = sis;
    const l = vista.añadir({ id: "301", nombre: "Luna", radio: LUNA.radio, color: LUNA.color, textura: "luna", prioridad: 50, ampliable: true, tipo: "luna", tabla: tierraSis.cuerpo("301"), fisico: LUNA, relativo: "399" });
    objetos.push(l); lunas.push(l);
  } else {
    const c = cfg.baricentro
      ? vista.añadir({ id: "bari", nombre: cfg.baricentro, radio: 0, color: "#ffffff", prioridad: 900, ampliable: false, tipo: "baricentro", tabla: null })
      : crearPlaneta(pid, false);
    c.pos = [0, 0, 0]; c.esCentro = true; c.noMover = true;
    objetos.push(c);
    for (const m of sis.meta.cuerpos) {
      const t = sis.cuerpo(m.id);
      const radio = m.radio_km || (m.id === "301" ? LUNA.radio : 0);
      const o = vista.añadir({ id: String(m.id), nombre: m.nombre, designacion: m.designacion, radio, color: COLOR_SATELITE[m.id] || "#b9b4aa",
        textura: m.id === "301" ? "luna" : m.id === "999" ? "pluton" : (COLOR_SATELITE[m.id] || "#b9b4aa"), prioridad: radio ? Math.min(900, radio) : 0, ampliable: true,
        tipo: m.id === "999" ? "planeta enano" : "luna", tabla: t, meta: m, orbitaMinPx: 5, orbitaRadioKm: m.a_km, aplan: 0, color2: null });
      if (m.id === "999") { o.fisico = PLANETAS["9"]; o.color = PLANETAS["9"].color; o.nombre = "Plutón"; }
      if (m.id === "901") o.nombre = "Caronte";
      o.actualizarOrbita = function () {
        const jd = reloj.jdTdb, P = this.meta.periodo_d || 1;
        const ref = this._orbJd;
        const paso = P / 100;
        if (ref !== undefined && Math.abs(jd - ref) < paso && !this._forzar) return;
        this._forzar = false;
        const t = this.tabla, v0 = t.meta.jd_valido_ini, v1 = t.meta.jd_valido_fin;
        const cabe = P * 1.05 < (v1 - v0);
        if (cabe) {
          const N = 120, a = Math.min(Math.max(jd - P / 2, v0), v1 - P), pts = new Float64Array((N + 1) * 3), tmp = [0, 0, 0];
          for (let i = 0; i <= N; i++) { t.pos(a + (P * i) / N, tmp); pts[i * 3] = tmp[0]; pts[i * 3 + 1] = tmp[1]; pts[i * 3 + 2] = tmp[2]; }
          this.orbita = pts;
        } else {
          const el = elipse(t.pos(jd), t.vel(jd), PLANETAS[pid].gm);
          this.orbita = el ? el.puntos : null;
        }
        this._orbJd = jd;
      };
      o.colorOrbita = o.meta.principal ? "rgba(150,190,240,0.5)" : "rgba(120,150,190,0.28)";
      objetos.push(o); lunas.push(o);
    }
  }
  const central = esSol ? solObj : vista.porId.get(cfg.baricentro ? "bari" : pid);
  const planetas = objetos.filter((o) => o.tipo === "planeta" || o.tipo === "planeta enano");
  const geo = cfg.eclipses ? crearGeometria(sol, sis) : null;

  // Fracción de la luna dentro del cono de umbra del planeta. p: posición de la luna respecto del planeta; h: posición heliocéntrica del planeta.
  function sombra(p, h, rm) {
    const dS = nrm(h), s = [-h[0] / dS, -h[1] / dS, -h[2] / dS];
    const x = -dot(p, s);
    if (x <= 0) return 0;
    const Rp = PLANETAS[pid].radio;
    const q = nrm([p[0] + s[0] * x, p[1] + s[1] * x, p[2] + s[2] * x]);
    const ru = Rp - x * ((SOL.radio - Rp) / dS);
    return ru > 0 ? Math.max(0, Math.min(1, (ru + rm - q) / (2 * Math.max(rm, 1)))) : 0;
  }
  /** Primer eclipse (por la sombra del planeta) posterior a `jd`: [inicio, fin] en JD TDB, o null. */
  function proximoEclipse(o, jd) {
    const P = o.meta.periodo_d, hor = Math.min(3 * P, 60), dt = Math.max(P / 300, 1e-3);
    const t = o.tabla, pp = [0, 0, 0], hh = [0, 0, 0];
    const f = (x) => sombra(t.pos(x, pp), sol.pos(pid, x, hh), o.radio || 0);
    let ini = null;
    for (let x = jd; x < Math.min(jd + hor, t.meta.jd_valido_fin); x += dt) {
      const e = f(x) > 0.02;
      if (ini === null && e) { let a = x - dt, b = x; for (let k = 0; k < 12; k++) { const m = (a + b) / 2; if (f(m) > 0.02) b = m; else a = m; } ini = b; }
      else if (ini !== null && !e) { let a = x - dt, b = x; for (let k = 0; k < 12; k++) { const m = (a + b) / 2; if (f(m) > 0.02) a = m; else b = m; } return [ini, a]; }
    }
    return ini === null ? null : [ini, ini];
  }

  // La Tierra gira según el ángulo de rotación terrestre (ERA, UT1 ~ UTC); W = ERA - (alfa0 + 90 grados).
  const baseTierra = (jdTdb) => {
    const pol = PLANETAS["399"].polo, T = (jdTdb - 2451545.0) / 36525;
    const a0 = (pol.a0 + pol.da0 * T) * RAD;
    return baseDelCuerpo(pol, jdTdb, anguloRotacionTerrestre(reloj.jdUtc) - (a0 + Math.PI / 2));
  };

  // ---------------------------------------------------------------- actualización por fotograma
  const tmp = [0, 0, 0];
  function actualizar() {
    const jd = reloj.jdTdb;
    if (esSol) {
      solObj.pos = [0, 0, 0];
      for (const o of planetas) o.tabla.pos(jd, o.pos);
      for (const o of lunas) { const t = o.tabla.pos(jd, tmp); const p = vista.porId.get(o.relativo).pos; o.pos[0] = p[0] + t[0]; o.pos[1] = p[1] + t[1]; o.pos[2] = p[2] + t[2]; }
      for (const o of planetas) o.base = o.id === "399" ? baseTierra(jd) : baseDelCuerpo(o.fisico.polo, jd);
      solObj.base = baseDelCuerpo(SOL.polo, jd);
    } else {
      const h = sol.pos(pid, jd, tmp);
      solObj.pos[0] = -h[0]; solObj.pos[1] = -h[1]; solObj.pos[2] = -h[2];
      central.base = pid === "399" ? baseTierra(jd) : baseDelCuerpo(PLANETAS[pid].polo, jd);
      const pluto = cfg.baricentro ? vista.porId.get("999") : null;
      const dSol = nrm(solObj.pos), s = [solObj.pos[0] / dSol, solObj.pos[1] / dSol, solObj.pos[2] / dSol];
      const Rp = PLANETAS[pid].radio;
      for (const o of lunas) {
        const t = o.tabla.meta;
        o.oculto = jd < t.jd_valido_ini || jd > t.jd_valido_fin;
        if (o.oculto) continue;
        o.tabla.pos(jd, o.pos);
        // eclipse por la sombra del planeta (cono de umbra)
        o.eclipsado = cfg.baricentro ? 0 : sombra(o.pos, h, o.radio || 0);
        if (cfg.baricentro && (o.id === "901" || o.id === "999")) { // Plutón y Caronte: rotación síncrona, se miran siempre la misma cara
          const otro = vista.porId.get(o.id === "901" ? "999" : "901");
          const ex = [otro.pos[0] - o.pos[0], otro.pos[1] - o.pos[1], otro.pos[2] - o.pos[2]]; const n = nrm(ex);
          const X = [ex[0] / n, ex[1] / n, ex[2] / n];
          let Z = o.id === "999" ? baseDelCuerpo(PLANETAS["9"].polo, jd).z : [0, 0, 1];
          const k = dot(Z, X); Z = [Z[0] - k * X[0], Z[1] - k * X[1], Z[2] - k * X[2]]; const zn = nrm(Z); Z = [Z[0] / zn, Z[1] / zn, Z[2] / zn];
          o.base = { x: X, y: [Z[1] * X[2] - Z[2] * X[1], Z[2] * X[0] - Z[0] * X[2], Z[0] * X[1] - Z[1] * X[0]], z: Z };
        } else if (o.id === "301") { // rotación síncrona media (sin libración)
          const ex = [-o.pos[0], -o.pos[1], -o.pos[2]]; const n = nrm(ex);
          const X = [ex[0] / n, ex[1] / n, ex[2] / n];
          let Z = [0, 0, 1]; const k = dot(Z, X); Z = [Z[0] - k * X[0], Z[1] - k * X[1], Z[2] - k * X[2]]; const zn = nrm(Z); Z = [Z[0] / zn, Z[1] / zn, Z[2] / zn];
          o.base = { x: X, y: [Z[1] * X[2] - Z[2] * X[1], Z[2] * X[0] - Z[0] * X[2], Z[0] * X[1] - Z[1] * X[0]], z: Z };
        }
      }
    }
  }

  // ---------------------------------------------------------------- panel de datos
  function seleccionar(o) {
    vista.seleccionado = o;
    pintarFicha();
    for (const b of document.querySelectorAll("#lista button")) b.setAttribute("aria-current", String(b.dataset.id === (o && o.id)));
    history.replaceState(null, "", `#o=${o.id}&f=${valorInputUtc(reloj.jdUtc)}`);
  }

  function datosCuerpo(o) {
    const jd = reloj.jdTdb;
    const p = o.pos;
    const dSol = nrm(sub(p, solObj.pos));
    const out = [];
    const fis = o.fisico;
    out.push(["Radio" + (fis && fis.aplan ? " ecuatorial" : ""), o.radio ? `${fmt(o.radio, o.radio < 100 ? 1 : 0)} km` : "no publicado"]);
    out.push(["Distancia al Sol", `${fmt(dSol / UA_KM, 4)} UA · luz ${fmt(dSol / C_KM_S / 60, 1)} min`]);
    if (o !== solObj && !o.esCentro && !esSol && o.tabla) {
      // En el sistema de Plutón todo gira en torno al baricentro; Caronte se describe respecto de Plutón (órbita relativa).
      const plu = cfg.baricentro && o.id === "901" ? vista.porId.get("999") : null;
      const rel = plu ? [p[0] - plu.pos[0], p[1] - plu.pos[1], p[2] - plu.pos[2]] : p, d = nrm(rel);
      const refN = cfg.baricentro ? (plu ? "Plutón" : "el baricentro") : PLANETAS[pid].nombre;
      out.push([`Distancia a ${refN}`, `${fmt(d)} km${cfg.baricentro ? "" : ` · ${fmt(d / PLANETAS[pid].radio, 1)} R`}`]);
      const v0 = o.tabla.vel(jd), vp = plu ? plu.tabla.vel(jd) : [0, 0, 0];
      const v = [v0[0] - vp[0], v0[1] - vp[1], v0[2] - vp[2]];
      out.push(["Velocidad orbital", `${fmt(nrm(v), 3)} km/s`]);
      const el = elementos(rel, v, PLANETAS[pid].gm);
      if (!(cfg.baricentro && o.id === "999")) {
        out.push(["a, e, i osculadores", `${fmt(el.a)} km · ${fmt(el.e, 4)} · ${fmt(el.i, 2)}°`]);
        out.push(["Periodo osculador", `${fmt(el.periodo_d, 3)} d`]);
      }
      const hv = [rel[1] * v[2] - rel[2] * v[1], rel[2] * v[0] - rel[0] * v[2], rel[0] * v[1] - rel[1] * v[0]];
      out.push(["Sentido de la órbita", dot(hv, central.base ? central.base.z : [0, 0, 1]) >= 0 ? "directo (como rota el planeta)" : "retrógrado"]);
      const lon = (Math.atan2(rel[1], rel[0]) / RAD + 360) % 360, lat = Math.asin(rel[2] / d) / RAD;
      out.push(["Long./lat. eclíptica J2000", `${fmt(lon, 2)}° · ${fmt(lat, 2)}°`]);
      const s = [solObj.pos[0] - p[0], solObj.pos[1] - p[1], solObj.pos[2] - p[2]];
      const cosA = dot(s, [-p[0], -p[1], -p[2]]) / (nrm(s) * d);
      const fase = (1 + cosA) / 2; // iluminada vista desde el planeta
      out.push(["Iluminación vista desde el planeta", `${fmt(fase * 100, 1)} %`]);
      if (o.eclipsado > 0) out.push(["Estado", `en la sombra de ${PLANETAS[pid].nombre} (${fmt(o.eclipsado * 100, 0)} %)`]);
      if (pid !== "399" && !cfg.baricentro && o.meta && o.meta.periodo_d < 60 && !o.oculto) {
        const ev = proximoEclipse(o, jd);
        out.push([`Próximo eclipse por ${PLANETAS[pid].nombre}`, ev ? `${formatoUtc(jdUtcDesdeTdb2(ev[0]), false)}${ev[1] > ev[0] ? ` · ${fmt((ev[1] - ev[0]) * 1440, 0)} min` : ""}` : `ninguno en ${fmt(Math.min(3 * o.meta.periodo_d, 60), 0)} d`]);
      }
      if (o.meta) {
        out.push(["Error máx. de interpolación", `${fmt(o.meta.error_max_km, 2)} km (medido vs. JPL)`]);
        if (o.meta.jd_valido_fin < 2470150) out.push(["Cobertura JPL", `hasta ${formatoUtc(jdUtcDesdeTdb2(o.meta.jd_valido_fin), false)}`]);
      }
    } else if (esSol && o.tabla) {
      const v = o.tabla.vel(jd);
      out.push(["Velocidad heliocéntrica", `${fmt(nrm(v), 3)} km/s`]);
      if (o.id !== "301") {
        const el = elementos(o.pos, v, SOL.gm);
        out.push(["a, e, i osculadores", `${fmt(el.a / UA_KM, 4)} UA · ${fmt(el.e, 4)} · ${fmt(el.i, 2)}°`]);
        out.push(["Periodo osculador", `${fmt(el.periodo_d / 365.25, 3)} años`]);
        out.push(["Error máx. de interpolación", `${fmt(o.tabla.meta.error_max_km, 3)} km (medido vs. JPL)`]);
      }
    }
    return out;
  }
  const jdUtcDesdeTdb2 = (j) => j - 69.184 / 86400;
  const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];

  function pintarFicha() {
    const o = vista.seleccionado || central;
    const extra = cfg.extra ? cfg.extra({ o, reloj, vista, sol, sis, geo, objetos, solObj, central, nrm, dot, fmt }) : [];
    $("ficha").innerHTML = html`<h3>${o.nombre}</h3><div class="etq">${o.tipo || ""}${o.designacion ? " · " + o.designacion.replace(/_/g, " ") : ""}${o.meta ? " · Horizons " + o.id : ""}</div>
      <dl class="datos">${datosCuerpo(o).concat(extra).map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("")}</dl>
      <div style="margin-top:8px;display:flex;gap:6px;flex-wrap:wrap"><button id="bEnf">Enfocar</button><button id="bVer">Ver el sistema</button></div>`;
    $("bEnf").onclick = () => vista.enfocar(o);
    $("bVer").onclick = () => { vista.seguir = esSol ? solObj : central; vista.cam.distObj = cfg.distInicial; };
  }

  // ---------------------------------------------------------------- lista
  function pintarLista() {
    const q = $("buscar").value.trim().toLowerCase();
    const ord = $("orden").value;
    let l = [...objetos, solObj].filter((o) => !o.esCentro || true).filter((o) => !q || (o.nombre + " " + (o.designacion || "")).toLowerCase().includes(q));
    const dist = (o) => nrm(sub(o.pos, esSol ? [0, 0, 0] : [0, 0, 0]));
    if (ord === "dist") l.sort((a, b) => dist(a) - dist(b)); else if (ord === "radio") l.sort((a, b) => (b.radio || 0) - (a.radio || 0)); else l.sort((a, b) => a.nombre.localeCompare(b.nombre, "es"));
    $("lista").innerHTML = l.slice(0, 400).map((o) => `<button role="option" data-id="${o.id}" aria-current="${o === vista.seleccionado}"><span>${o.nombre}${o.oculto ? " (sin efemérides)" : ""}</span><small>${o.radio ? fmt(o.radio, o.radio < 100 ? 1 : 0) + " km" : "—"}</small></button>`).join("");
    $("tCuerpos").textContent = esSol ? `Cuerpos (${objetos.length + 1})` : cfg.baricentro ? `Cuerpos del sistema (${lunas.length})` : `Lunas de ${PLANETAS[pid].nombre} (${lunas.length})`;
  }
  $("lista").addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const o = vista.porId.get(b.dataset.id); if (o) { vista.seleccionar(o, true); }
  });
  $("buscar").addEventListener("input", pintarLista);
  $("orden").addEventListener("change", pintarLista);

  // ---------------------------------------------------------------- controles
  $("sVel").innerHTML = VELOCIDADES.map(([t, v]) => `<option value="${v}">${t}</option>`).join("");
  $("sVel").value = String(cfg.velocidad || 3600);
  $("sPaso").innerHTML = PASOS.map(([t, v]) => `<option value="${v}">${t}</option>`).join("");
  $("sPaso").value = String(cfg.paso || 3600);
  const AMP = cfg.ampliaciones || [1, 10, 100, 1000];
  $("sAmp").innerHTML = AMP.map((a) => `<option value="${a}">${a === 1 ? "Real (×1)" : "×" + a.toLocaleString("es-CL")}</option>`).join("");
  function avisoEscala() {
    const a = vista.ampliacion;
    $("avisoEscala").textContent = a === 1 ? "Tamaños reales y distancias reales (cuerpos pequeños se marcan con un punto de ≥ 2 px)." :
      `Los cuerpos ${esSol ? "(planetas y Luna)" : "(lunas)"} se dibujan ×${a.toLocaleString("es-CL")} más grandes que su tamaño real; las distancias siguen siendo las reales.`;
  }
  $("sAmp").onchange = () => { vista.ampliacion = +$("sAmp").value; avisoEscala(); };
  avisoEscala();
  $("cOrb").onchange = () => (vista.mostrarOrbitas = $("cOrb").checked);
  $("cEtq").onchange = () => (vista.mostrarEtiquetas = $("cEtq").checked);
  if (cfg.anillos) $("cAni").onchange = () => (vista.mostrarAnillos = $("cAni").checked);
  $("sVel").onchange = () => { reloj.velocidad = Math.abs(+$("sVel").value) * (reloj.velocidad < 0 ? -1 : 1); };
  const play = () => { reloj.activo = !reloj.activo; $("bPlay").textContent = reloj.activo ? "⏸" : "▶"; $("bPlay").setAttribute("aria-label", reloj.activo ? "Pausar" : "Reproducir"); };
  $("bPlay").onclick = play;
  const salto = (dir) => { reloj.fijar(reloj.jdUtc + (dir * +$("sPaso").value) / 86400); };
  $("bAtras").onclick = () => salto(-1);
  $("bAdel").onclick = () => salto(1);
  $("bIni").onclick = () => reloj.fijar(JD_UTC_INICIO);
  $("bFin").onclick = () => reloj.fijar(JD_UTC_FIN);
  $("bInv").onclick = () => { reloj.velocidad = -reloj.velocidad; $("bInv").setAttribute("aria-pressed", String(reloj.velocidad < 0)); };
  $("bIr").onclick = () => { const jd = jdUtcDesdeInput($("iFecha").value); if (jd) reloj.fijar(jd); };
  $("iFecha").addEventListener("keydown", (e) => { if (e.key === "Enter") $("bIr").click(); });
  window.addEventListener("keydown", (e) => {
    if (/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) return;
    if (e.code === "Space") { e.preventDefault(); play(); }
    else if (e.key === "," ) salto(-1); else if (e.key === ".") salto(1);
  });

  // atajos de enfoque
  $("atajos").innerHTML = (cfg.atajos ? cfg.atajos({ vista, objetos, central, solObj, esSol }) : []).map((a, i) => `<button data-i="${i}">${a.texto}</button>`).join("");
  const at = cfg.atajos ? cfg.atajos({ vista, objetos, central, solObj, esSol }) : [];
  $("atajos").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) at[+b.dataset.i].accion(); });

  // eclipses
  if (cfg.eclipses) {
    const ecl = geo.buscar(jdTdbDesdeUtc(JD_UTC_INICIO), jdTdbDesdeUtc(JD_UTC_FIN));
    $("eclipses").innerHTML = `<table class="tabla"><thead><tr><th>Fecha (UTC)</th><th>Tipo</th><th>Dato</th></tr></thead><tbody>` +
      ecl.map((e, i) => `<tr><td><button data-i="${i}" title="Ir al máximo">${formatoUtc(e.jdUtc, false).replace(" UTC", "")}</button></td><td>${e.tipo === "solar" ? "☀ Sol" : "☾ Luna"} ${e.clase}</td><td>${e.tipo === "solar" ? "γ " + fmt(e.gamma, 3) : e.clase === "penumbral" ? "mag. penumbral " + fmt(e.mag_penumbral, 2) : "mag. umbral " + fmt(e.mag_umbral, 2)}</td></tr>`).join("") + "</tbody></table>";
    $("eclipses").addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; const x = ecl[+b.dataset.i]; reloj.fijar(x.jdUtc - 0 / 1); reloj.activo = false; $("bPlay").textContent = "▶"; vista.seleccionar(vista.porId.get("301")); });
    cfg._eclipses = ecl;
  }

  // fenómenos calculados (estaciones, ápsides, oposiciones…): grupos {titulo, aviso, filas:[{jdUtc, etiqueta, dato}]}
  if (cfg.eventos) {
    const grupos = cfg.eventos({ sol, sis, reloj });
    $("eventos").innerHTML = grupos.map((g, gi) => `<details><summary>${g.titulo} (${g.filas.length})</summary><p class="aviso">${g.aviso || ""}</p>
      <div class="lista" style="max-height:240px"><table class="tabla"><tbody>${g.filas.map((f, i) => `<tr><td><button data-g="${gi}" data-i="${i}" title="Ir a este instante">${formatoUtc(f.jdUtc, false).replace(" UTC", "")}</button></td><td>${f.etiqueta}</td><td>${f.dato || ""}</td></tr>`).join("")}</tbody></table></div></details>`).join("");
    $("eventos").addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; reloj.fijar(grupos[+b.dataset.g].filas[+b.dataset.i].jdUtc); reloj.activo = false; $("bPlay").textContent = "▶"; });
  }

  // metadatos
  const resumen = (s) => { const c = s.meta.cuerpos; const peor = c.reduce((m, x) => (x.error_max_km > m.error_max_km ? x : m), c[0]); return `${s.nombre}: ${c.length} cuerpos; error máximo de interpolación ${fmt(peor.error_max_km, 2)} km (${peor.nombre}).`; };
  $("meta").innerHTML = html`<p>${resumen(sol)}<br>${esSol ? "" : resumen(sis)}</p>
    <p>Marco: eclíptica y equinoccio J2000 (ICRF), coordenadas geométricas, centro ${esSol ? "el Sol" : "el planeta"}; escala TDB mostrada en UTC (TDB − UTC = 69,184 s fijo). Rejilla regular + Lagrange de 10 puntos.</p>
    <p>Soporte: 2027-01-01 a 2050-12-31. Fuente: NASA/JPL Horizons API v1.2, descarga con <code>herramientas/efemerides/generar_efemerides.py</code>.</p>`;

  // estado desde la URL
  const m = /f=([0-9T:-]+)/.exec(location.hash); if (m) { const jd = jdUtcDesdeInput(m[1]); if (jd) reloj.fijar(jd); }
  const mo = /o=([0-9A-Za-z]+)/.exec(location.hash);
  vista.enfocar(esSol ? solObj : central, cfg.distInicial);
  vista.cam.dist = vista.cam.distObj = cfg.distInicial;
  if (cfg.camara) Object.assign(vista.cam, cfg.camara);
  actualizar(); pintarLista();
  const inicial = (mo && vista.porId.get(mo[1])) || (cfg.seleccionInicial ? vista.porId.get(cfg.seleccionInicial) : null) || central;
  seleccionar(inicial);
  if (cfg.inicio) cfg.inicio({ vista, reloj, objetos, central, solObj });
  vista.umbralEtiquetas = cfg.umbralEtiquetas ?? 0;

  // ---------------------------------------------------------------- bucle
  let ultimaFicha = 0;
  function cuadro(ahora) {
    reloj.paso(ahora);
    actualizar();
    if (ahora - ultimaFicha > 400) {
      ultimaFicha = ahora;
      pintarFicha();
      $("fecha").textContent = formatoUtc(reloj.jdUtc);
      $("sub").textContent = `JD TDB ${reloj.jdTdb.toFixed(5)} · ${vista.ampliacion === 1 ? "tamaños reales" : "tamaños ×" + vista.ampliacion} · velocidad ${VELOCIDADES.find((v) => v[1] === Math.abs(reloj.velocidad))?.[0] || ""}${reloj.velocidad < 0 ? " (inversa)" : ""}`;
      if (document.activeElement !== $("iFecha")) $("iFecha").value = valorInputUtc(reloj.jdUtc);
    }
    vista.dibujar(reloj.jdTdb);
    requestAnimationFrame(cuadro);
  }
  requestAnimationFrame(cuadro);
  window.__sim = { vista, reloj, objetos, sol, sis, geo }; // para depuración y pruebas
}
