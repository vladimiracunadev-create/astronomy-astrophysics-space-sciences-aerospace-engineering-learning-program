#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Regenera el manifiesto SHA-256 de los archivos versionables del programa."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "MANIFIESTO_SHA256.txt"
EXCLUDED_PARTS = {".git", ".claude", "__pycache__"}
EXCLUDED_NAMES = {OUTPUT.name}


def versionable_files() -> list[Path]:
    return sorted(
        (
            path
            for path in ROOT.rglob("*")
            if path.is_file()
            and path.name not in EXCLUDED_NAMES
            and not EXCLUDED_PARTS.intersection(path.relative_to(ROOT).parts)
        ),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    lines = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in versionable_files()
    ]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Manifiesto actualizado: {len(lines)} archivos")


if __name__ == "__main__":
    main()
