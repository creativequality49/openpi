#!/usr/bin/env python3
"""Remove the open-claw Codex skill directory if present."""

from pathlib import Path
import os
import shutil

codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
skills_dir = codex_home / "skills"
candidates = ["open-claw", "open_claw", "open claw"]

removed = []
for name in candidates:
    path = skills_dir / name
    if path.exists():
        shutil.rmtree(path)
        removed.append(path)

if removed:
    print("Removed:")
    for path in removed:
        print(f"- {path}")
else:
    print("open-claw is already not installed.")
