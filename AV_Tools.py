# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:14:00 2026

@author: 
"""
import os
import ffmpeg
from pathlib import Path

def extract_audio_to_mp3():
    input_path = input("Enter path to the video file: ").strip().strip('"')
    if not os.path.isfile(input_path):
        print("File not found.")
        return

    output_path = os.path.splitext(input_path)[0] + ".mp3"

    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, acodec="libmp3lame", audio_bitrate="192k", vn=None)
            .overwrite_output()
            .run(quiet=True)
        )
        print(f"Saved: {output_path}")
    except ffmpeg.Error as e:
        print("FFmpeg error:", e.stderr.decode() if e.stderr else e)

# --- Examples ---
# compress_mp3(bitrate="128k")
# compress_mp3(mono=True, sample_rate=22050)
def compress_mp3(bitrate="128k", mono=False, sample_rate=None):
    
    try:
        input_file = Path(input("Enter path to the video file: ").strip().strip('"'))
    except:
        print("Invalid File Name.")
        return
    
    if not input_file.is_file():
        print("File not found.")
        return
    
    output_file = input_file.with_name(input_file.stem + "_compressed.mp3")
    # out = ffmpeg.input(str(input_file))

    kwargs = {
        "acodec": "libmp3lame",
        "b:a": bitrate,
    }
    if mono:
        kwargs["ac"] = 1
    if sample_rate:
        kwargs["ar"] = sample_rate

    try:
        (
            ffmpeg.input(str(input_file))
            .output(str(output_file), **kwargs)
            .overwrite_output()
            .run(capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print(e.stderr.decode())  # bytes → str
    
    print(f"Done: {output_file} ({os.path.getsize(output_file) / 1024:.1f} KB)")
