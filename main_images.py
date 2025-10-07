# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from pathlib import Path
from PIL import Image, ExifTags, ImageFile
from pillow_heif import register_heif_opener
from datetime import datetime
import piexif
import re
import shutil
import time

Image.MAX_IMAGE_PIXELS = 2300000000
register_heif_opener()

def convert_heic(filename, target_format='jpeg', delete_original=True):
    # Convert files to jpg while keeping the timestamp
    image = Image.open(filename)
    image_exif = image.getexif()
    if image_exif:
            # Make a map with tag names and grab the datetime
            exif = { ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS and type(v) is not bytes }
            try:
                date = datetime.strptime(exif['DateTime'], '%Y:%m:%d %H:%M:%S')
            except:
                date = datetime.now()
            #
            # Load exif data via piexif
            exif_dict = piexif.load(image.info["exif"])
            #
            # Update exif data with orientation and datetime
            exif_dict["0th"][piexif.ImageIFD.DateTime] = date.strftime("%Y:%m:%d %H:%M:%S")
            exif_dict["0th"][piexif.ImageIFD.Orientation] = 1
            exif_bytes = piexif.dump(exif_dict)
            #
            # Save image as jpeg
            if target_format=='jpeg':
                new_file = filename.with_suffix(".jpg")
                image.save(new_file, "jpeg", exif= exif_bytes)
                if new_file.is_file():
                    print("HEIC image converted {}".format(new_file))
                    if delete_original:
                        filename.unlink()
                        print("     Original HEIC image deleted {}".format(filename))
                    return True
                else:
                    print("Format not JPEG {}".format(target_format))
                    return False
            else:
                print("Format not JPEG {}".format(filename))
                return False
            #
    else:
        print("Unable to get exif data for {}".format(filename))
        return False
    return False


def process_heic_in_directory(dir_of_interest, target_format='jpeg'):
    count = 0
    dir_of_interest = Path(dir_of_interest)
    if dir_of_interest.is_dir():
        sub_dirs = [x for x in dir_of_interest.iterdir() if x.is_dir()]
        #
        filenames  = [x for x in dir_of_interest.iterdir() if x.is_file()]
        HEIC_files = [x for x in filenames if x.suffix =='.heic' or x.suffix =='.HEIC']
        #
        for filename in HEIC_files:
            if convert_heic(filename, target_format=target_format):
                count += 1
        #
        for directory in sub_dirs:
            count += process_heic_in_directory(directory, target_format=target_format)
    print("process_heic_in_directory: Converted {} HEIC file to format {}".format (count, target_format))
    return count

def is_damaged(image_file):
    #
    ImageFile.LOAD_TRUNCATED_IMAGES = False
    try:
        image = Image.open(image_file)
    except:
        return 1  # File is corrupted
    #
    try:
        image.verify()
    except:
        return 2  # File fails basic test
    #
    try:
        image = Image.open(image_file)
        im_pixels = image.load() 
    except:
        # Image may be truncated 
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        image = Image.open(image_file)
        try: _ = image.load() 
        except:
            print("   is_damaged: CAN NOT FIX Truncated file={}".format(image_file))
            return 3 # Image corrupted
        # Loaded Truncated image, rotate, save to try to FIX the PRoblem
        image = image.rotate(360)
        image.save(image_file)
        image.close()
        time.sleep(5)
        print("   is_damaged: Fixed Truncated file={}".format(image_file))
        # 
        return 4   # Truncated... 
    #
    return False
         
def find_files(dir_of_interest, target_format=['.jpg', '.jpeg', '.png'], check_subdirs=True):
    target_format = set([x.upper() for x in target_format] + [x.lower() for x in target_format]) 
    target_files = []
    if dir_of_interest.is_dir():
        sub_dirs = [x for x in dir_of_interest.iterdir() if x.is_dir()]
        #
        filenames  = [x for x in dir_of_interest.iterdir() if x.is_file()]
        target_files = [x for x in filenames if x.suffix in target_format]
        if check_subdirs:
            for directory in sub_dirs:
                new_files = find_files(dir_of_interest=directory , target_format=target_format, check_subdirs=check_subdirs)
                for file in new_files:
                    target_files.append(file)
        return target_files
    else:
        return target_files
    

def find_damaged_in_directory(dir_of_interest, damaged_dir, target_format=['.jpg', '.jpeg', '.png'], copy_damaged=True,  copy_repaired=True, del_damaged=True):
    dir_of_interest = Path(dir_of_interest)
    damaged_files  = []
    repaired_files = []
    copied_files   = []
    del_files      = []
    
    target_format = set([x.upper() for x in target_format] + [x.lower() for x in target_format])  #
    print ('Finding Damaged Pics in Dir={}'.format(dir_of_interest))
    if dir_of_interest.is_dir():
        sub_dirs = [x for x in dir_of_interest.iterdir() if x.is_dir()]
        #
        filenames  = [x for x in dir_of_interest.iterdir() if x.is_file()]
        target_files = [x for x in filenames if x.suffix in target_format]
        #
        for filename in target_files:
            is_bad = is_damaged(filename)
            #
            if is_bad:    
                damaged_files.append(filename)
                #
                if is_bad == 4 and copy_repaired:
                    file_copy = shutil.copy(src=filename, dst=damaged_dir)
                    repaired_files.append(file_copy)
                    copied_files.append(file_copy)
                #    
                elif copy_damaged:
                    file_copy = shutil.copy(src=filename, dst=damaged_dir)
                    copied_files.append(file_copy)
                #
                if del_damaged:
                    del_files.append(filename)
                    filename.unlink()
        print ('   {}===> Repaired/Damaged #={}/{},  Copied #={}, Deleted #={}'.format(dir_of_interest, len(repaired_files), len(damaged_files), len(copied_files), len(del_files)))
        #
        for directory in sub_dirs:
            find_damaged_in_directory(directory, damaged_dir, target_format=target_format, copy_damaged=copy_damaged, copy_repaired=copy_repaired, del_damaged=del_damaged)
    
    print(' ')
    return
                
def move_files(dir_of_interest, target_dir, target_format=['.mov', '.mp4'], check_subdirs=True):
    #
    target_files = find_files(dir_of_interest=dir_of_interest, target_format=target_format, check_subdirs=check_subdirs)
    for file in target_files:
        new_name = target_dir / file.name
        file.rename(new_name)
    return
    
        
    