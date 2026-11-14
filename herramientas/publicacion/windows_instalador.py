# SPDX-License-Identifier: Apache-2.0
"""Instalador de Windows (Setup.exe) del programa, además del ZIP portable.

Compila con el compilador de C# incluido en Windows (.NET Framework 4, sin instalar nada) un instalador de un solo archivo que lleva incrustado
el paquete portable (`windows.py`). Instala **por usuario** (no pide permisos de administrador) en `%LocalAppData%\\Programs\\Programa Aeroespacial`,
crea accesos directos en el menú Inicio (y, si se elige, en el escritorio) y se registra en «Aplicaciones instaladas» con su desinstalador.

Uso: python herramientas/publicacion/windows_instalador.py          (requiere haber ejecutado antes windows.py)
Opciones del instalador: `/S` instalación silenciosa, `/D=<carpeta>` carpeta de destino, `/escritorio` acceso directo en el escritorio,
`/desinstalar` desinstala (con `/S` sin preguntar).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import *  # noqa: E402,F401,F403
from windows import CSC, NOMBRE, icono  # noqa: E402

CODIGO = r"""
using System;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Reflection;
using System.Windows.Forms;
using Microsoft.Win32;

static class Instalador
{
    const string Nombre = "Programa Aeroespacial";
    const string Version = "@VERSION@";
    const string Exe = "@EXE@";
    const string Clave = @"Software\Microsoft\Windows\CurrentVersion\Uninstall\ProgramaAeroespacial";

