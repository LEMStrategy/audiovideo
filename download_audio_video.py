# -*- coding: utf-8 -*-
"""
Spyder   Editor
"""

import yt_dlp
from pathlib import Path
import re
import sys
import os

# Configuration
#
# Query Local/NAS Save
print("Select Download Localion:")
print("1: Local")
print("2: NAS")
download_type = input("Enter choice (1 or 2): ").strip()
#
file_system = os.name
if file_system == "posix" or file_system == "darwin" or file_system == "linux" :
    path_break = '/'
    if download_type == '1':
        SAVE_PATH = Path('~/Downloads/Audio/Youtube_Downloads/') # Output directory)
    else:
        SAVE_PATH = Path('/mnt/Media/Digital/Audio/Youtube_Downloads/') # Output directory)
elif file_system == "nt" or file_system == "win32" or file_system == "win64" :
    path_break = '\\'
    if download_type == '1':
        SAVE_PATH = Path('C:/C_Temp/Media/Youtube_Downloads/') # Output directory)
    else:
        SAVE_PATH = Path('K:/Digital/Audio/Youtube_Downloads/') # Output directory)
else:
    print("Error: Unknown OS/Download Typ Combo ={} and {}>".format(file_system, download_type))
    sys.exit(1)
#
VERBOSE = True  # Set to True for detailed logging

def sanitize_path_element(name: str) -> str:
    """
    Sanitize a string to be a valid path element (filename or directory) for Windows and Linux.

    Args:
        name: The input string to sanitize.

    Returns:
        A sanitized string safe for use as a path element.
    """
    # Replace invalid characters with an underscore
    # Windows: < > : " / \ | ? *
    # Linux: /
    invalid_chars = r'[<,>:"/\\|?*\x00-\x1F]'
    sanitized = re.sub(invalid_chars, '', name)

    # Remove leading/trailing spaces and periods (Windows restriction)
    sanitized = sanitized.strip().strip('.')

    # Handle reserved Windows names (e.g., CON, PRN, AUX, NUL, COM1, LPT1)
    reserved_names = {
        'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
        'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4',
        'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'
    }
    if sanitized.upper() in reserved_names:
        sanitized = f"_{sanitized}"

    # Ensure the name is not empty
    if not sanitized:
        sanitized = "unnamed"

    return sanitized

def get_playlist_info(playlist_url):
    """Fetch playlist metadata to get total video count."""
    ydl_opts = {
        'extract_flat': True,  # Get metadata without downloading
        'noplaylist': False,
        'ignoreerrors': True,
        'restrictfilenames': True,  # Avoid special characters
        'verbose': VERBOSE,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(playlist_url, download=False)
            return info.get('title'), info.get('entries', []), len(info.get('entries', []))
        except Exception as e:
            print(f"Error fetching playlist info: {e}")
            return [], 0

def download_single_video(video_url, output_type, save_path):
    """Download a single YouTube video as video (MP4) or audio (MP3)."""
    ydl_opts = {
        'outtmpl': f'{save_path}{path_break}%(title)s.%(ext)s',
        'noplaylist': True,
        'ignoreerrors': True,
        'verbose': VERBOSE,
    }

    if output_type == 'video':
        ydl_opts.update({
            'format': 'bestvideo[vcodec^=hev1]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Prioritizes H.264 (avc1) video + AAC audio in MP4
            'merge_output_format': 'mp4',
        })
    else:  # audio
        ydl_opts.update({
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Downloaded: {video_url} to {save_path}")
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

def download_playlist(playlist_url, output_type, save_path, start_index=1):
    """Download a YouTube playlist as video (MP4) or audio (MP3)."""
    print(f"DEBUG: Running updated download_playlist function (2025-05-16)")

    # Get playlist info
    title, entries, total_videos = get_playlist_info(playlist_url)
    if total_videos == 0:
        print("No videos found in playlist or playlist is invalid.")
        return

    # Adjust start_index if too high
    if start_index > total_videos:
        print(f"Start index {start_index} is greater than playlist size ({total_videos}). Setting to 1.")
        start_index = 1
    save_path = save_path / sanitize_path_element(title)
    ydl_opts = {
        'outtmpl': f'{save_path}{path_break}%(playlist_index)02d - %(title)s.%(ext)s',
        'noplaylist': False,
        'playlist_items': f"{start_index}-",
        'ignoreerrors': True,
        'verbose': VERBOSE,
    }

    if output_type == 'video':
        ydl_opts.update({
            'format': 'bestvideo[vcodec^=hev1]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Prioritizes H.264 (avc1) video + AAC audio in MP4
            'merge_output_format': 'mp4',
        })
    else:  # audio
        ydl_opts.update({
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
            print(f"Downloaded playlist: {playlist_url} (from index {start_index})")
        except Exception as e:
            print(f"Error downloading playlist {playlist_url}: {e}")

def main():
    """Main function to handle user input and initiate downloads."""
    print("DEBUG: Running updated script version (2025-05-16)")

    # Query source type
    print("Select YouTube source type:")
    print("1: Single Video")
    print("2: Playlist")
    download_source = input("Enter choice (1 or 2): ").strip()

    if download_source not in ['1', '2']:
        print(f"Invalid source type: {download_source}. Please choose 1 or 2.")
        return

    # Query output type
    print("\nSelect output type:")
    print("1: Video (MP4)")
    print("2: Audio (MP3)")
    output_type = input("Enter choice (1 or 2): ").strip()

    if output_type not in ['1', '2']:
        print(f"Invalid output type: {output_type}. Please choose 1 or 2.")
        return

    output_type = 'video' if output_type == '1' else 'audio'

    # Get URL and download
    if download_source == '1':
        url = input("\nEnter the YouTube VIDEO URL: ").strip()
        download_single_video(url, output_type, SAVE_PATH)
    else:  # download_source == '2'
        url = input("\nEnter the YouTube PLAYLIST URL: ").strip()
        start_index = input("Enter start index (default 1): ").strip()
        start_index = int(start_index) if start_index.isdigit() else 1
        download_playlist(url, output_type, SAVE_PATH, start_index)

if __name__ == '__main__':
    main()
