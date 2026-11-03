#!/usr/bin/env python3
"""Write data/manifest.json: a flat list of every file under data/ (path relative to data/, and
its size), for the app's network-import option (ImportViewController.m / MainActivity.java's
"Download from Server..."). Run after tools/gen_player_data.sh, or standalone against an
existing data/ folder. Then serve data/ over plain HTTP from the same machine (for example
`cd data && python3 -m http.server 8000`) and enter that machine's address in the app.

usage: gen_manifest.py [data dir]   (default: data, next to this script's repo root)
"""
import json
import os
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
root = os.path.abspath(root)
files = []
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if not d.startswith(".")]
    for name in filenames:
        if name in ("manifest.json",) or name.startswith("."):
            continue
        full = os.path.join(dirpath, name)
        rel = os.path.relpath(full, root).replace(os.sep, "/")
        files.append({"path": rel, "size": os.path.getsize(full)})
files.sort(key=lambda f: f["path"])
out = os.path.join(root, "manifest.json")
with open(out, "w") as f:
    json.dump({"files": files}, f)
total = sum(f["size"] for f in files)
print("%s: %d files, %.1f GB" % (out, len(files), total / 1e9))
