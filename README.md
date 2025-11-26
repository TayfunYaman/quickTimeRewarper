# Rewarp.py – Simple FFmpeg Rewrap Tool

This script quickly **rewraps (remuxes)** any video file using FFmpeg **without re-encoding**. It preserves full quality and metadata while simply placing the video/audio streams into a fresh container.

This version is **minimal**, **clean**, and **command‑line friendly**.

---

## ✅ Features
- No re-encoding (**copy codec**) → lossless, very fast
- Automatically detects FPS using `ffprobe`
- Preserves metadata
- Simple command-line usage (`python3 rewarp.py input.mov`)
- Outputs automatically to `/output/` folder

---

## 📦 Requirements
Make sure FFmpeg and FFprobe are installed.

### macOS
```bash
brew install ffmpeg
```

### Linux
```bash
sudo apt install ffmpeg
```

### Windows
- Download FFmpeg from the official website
- Add `ffmpeg.exe` and `ffprobe.exe` to PATH

---

## ▶️ Usage
Run the script by passing an input video file:

```bash
python3 rewarp.py input_video.mov
```

### Output
- Results are saved in the **output/** directory
- Output file keeps the same name as input

Example:
```
input:   B004_02152204_C009.mov
output:  output/B004_02152204_C009.mov
```

---

## 🧠 How It Works
1. Script calls `ffprobe` to detect the FPS.
2. FFmpeg is run with:
   - `-c:v copy` (copy video stream)
   - `-c:a copy` (copy audio stream)
   - `-map_metadata 0` (preserve metadata)
   - `-r <fps>` (ensure correct container FPS)
3. Output is placed into `output/` folder.

---

## 🗂 Example Folder Structure
```
project/
├── rewarp.py
├── input.mov
└── output/
    └── input.mov
```


