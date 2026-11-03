# Player data tools

Converts your own legally-owned copy of the original arcade game into a `data/` folder an
associated client app can import. This is just the conversion tooling - no app source, no
build scripts, nothing else.

## What you need

1. **This folder**, as-is.
2. **Your own original game dump**, as a folder named `Original Game Data` sitting right next
   to this one (a sibling, not inside it):
   ```
   some folder/
     Original Game Data/     <- your own copy, containing `main` and `data/`
     ownloader/               <- this folder
   ```
   If you don't have that yet, this toolset doesn't produce it for you - it only converts a
   copy you already own.
3. **A computer**, not a phone or tablet - this step needs real developer tools and won't run
   on iOS or Android.
4. **Free disk space**: a few GB for the original data, a few GB more for the converted output.

## Step 1: install the dependencies

macOS (with [Homebrew](https://brew.sh)):
```sh
brew install python3 binutils ffmpeg
pip3 install capstone unicorn pillow numpy
```

Linux (Debian/Ubuntu):
```sh
sudo apt install python3 python3-pip binutils ffmpeg
pip3 install capstone unicorn pillow numpy
```

You also need a C compiler (`cc`) - already present on macOS (Xcode Command Line Tools:
`xcode-select --install`) and on most Linux installs (`sudo apt install build-essential` if
not).

## Step 2: run the conversion

From inside this folder:
```sh
sh tools/gen_player_data.sh
```

This takes a while - the car roster and the physics recompilation step are the slow parts.
Progress prints as it goes (`the Tokyo map...`, `cars (this is the slow one)...`, etc.), so if
it looks stalled for a minute on that step, that's normal.

When it finishes, you'll have a `data/` folder right here, with everything the app needs
inside it, including `data/manifest.json` (a plain list of every file - see Step 3).

If it stops partway with an error, re-running the same command picks up roughly where it left
off (files already converted aren't redone) rather than starting over.

## Step 3: get `data/` onto your device

The app's "first launch" screen has two ways to bring that folder in - pick whichever's easier:

**A) Copy it directly onto the device**, then use the app's "Choose Data Folder…" button:
- iOS: AirDrop the `data` folder to the device, or put it in iCloud Drive/Files.
- Android: copy it over USB, or upload to Google Drive/a cloud folder and download it on the
  device.

**B) Serve it over your network**, then use the app's "Download from Server…" button:
```sh
cd data
python3 -m http.server 8000
```
Then on the device (same Wi-Fi), enter this computer's IP address and port in the app, e.g.
`192.168.1.50:8000`. This needs `data/manifest.json` to be sitting next to the files it
describes - Step 2 already wrote it there, so no extra step is needed.

Either way, the app copies it in with a progress bar and launches straight into the game once
it's verified - no further setup.
