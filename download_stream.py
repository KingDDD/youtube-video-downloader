#!/usr/bin/env python3

import argparse
from pathlib import Path
import shutil
import sys

import yt_dlp


# Save downloads alongside this script.
OUTPUT_DIR = Path(__file__).resolve().parent


def download_stream(url: str) -> None:
    """Download the best available YouTube replay."""

    if not shutil.which("ffmpeg"):
        raise RuntimeError(
            "FFmpeg not found. Please install FFmpeg "
            "and ensure it is in your PATH."
        )

    options = {
        "format": "bestvideo*+bestaudio/best",
        "outtmpl": str(OUTPUT_DIR / "%(title)s [%(id)s].%(ext)s"),
        "merge_output_format": "mkv",
        "noplaylist": True,
        "retries": 10,
        "fragment_retries": 10,
        "continuedl": True,
        "overwrites": False,
    }

    with yt_dlp.YoutubeDL(options) as downloader:
        info = downloader.extract_info(url, download=True)

    print("\nDownload complete!")
    print(f"Title: {info.get('title', 'Unknown')}")
    print(f"Video ID: {info.get('id', 'Unknown')}")
    print(f"Output directory: {OUTPUT_DIR}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download the best available YouTube replay as an MKV file."
    )
    parser.add_argument(
        "url",
        nargs="?",
        help="YouTube video URL (prompts interactively if omitted)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        args = parse_args()
        url = (
            args.url.strip()
            if args.url
            else input("Paste YouTube replay URL: ").strip()
        )

        if not url:
            sys.exit("No URL provided.")

        download_stream(url)

    except KeyboardInterrupt:
        print("\nDownload interrupted.")
        sys.exit(130)
    except Exception as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        sys.exit(1)
