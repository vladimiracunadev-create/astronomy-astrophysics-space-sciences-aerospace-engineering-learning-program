# SPDX-License-Identifier: Apache-2.0
"""Construye el APK de Android (lector sin conexión) con las herramientas del SDK, sin Gradle.

La aplicación es un WebView que abre el sitio HTML (build/web) empaquetado en los assets.
Requisitos: Android SDK (build-tools, platform android-34) y un JDK (el de Android Studio sirve).

Uso: python herramientas/publicacion/android.py
La clave de firma se crea una vez fuera del repositorio (~/.android/programa-aeroespacial-release.*).
"""
from __future__ import annotations

import os
import secrets
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import *  # noqa: E402,F401,F403

PAQUETE = "io.github.vladimiracunadev.programa"
NOMBRE_APP = "Programa Aeroespacial"
SDK = Path(os.environ.get("ANDROID_HOME") or os.environ.get("LOCALAPPDATA", "") + "/Android/Sdk")
JBR = Path("C:/Program Files/Android/Android Studio/jbr/bin")
COMPILE = 34
MINSDK = 24

MANIFEST = f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="{PAQUETE}">
    <application android:label="{NOMBRE_APP}" android:icon="@drawable/ic_launcher" android:allowBackup="false"
        android:theme="@android:style/Theme.DeviceDefault.NoActionBar" android:supportsRtl="true">
        <activity android:name=".MainActivity" android:exported="true" android:configChanges="orientation|screenSize|keyboardHidden|smallestScreenSize|screenLayout">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