    static string DestinoPorDefecto()
    {
        return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "Programs", Nombre);
    }
    static string MenuInicio()
    {
        return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.Programs), Nombre + ".lnk");
    }
    static string Escritorio()
    {
        return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory), Nombre + ".lnk");
    }

    static void Acceso(string lnk, string destino, string trabajo, string icono)
    {
        Type t = Type.GetTypeFromProgID("WScript.Shell");
        object sh = Activator.CreateInstance(t);
        object a = t.InvokeMember("CreateShortcut", BindingFlags.InvokeMethod, null, sh, new object[] { lnk });
        Type ta = a.GetType();
        ta.InvokeMember("TargetPath", BindingFlags.SetProperty, null, a, new object[] { destino });
        ta.InvokeMember("WorkingDirectory", BindingFlags.SetProperty, null, a, new object[] { trabajo });
        ta.InvokeMember("IconLocation", BindingFlags.SetProperty, null, a, new object[] { icono });
        ta.InvokeMember("Description", BindingFlags.SetProperty, null, a, new object[] { Nombre });
        ta.InvokeMember("Save", BindingFlags.InvokeMethod, null, a, null);
    }

    static void Instalar(string dir, bool escritorio, Action<int> progreso)
    {
        Directory.CreateDirectory(dir);
        string raiz = Path.GetFullPath(dir).TrimEnd('\\') + "\\";
        using (Stream s = Assembly.GetExecutingAssembly().GetManifestResourceStream("paquete.zip"))
        using (ZipArchive z = new ZipArchive(s, ZipArchiveMode.Read))
        {
            int n = 0, total = z.Entries.Count;
            foreach (ZipArchiveEntry e in z.Entries)
            {
                n++;
                int barra = e.FullName.IndexOf('/');
                string rel = barra >= 0 ? e.FullName.Substring(barra + 1) : e.FullName;   // quita la carpeta raíz del ZIP portable
                if (rel.Length == 0) continue;
                string destino = Path.GetFullPath(Path.Combine(dir, rel.Replace('/', '\\')));
                if (!destino.StartsWith(raiz, StringComparison.OrdinalIgnoreCase)) continue;  // nunca escribe fuera de la carpeta
                if (rel.EndsWith("/")) { Directory.CreateDirectory(destino); continue; }
                Directory.CreateDirectory(Path.GetDirectoryName(destino));
                e.ExtractToFile(destino, true);
                if (n % 200 == 0 && progreso != null) progreso(100 * n / total);
            }
        }
        string desinstalador = Path.Combine(dir, "Desinstalar.exe");
        File.Copy(Assembly.GetExecutingAssembly().Location, desinstalador, true);
        string exe = Path.Combine(dir, Exe);
        Acceso(MenuInicio(), exe, dir, exe + ",0");
        if (escritorio) Acceso(Escritorio(), exe, dir, exe + ",0");
        using (RegistryKey k = Registry.CurrentUser.CreateSubKey(Clave))
        {
            k.SetValue("DisplayName", Nombre);
            k.SetValue("DisplayVersion", Version);
            k.SetValue("Publisher", "Programa Aeroespacial");
            k.SetValue("InstallLocation", dir);
            k.SetValue("DisplayIcon", exe + ",0");
            k.SetValue("UninstallString", "\"" + desinstalador + "\" /desinstalar");
            k.SetValue("NoModify", 1, RegistryValueKind.DWord);
            k.SetValue("NoRepair", 1, RegistryValueKind.DWord);
        }
        if (progreso != null) progreso(100);
    }

    static void Desinstalar(bool silencioso)
    {
        string dir = null;
        using (RegistryKey k = Registry.CurrentUser.OpenSubKey(Clave)) { if (k != null) dir = k.GetValue("InstallLocation") as string; }
        if (dir == null) dir = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
        if (!silencioso && MessageBox.Show("¿Desinstalar " + Nombre + " de " + dir + "?", Nombre, MessageBoxButtons.YesNo, MessageBoxIcon.Question) != DialogResult.Yes) return;
        try { File.Delete(MenuInicio()); } catch { }
        try { File.Delete(Escritorio()); } catch { }
        try { Registry.CurrentUser.DeleteSubKeyTree(Clave, false); } catch { }
        string perfil = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "ProgramaAeroespacial");
        // el desinstalador vive dentro de la carpeta: se borra desde un proceso aparte cuando este termina
        ProcessStartInfo p = new ProcessStartInfo("cmd.exe", "/c ping 127.0.0.1 -n 3 >nul & rmdir /s /q \"" + dir + "\" & rmdir /s /q \"" + perfil + "\"");
        p.CreateNoWindow = true; p.UseShellExecute = false;
        Process.Start(p);
        if (!silencioso) MessageBox.Show(Nombre + " se ha desinstalado.", Nombre, MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    [STAThread]
    static int Main(string[] args)
    {
        bool silencioso = false, escritorio = false, desinstalar = false;
        string dir = DestinoPorDefecto();
        foreach (string a in args)
        {
            if (a.Equals("/S", StringComparison.OrdinalIgnoreCase)) silencioso = true;
            else if (a.Equals("/escritorio", StringComparison.OrdinalIgnoreCase)) escritorio = true;
            else if (a.Equals("/desinstalar", StringComparison.OrdinalIgnoreCase)) desinstalar = true;
            else if (a.StartsWith("/D=", StringComparison.OrdinalIgnoreCase)) dir = a.Substring(3).Trim('"');
        }
        if (desinstalar) { Desinstalar(silencioso); return 0; }
        if (silencioso) { try { Instalar(dir, escritorio, null); return 0; } catch (Exception ex0) { Console.Error.WriteLine(ex0.Message); return 1; } }

        Application.EnableVisualStyles();
        Form f = new Form();
        f.Text = "Instalar " + Nombre + " " + Version; f.Width = 560; f.Height = 300; f.StartPosition = FormStartPosition.CenterScreen;
        f.FormBorderStyle = FormBorderStyle.FixedDialog; f.MaximizeBox = false;
        Label t = new Label(); t.Text = Nombre + " " + Version + "\nLector sin conexión del programa (no requiere permisos de administrador)."; t.Left = 16; t.Top = 14; t.Width = 510; t.Height = 44; f.Controls.Add(t);
        Label l = new Label(); l.Text = "Carpeta de instalación:"; l.Left = 16; l.Top = 70; l.Width = 300; f.Controls.Add(l);
        TextBox c = new TextBox(); c.Text = dir; c.Left = 16; c.Top = 92; c.Width = 420; f.Controls.Add(c);
        Button b = new Button(); b.Text = "Examinar…"; b.Left = 444; b.Top = 90; b.Width = 84;
        b.Click += delegate { FolderBrowserDialog d = new FolderBrowserDialog(); if (d.ShowDialog() == DialogResult.OK) c.Text = Path.Combine(d.SelectedPath, Nombre); };
        f.Controls.Add(b);
        CheckBox e = new CheckBox(); e.Text = "Crear acceso directo en el escritorio"; e.Left = 16; e.Top = 128; e.Width = 400; e.Checked = true; f.Controls.Add(e);
        ProgressBar pb = new ProgressBar(); pb.Left = 16; pb.Top = 166; pb.Width = 512; pb.Height = 18; f.Controls.Add(pb);
        Button ok = new Button(); ok.Text = "Instalar"; ok.Left = 340; ok.Top = 208; ok.Width = 90; f.Controls.Add(ok);
        Button no = new Button(); no.Text = "Cancelar"; no.Left = 438; no.Top = 208; no.Width = 90; no.Click += delegate { f.Close(); }; f.Controls.Add(no);
        ok.Click += delegate
        {
            ok.Enabled = false; no.Enabled = false; f.Cursor = Cursors.WaitCursor;
            try
            {
                Instalar(c.Text, e.Checked, delegate (int p) { pb.Value = Math.Min(100, p); Application.DoEvents(); });
                f.Cursor = Cursors.Default;
                if (MessageBox.Show("Instalación terminada. ¿Abrir " + Nombre + " ahora?", Nombre, MessageBoxButtons.YesNo, MessageBoxIcon.Information) == DialogResult.Yes)
                    Process.Start(new ProcessStartInfo(Path.Combine(c.Text, Exe)) { UseShellExecute = true, WorkingDirectory = c.Text });
                f.Close();
            }
            catch (Exception ex) { f.Cursor = Cursors.Default; MessageBox.Show("No se pudo instalar: " + ex.Message, Nombre, MessageBoxButtons.OK, MessageBoxIcon.Error); ok.Enabled = true; no.Enabled = true; }
        };
        Application.Run(f);
        return 0;
    }
}
"""


def construir():
    zip_portable = DIST / f"Programa-Aeroespacial_v{VERSION}_Windows.zip"
    assert zip_portable.exists(), f"falta {zip_portable}: ejecute antes windows.py"
    trabajo = BUILD / "windows-instalador"
    trabajo.mkdir(parents=True, exist_ok=True)
    (trabajo / "Instalador.cs").write_text(CODIGO.replace("@VERSION@", VERSION).replace("@EXE@", f"{NOMBRE}.exe"), encoding="utf-8")
    icono(trabajo / "icono.ico")
    salida = DIST / f"Programa-Aeroespacial_v{VERSION}_Windows_Setup.exe"
    r = subprocess.run([str(CSC), "/nologo", "/target:winexe", f"/out:{salida}", f"/win32icon:{trabajo / 'icono.ico'}",
                        f"/resource:{zip_portable},paquete.zip", "/reference:System.Windows.Forms.dll",
                        "/reference:System.IO.Compression.dll", "/reference:System.IO.Compression.FileSystem.dll", "/optimize+",
                        str(trabajo / "Instalador.cs")], capture_output=True)
    if r.returncode != 0:
        print(r.stdout.decode("cp850", errors="replace"), r.stderr.decode("cp850", errors="replace"))
        sys.exit(1)
    print(f"Windows (instalador): {salida} ({salida.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    construir()
