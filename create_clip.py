#!/usr/bin/env python3
"""Create frame-accurate MP4 clips from an MKV video using FFmpeg."""

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


CLIPS_DIR = Path(__file__).resolve().parent / "clips"


def create_clip(
    input_file: Path, start: str, end: str, output_name: str | None = None
) -> Path:
    """Extract a clip from input_file between start and end timestamps."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError(
            "FFmpeg not found. Please install FFmpeg "
            "and ensure it is in your PATH."
        )

    if not input_file.is_file():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    CLIPS_DIR.mkdir(exist_ok=True)

    if output_name:
        output_path = CLIPS_DIR / output_name
    else:
        safe_start = start.replace(":", "-")
        safe_end = end.replace(":", "-")
        output_path = CLIPS_DIR / f"{input_file.stem}_{safe_start}_to_{safe_end}.mp4"

    command = [
        "ffmpeg",
        "-i",
        str(input_file),
        "-ss",
        start,
        "-to",
        end,
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        str(output_path),
    ]

    subprocess.run(command, check=True)
    return output_path


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Clip a segment from an MKV video into an MP4 file."
    )
    parser.add_argument("input", type=Path, help="Path to source MKV file")
    parser.add_argument("start", help="Start timestamp (e.g. 00:01:30)")
    parser.add_argument("end", help="End timestamp (e.g. 00:02:15)")
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output filename inside clips/ (default: auto-named)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        args = parse_args()
        saved_path = create_clip(args.input, args.start, args.end, args.output)
        print(f"\nClip saved to: {saved_path}")

    except KeyboardInterrupt:
        print("\nClipping interrupted.")
        sys.exit(130)
    except subprocess.CalledProcessError as exc:
        print(f"\nFFmpeg failed with exit code {exc.returncode}.", file=sys.stderr)
        sys.exit(exc.returncode)
    except Exception as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        sys.exit(1)
