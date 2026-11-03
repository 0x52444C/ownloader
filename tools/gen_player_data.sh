#!/bin/sh
# Produce a complete, ready-to-import data/ folder from your own legally-owned copy of the
# arcade's original data, for a bring-your-own-assets client, or anyone
# else who wants this repo's data/ without hand-running every command in README.md.
#
# This is NOT tools/gen_from_original.sh: that one (Step 1 in README.md) regenerates the app's
# own *source code* (src/*.h, the recompiled physics) - useful only if you're building the app
# yourself. This script does README's Step 2 (the actual game assets, into data/) plus the two
# data/ outputs gen_from_original.sh produces as a side effect (data/phys.img, data/minicourse.wpk)
# and one raw copy README.md never mentions (data/carconfig, read directly by src/car.c at
# runtime). Together these are everything the app's importer checks for and everything the game
# reads back out of data/ at runtime.
#
# This is still a real developer toolchain, not a one-click converter: see README.md's "Tools
# you need" (Python 3 with capstone, unicorn, pillow, numpy; c++filt; a C compiler; ffmpeg with
# the Bink decoder). There is no way around that while the conversion runs locally - it statically
# recompiles part of the original executable. Expect this to take a while (the Tokyo map and the
# full car roster are the slow parts) and several GB of free disk.
#
# Usage: tools/gen_player_data.sh [arcade root]
#   arcade root: the folder that has `main` and `data/` (default: the folder next to this
#   repository, "../Original Game Data", same as README.md's Setup).
#   Always writes into this repo's own data/ (every packer's own default, and what
#   prepare_sound.sh/prepare_bgm.sh/prepare_movie.sh hardcode regardless): zip that folder, or
#   point the app's importer straight at it.
#
# A different arcade root only partly works: pack_tokyo.sh, pack_traffic.sh and pack_car.sh
# hardcode the sibling-folder path above and ignore this script's argument entirely (same
# limitation as upstream, not something this script papers over) - so an override here still
# needs the arcade original to ALSO sit at that sibling location for the Tokyo map, traffic and
# the starter FD3S to pack correctly.
set -e
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
ORIG="../Original Game Data"
[ -n "$1" ] && ORIG="$1"
ORIG="$(cd "$ORIG" && pwd)"
MAIN="$ORIG/main"
D="$ORIG/data"
[ -f "$MAIN" ] || { echo "no arcade main at $MAIN" >&2; exit 1; }

SIBLING="$(cd "$ROOT/.." 2>/dev/null && pwd)/Original Game Data"
if [ "$ORIG" != "$SIBLING" ]; then
  echo "note: $ORIG is not the sibling folder ($SIBLING)." >&2
  echo "      pack_tokyo.sh, pack_traffic.sh and pack_car.sh ignore this script's argument and" >&2
  echo "      will still read from the sibling folder - put your copy there too, or those three" >&2
  echo "      steps (the Tokyo map, traffic and the starter FD3S) will fail." >&2
fi

run() { echo "  $*"; "$@"; }
mkdir -p data

echo "step 1's data/ side effects (phys.img, minicourse.wpk)..."
run sh tools/gen_from_original.sh "$ORIG" --phys

echo "car configs (raw copy, read directly at runtime - not produced by any packer)..."
mkdir -p data/carconfig
cp "$D"/carconfig/*.txt data/carconfig/

echo "Tokyo (day and night)..."
run sh tools/stage/pack_tokyo.sh daytime "$ROOT/data/tokyo.wpk"
run sh tools/stage/pack_tokyo.sh night "$ROOT/data/tokyo_night.wpk"

echo "the other cities..."
for city in oosaka hakone nagoya fukuoka; do
  for time in daytime night; do
    run python3 tools/stage/pack_city.py "$D" "$city" "$time" data
  done
done

echo "street and building lights..."
run python3 tools/stage/pack_lights.py "$D" data

echo "under neons..."
run python3 tools/stage/pack_neon.py "$D" data/neon.wpk

echo "cars (this is the slow one)..."
run python3 tools/stage/pack_cars.py "$ORIG" data/cars
for aero in a b c; do
  run python3 tools/stage/pack_cars.py "$ORIG" data/cars --aero "$aero"
done
run python3 tools/stage/pack_cars.py "$ORIG" data/wheels --wheels
run python3 tools/stage/pack_cars.py "$ORIG" data/chara --chara

echo "stickers..."
run python3 tools/stage/pack_vinyl.py "$ORIG" data/vinyl

echo "traffic..."
run sh tools/stage/pack_traffic.sh "$ROOT/data/traffic"

echo "starter car (FD3S)..."
run sh tools/stage/pack_car.sh 1 "$ROOT/data/fd3s.wpk"

echo "race HUD and meters..."
run python3 tools/hudpack.py "$D/sprite" "$MAIN" data

echo "minimap..."
run python3 tools/navipack.py "$D" "$MAIN" data

echo "menus..."
[ -f tools/vsdisc/icon_0.png ] || run python3 tools/vsdiscs.py "$D/sprite"
run python3 tools/menupack.py "$ORIG" data/menu.bin

echo "sound effects, BGM, movies..."
run sh prepare_sound.sh
run sh prepare_bgm.sh
run sh prepare_movie.sh

echo "manifest (for the app's network import option)..."
run python3 tools/gen_manifest.py data

echo "done - data/ is ready to import (zip it for another device, or serve it"
echo "over HTTP - e.g. 'cd data && python3 -m http.server 8000' - and use the app's"
echo "'Download from Server...' option with this machine's address)."