"""

ACTIVIDAD = """package %s;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView web;

    @Override
    protected void onCreate(Bundle estado) {
        super.onCreate(estado);
        web = new WebView(this);
        setContentView(web);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setAllowFileAccess(true);
        s.setBuiltInZoomControls(true);
        s.setDisplayZoomControls(false);
        s.setSupportZoom(true);
        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView v, WebResourceRequest r) {
                Uri u = r.getUrl();
                String esquema = u.getScheme();
                if ("http".equals(esquema) || "https".equals(esquema) || "mailto".equals(esquema)) {
                    startActivity(new Intent(Intent.ACTION_VIEW, u));
                    return true;
                }
                return false;
            }
        });
        if (estado != null) {
            web.restoreState(estado);
        } else {
            web.loadUrl("file:///android_asset/web/index.html");
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle salida) {
        super.onSaveInstanceState(salida);
        web.saveState(salida);
    }

    @Override
    public void onBackPressed() {
        if (web.canGoBack()) {
            web.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
""" % PAQUETE


def ejecutar(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print("COMANDO FALLÓ:", " ".join(map(str, cmd))[:300])
        print(r.stdout[-1500:], r.stderr[-2500:])
        sys.exit(1)
    return r


def icono(destino: Path):
    from PIL import Image, ImageDraw
    n = 432
    im = Image.new("RGB", (n, n), (13, 27, 62))
    d = ImageDraw.Draw(im)
    d.ellipse((n * .17, n * .17, n * .83, n * .83), outline=(121, 184, 255), width=10)
    d.ellipse((n * .32, n * .32, n * .68, n * .68), fill=(255, 205, 80))
    d.ellipse((n * .66, n * .22, n * .76, n * .32), fill=(240, 240, 255))
    destino.parent.mkdir(parents=True, exist_ok=True)
    im.save(destino)


def clave():
    base = Path.home() / ".android"
    base.mkdir(exist_ok=True)
    jks = base / "programa-aeroespacial-release.jks"
    pw = base / "programa-aeroespacial-release.pass"
    if not jks.exists():
        pw.write_text(secrets.token_urlsafe(24), encoding="utf-8")
        ejecutar([str(JBR / "keytool.exe"), "-genkeypair", "-keystore", str(jks), "-alias", "programa", "-keyalg", "RSA",
                  "-keysize", "4096", "-validity", "9125", "-storepass:file", str(pw), "-keypass:file", str(pw),
                  "-dname", "CN=Programa Aeroespacial, O=Programa Integral de Astronomia y Ciencias Espaciales, C=CL"])
        print(f"Clave de firma creada en {jks} (haz una copia de seguridad: sin ella no se pueden publicar actualizaciones)")
    return jks, pw


def construir():
    bt = sorted((SDK / "build-tools").iterdir())[-1]
    android_jar = SDK / "platforms" / f"android-{COMPILE}" / "android.jar"
    assert android_jar.exists(), android_jar
    # ruta corta: Windows limita las rutas a 260 caracteres y el sitio tiene carpetas profundas
    trabajo = Path(tempfile.gettempdir()) / "programa-ap"
    if trabajo.exists():
        shutil.rmtree(trabajo)
    (trabajo / "res").mkdir(parents=True)
    src = trabajo / "src" / Path(*PAQUETE.split("."))
    src.mkdir(parents=True)
    (src / "MainActivity.java").write_text(ACTIVIDAD, encoding="utf-8")
    (trabajo / "AndroidManifest.xml").write_text(MANIFEST, encoding="utf-8")
    icono(trabajo / "res" / "drawable" / "ic_launcher.png")

    # 1) recursos
    flata = trabajo / "recursos.zip"
    ejecutar([str(bt / "aapt2.exe"), "compile", "--dir", str(trabajo / "res"), "-o", str(flata)])
    # 2) enlazar (manifiesto, recursos y assets)
    assets = trabajo / "assets"
    assets.mkdir()
    shutil.copytree(WEB, assets / "web")
    base_apk = trabajo / "base.apk"
    ejecutar([str(bt / "aapt2.exe"), "link", "-o", str(base_apk), "-I", str(android_jar), "--manifest", str(trabajo / "AndroidManifest.xml"),
              "-A", str(assets), "--min-sdk-version", str(MINSDK), "--target-sdk-version", str(COMPILE),
              "--version-code", "1", "--version-name", VERSION, "--rename-manifest-package", PAQUETE, str(flata)])
    # 3) compilar Java y pasar a dex
    clases = trabajo / "clases"
    clases.mkdir()
    ejecutar([str(JBR / "javac.exe"), "--release", "8", "-cp", str(android_jar), "-d", str(clases), str(src / "MainActivity.java")])
    jar_clases = [str(p) for p in clases.rglob("*.class")]
    dex = trabajo / "dex"
    dex.mkdir()
    ejecutar(["cmd", "/c", str(bt / "d8.bat"), "--lib", str(android_jar), "--min-api", str(MINSDK), "--output", str(dex)] + jar_clases)
    # 4) añadir classes.dex al APK
    sin_firmar = trabajo / "sin-firmar.apk"
    with zipfile.ZipFile(base_apk) as zin, zipfile.ZipFile(sin_firmar, "w", zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            zout.writestr(it, zin.read(it.filename), compress_type=it.compress_type)
        zout.write(dex / "classes.dex", "classes.dex")
    # 5) alinear y firmar
    alineado = trabajo / "alineado.apk"
    ejecutar([str(bt / "zipalign.exe"), "-p", "-f", "4", str(sin_firmar), str(alineado)])
    jks, pw = clave()
    DIST.mkdir(parents=True, exist_ok=True)
    final = DIST / f"Programa-Aeroespacial_v{VERSION}_Android.apk"
    ejecutar(["cmd", "/c", str(bt / "apksigner.bat"), "sign", "--ks", str(jks), "--ks-pass", f"file:{pw}", "--ks-key-alias", "programa",
              "--min-sdk-version", str(MINSDK), "--out", str(final), str(alineado)])
    ejecutar(["cmd", "/c", str(bt / "apksigner.bat"), "verify", "--verbose", str(final)])
    print(f"APK: {final} ({final.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    construir()
