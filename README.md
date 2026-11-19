# YouTube Stream Downloader & Clipper

Lightweight command-line Python tools to download the best available YouTube video/audio streams as `.mkv` files and extract frame-accurate `.mp4` clips using `yt-dlp` and FFmpeg.

## Prerequisites

* **Python 3.10+** (tested on Python 3.14)
* **FFmpeg** installed and available in your system `PATH`

## Setup

1. Clone the repository and navigate into the project folder:
   ```bash
   git clone git@github.com:KingDDD/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Download a Stream (`download_stream.py`)

**Pass a URL directly:**
```bash
./download_stream.py "https://youtube.com..."
```

**Or run interactively (prompts for a URL):**
```bash
./download_stream.py
```

### 2. Create Clips (`clip_video.py`)

**Extract a clip using start and end timestamps (`HH:MM:SS`):**
```bash
./clip_video.py "video.mkv" 00:01:30 00:02:15
```

**Specify a custom output filename (saved inside `clips/`):**
```bash
./clip_video.py "video.mkv" 00:01:30 00:02:15 -o highlight.mp4
```

**View CLI options for either script:**
```bash
./download_stream.py -h
./clip_video.py -h
```

## Notes

* Downloaded `.mkv` files are saved in the root directory alongside the scripts without overwriting existing files.
* Extracted `.mp4` clips are saved automatically into the `clips/` folder using video stream copy (`-c:v copy`) and AAC audio (`-c:a aac`) for fast, lossless video cuts.
* Both `clips/` and downloaded media files are excluded from version control via `.gitignore`.
