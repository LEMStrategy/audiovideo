# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:51:30 2026

@author: molin
"""

from PIL import Image, ImageDraw, ImageFont
import sys
import os
from pathlib import Path
from pathvalidate import sanitize_filename, sanitize_filepath

def create_scrolling_gif(
    input_path: str,
    output_path: str,
    viewport_width: int = 800,
    scroll_speed: float = 2.0,      # pixels per frame
    fps: int = 30,
    padding: int = 50,              # extra space on sides (for seamless feel)
    background_color: tuple = (0, 0, 0),
    loop: bool = True
):
    """
    Create a GIF where the input image scrolls horizontally.
    
    Args:
        input_path: Path to input image (PNG, JPG, etc.)
        output_path: Path for output GIF
        viewport_width: Width of the visible area in the GIF
        scroll_speed: Pixels to move per frame (higher = faster)
        fps: Frames per second (controls smoothness and playback speed)
        padding: Extra pixels added on left/right for better looping
        background_color: Background color if image doesn't fill height
        loop: Whether GIF should loop infinitely
    """
    
    # Load image
    img = Image.open(input_path).convert("RGB")
    orig_width, height = img.size
    
    # Create a wider canvas for seamless scrolling if desired
    canvas_width = orig_width + 2 * padding
    canvas = Image.new("RGB", (canvas_width, height), background_color)
    canvas.paste(img, (padding, 0))
    
    # Calculate number of frames needed to scroll the full content
    total_distance = orig_width + viewport_width  # full sweep + viewport
    num_frames = int(total_distance / scroll_speed) + 1
    
    frames = []
    duration_per_frame = int(1000 / fps)  # milliseconds
    
    print(f"Creating {num_frames} frames at {fps} FPS...")
    
    for i in range(num_frames):
        # Calculate current offset
        offset = int(i * scroll_speed) - padding
        
        # Create frame
        frame = Image.new("RGB", (viewport_width, height), background_color)
        
        # Paste the relevant portion
        paste_x = -offset
        frame.paste(canvas, (paste_x, 0))
        
        frames.append(frame)
    
    # Save as GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_per_frame,
        loop=0 if loop else 1,
        optimize=True
    )
    
    print(f"GIF saved to: {output_path}")
    print(f"Total duration: {num_frames * duration_per_frame / 1000:.1f} seconds")


# Example usage
if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python scroll_gif.py <input_image> <output_gif> [viewport_width] [speed]")
    #     print("\nExample:")
    #     print("python scroll_gif.py banner.png output.gif 800 1.5")
    #     sys.exit(1)
    
    # input_img = sys.argv[1]
    # output_gif = sys.argv[2]
    
    print("Select Conversion Localion:")
    print("1: Local")
    print("2: NAS")
    download_type = input("Enter choice (1 or 2): ").strip()
    #
    file_system = os.name
    if file_system == "posix" or file_system == "darwin" or file_system == "linux" :
        if download_type == '2':
            path_prefix = "/mnt/Media/Digital/GIFs"
        elif download_type == '1':
            path_prefix = "~/Downloads"
    elif file_system == "nt" or file_system == "win32" or file_system == "win64" :
        if download_type == '2':
            path_prefix = "K:/Digital/GIFs"
        elif download_type == '1':
            path_prefix = "C:/C_Temp/Media/GIFs"

    else:
        print("Error: Unknown OS name ={}>".format(file_system))
        sys.exit(1)
    #
    input_img = Path(input("Enter Image File Name: ").strip())
    output_gif = path_prefix / input_img.with_suffix('.gif')
    #
    
    viewport_w = int(sys.argv[3]) if len(sys.argv) > 3 else 800
    speed = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
    
    create_scrolling_gif(
        input_path=input_img,
        output_path=output_gif,
        viewport_width=viewport_w,
        scroll_speed=speed,
        fps=30,
        padding=100
    )