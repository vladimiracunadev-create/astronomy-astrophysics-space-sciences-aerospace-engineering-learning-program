# SPDX-License-Identifier: Apache-2.0
"""Empaqueta la aplicación de Windows (portable): lanzador .exe + sitio HTML sin conexión.

El lanzador abre el sitio en una ventana de aplicación de Microsoft Edge (instalado de serie en Windows 10/11)
o de Google Chrome, con su propio perfil; si no hay ninguno, lo abre en el navegador predeterminado.
Se compila con el compilador de C# incluido en Windows (.NET Framework 4), sin instalar nada.

Uso: python herramientas/publicacion/windows.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import *  # noqa: E402,F401,F403

CSC = Path("C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe")
NOMBRE = "ProgramaAeroespacial"

LANZADOR = r"""
using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;

static class Lanzador
{
    [STAThread]
    static void Main()
    {
        string dir = AppDomain.CurrentDomain.BaseDirectory;
        string indice = Path.Combine(dir, "web", "index.html");
        if (!File.Exists(indice))
        {
            MessageBox.Show("No se encuentra la carpeta 'web' junto al programa.\nVuelve a extraer el archivo ZIP completo.",
                "Programa Aeroespacial", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }
        string uri = new Uri(indice).AbsoluteUri;
        string pf = Environment.GetFolderPath(Environment.SpecialFolder.ProgramFiles);
        string pf86 = Environment.GetFolderPath(Environment.SpecialFolder.ProgramFilesX86);
        string local = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
        string[] candidatos = {
            Path.Combine(pf86, @"Microsoft\Edge\Application\msedge.exe"),
            Path.Combine(pf, @"Microsoft\Edge\Application\msedge.exe"),
            Path.Combine(pf, @"Google\Chrome\Application\chrome.exe"),
            Path.Combine(pf86, @"Google\Chrome\Application\chrome.exe"),
            Path.Combine(local, @"Google\Chrome\Application\chrome.exe")
        };
        string perfil = Path.Combine(local, "ProgramaAeroespacial", "perfil");
        foreach (string exe in candidatos)
        {
            if (File.Exists(exe))
            {
                Process.Start(new ProcessStartInfo(exe,
                    "--app=\"" + uri + "\" --user-data-dir=\"" + perfil + "\" --window-size=1200,860 --no-first-run --no-default-browser-check")
                { UseShellExecute = false });
                return;
            }
        }
        Process.Start(new ProcessStartInfo(indice) { UseShellExecute = true });
    }
}
"""

LEEME = f"""PROGRAMA AEROESPACIAL (versión {VERSION}) - lector sin conexión para Windows
================================================================================

{TITULO}

CÓMO USARLO
1. Extrae TODO el contenido del ZIP en una carpeta (por ejemplo, C:\\Programa-Aeroespacial).
2. Abre "{NOMBRE}.exe". Se abre una ventana de aplicación con el programa.
   (Usa Microsoft Edge o Google Chrome ya instalados; si no hay ninguno, se abre en tu navegador.)
3. Usa la barra superior: Inicio, Buscar, Áreas, Roles, Anexos y Glosario.

NO REQUIERE conexión a Internet ni instalación. Para desinstalar, borra la carpeta.
Windows SmartScreen puede avisar porque el programa no está firmado digitalmente: es normal en esta versión.

CONTENIDO
- 12 áreas, 133 bloques, 2.077 clases redactadas, 24 roles, 20 anexos y glosarios (esencial y completo).
- Los PDF (general, por área y por rol) se publican aparte en la misma página de la versión.

AVISO
{AVISO}

Licencia del contenido: CC BY-NC-SA 4.0 (ver web\\LICENSE-CONTENT.html). Código: Apache-2.0.
"""


def icono(destino: Path):
    from PIL import Image, ImageDraw
    n = 256
    im = Image.new("RGBA", (n, n), (13, 27, 62, 255))
    d = ImageDraw.Draw(im)
    d.ellipse((n * .17, n * .17, n * .83, n * .83), outline=(121, 184, 255, 255), width=8)
    d.ellipse((n * .32, n * .32, n * .68, n * .68), fill=(255, 205, 80, 255))
    d.ellipse((n * .66, n * .22, n * .76, n * .32), fill=(240, 240, 255, 255))
    im.save(destino, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])


def construir():
    assert CSC.exists(), CSC
    trabajo = BUILD / "windows"
    if trabajo.exists():
        shutil.rmtree(trabajo)
    trabajo.mkdir(parents=True)
    (trabajo / "Lanzador.cs").write_text(LANZADOR, encoding="utf-8")
    icono(trabajo / "icono.ico")
    exe = trabajo / f"{NOMBRE}.exe"
    r = subprocess.run([str(CSC), "/nologo", "/target:winexe", f"/out:{exe}", f"/win32icon:{trabajo / 'icono.ico'}",
                        "/reference:System.Windows.Forms.dll", "/optimize+", str(trabajo / "Lanzador.cs")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        sys.exit(1)
    DIST.mkdir(parents=True, exist_ok=True)
    raiz = f"Programa-Aeroespacial_v{VERSION}_Windows"
    salida = DIST / f"{raiz}.zip"
    with zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        z.write(exe, f"{raiz}/{NOMBRE}.exe")
        z.writestr(f"{raiz}/LEEME.txt", LEEME.replace("\n", "\r\n"))
        for p in sorted(WEB.rglob("*")):
            if p.is_file():
                z.write(p, f"{raiz}/web/{p.relative_to(WEB).as_posix()}")
    print(f"Windows: {salida} ({salida.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    construir()
