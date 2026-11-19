# YouTube Replay Downloader

A lightweight command-line Python script to download the best available video and audio streams from a YouTube URL and merge them into a single `.mkv` file using `yt-dlp` and FFmpeg.

## Prerequisites

* **Python 3.8+**
* **FFmpeg** installed and available in your system `PATH`

## Setup

1. Clone the repository and navigate into the project folder:
   ```bash
   git clone <your-repo-url>
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

**Pass a URL directly:**
```bash
./<script_name>.py "https://youtube.com..."
```

**Or run interactively (prompts for a URL):**
```bash
./<script_name>.py
```

**View help and options:**
```bash
./<script_name>.py -h
```

## Notes

* Downloaded `.mkv` files are saved automatically in the same directory as the script.
* Existing files are not overwritten (`overwrites: False`), and interrupted downloads can resume automatically.
