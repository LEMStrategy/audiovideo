# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:58:29 2026

@author: molin
"""

from pathlib import Path
import ffmpeg
import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

max_workers = 4                   # Number of parallel conversions

def convert_flac_to_alac(flac_path: Path, m4a_path: Path, erase_original: bool) -> bool:
    """Convert FLAC to ALAC .m4a using ffmpeg-python"""
    if m4a_path.exists():
        print(f"✅ Skipped (already exists): {m4a_path.name}")
        return True

    print(f"Converting: {flac_path.name} → {m4a_path.name}")

    try:
        (
            ffmpeg
            .input(str(flac_path))
            .output(
                str(m4a_path),
                **{
                    'c:a': 'alac',
                    'c:v': 'copy',       # copy the cover art stream as-is
                    'map': '0',          # map all streams
                    'map_metadata': '0',
                    'loglevel': 'error'
                }
        )
    .overwrite_output()
    .run(quiet=True)
)
        print(f"✅ Success: {m4a_path.name}")
        if erase_original:
            print(f"✅ Erasing Original: {flac_path.name}")
            flac_path.unlink()
        return True

    except ffmpeg.Error as e:
        print(f"❌ Error converting {flac_path.name}")
        if e.stderr:
            print(e.stderr.decode())
        return False
    except Exception as e:
        print(f"❌ Unexpected error with {flac_path.name}: {e}")
        return False


def convert_directory_and_subdirs (source_dir: Path, erase_original: bool):
    #
    if not source_dir.exists():
        print(f"Error: Directory not found → {source_dir}")
        return
        
    # Do Subdirectories
    dir_list = [item for item in source_dir.iterdir() if item.is_dir()]
    for directory in dir_list:
        convert_directory_and_subdirs (directory, erase_original)

    # Find all FLAC files recursively
    flac_files = list(source_dir.rglob("*.flac"))
    print(f"Found {len(flac_files)} FLAC files on {source_dir} and SubDirectories.\n")

    if not flac_files:
        print("No FLAC files found on {source_dir}.")
        return

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {}

        for flac_path in flac_files:
            m4a_path = flac_path.with_suffix('.m4a')
            future = executor.submit(convert_flac_to_alac, flac_path, m4a_path, erase_original)
            future_to_file[future] = flac_path

        # Wait for completion
        for future in as_completed(future_to_file):
            future.result()

        print("\n🎉 Batch conversion for {} finished!".format(source_dir))
    return

def main():
    # ================== CONFIGURATION ==================
    
    print("Select TRANSFORM Localion:")
    print("1: Local")
    print("2: NAS")
    download_type = input("Enter choice (1 or 2): ").strip()
    
    #
    file_system = os.name
    if file_system == "posix" or file_system == "darwin" or file_system == "linux" :
        if download_type == '2':
            path_prefix = "/mnt/Media/Boris_iTunes/Music"
        elif download_type == '1':
            path_prefix = "~/Downloads"
    elif file_system == "nt" or file_system == "win32" or file_system == "win64" :
        if download_type == '2':
            path_prefix = "K:/Boris_iTunes/Music"
        elif download_type == '1':
            path_prefix = "C:/C_Temp/"
    source_dir = Path(path_prefix)   # 

    #
    response = input("Use DEFAULT AUDIO library {} (y/n): ".format(path_prefix))
    while response=='n' or response=='N'  :
        new_dir = input("    Enter NEW Video Directory ---> ")
        try:
            source_dir = Path(new_dir)
            break
        except:
            print("Error: Invalid Path ={}>".format(new_dir))
            print("  TRY AGAIN!")    
    
    response = input("ERASE ORIGINAL (Y/y) OR (N/n): ")
    if response=='y' or response=='Y'  :
        erase_original = True      # False = create "ALAC" folder
    elif response=='N' or response=='n'  :
        erase_original = False      # 
    else:
        print("Invalid Response ={}".format(response))

    convert_directory_and_subdirs (source_dir, erase_original)
    return


if __name__ == "__main__":
    main()