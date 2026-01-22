#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:30:57 2025

@author: cygnus_x1
"""
from mutagen.mp4 import MP4
import os
import sys
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from pymediainfo import MediaInfo
import subprocess
import ffmpeg
from io import StringIO
import io
from pathvalidate import sanitize_filename, sanitize_filepath
from tmdbv3api import TMDb, TV, Season
import requests


# Initialize TMDb
tmdb = TMDb()
tmdb.api_key = "dd17a346556e803cc93810a544c008e8"  # Replace with your key
tmdb.language = "en"
tv = TV()
season = Season()

def clean_filename(filename):
    allowed_chars = ['-', '(', ')', "\'", '/', '\\', ' ', '.', '[', ']']
    name = str(filename)
    new_name = ''.join(char for char in name if char.isalnum() or char in allowed_chars)
    return new_name

def is_numeric(var):
    return isinstance(var, (int, float, complex))


def get_image_stream_index_type(m4v_file):
    image_list = []
    try:
        # Run ffprobe and get the output in JSON format
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'stream=index,codec_name', '-of', 'json', m4v_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
       # Parse the JSON output
        output = json.loads(result.stdout)
        #
        image_type = None
        # Iterate through streams to find PNG codec
        for stream in output['streams']:
            if 'codec_name' in stream.keys():
                if stream['codec_name'] == 'png':
                    image_type = '.png'
                    image_list.append((stream['index'], image_type ))
                elif stream['codec_name'] == 'mjpeg' :
                    image_type = '.mjpeg'
                    image_list.append((stream['index'], image_type ))
                elif stream['codec_name'] == 'jpeg':
                    image_type = '.jpeg'
                    image_list.append((stream['index'], image_type ))
                if stream['codec_name'] == 'bmp':
                    image_type = '.bmp'
                    image_list.append((stream['index'], image_type ))
                if stream['codec_name'] == 'gif':
                    image_type = '.gif'
                    image_list.append((stream['index'], image_type ))
                if stream['codec_name'] == 'tiff':
                    image_type = '.tif'
                    image_list.append((stream['index'], image_type ))
                if stream['codec_name'] == 'webp':
                    image_type = '.webp'
                    image_list.append((stream['index'], image_type ))
                elif stream['codec_name'] == 'heic':
                    image_type = '.heic'
                    image_list.append((stream['index'], image_type ))
                elif stream['codec_name'] == 'heif':
                    image_type = '.heif'
                    image_list.append((stream['index'], image_type ))
                else:
                    pass
        #
        return image_list  # Return None if no image stream is found
    #
    except subprocess.CalledProcessError as e:
        print("An error occurred in get_image_stream_index_type: {}".format(e.stderr.decode()))
        return image_list


def extract_artwork(m4v_file, title, overwrite_artwork=True,  nfo_type="movie"):
    # Get Image Stream and type
    image_count = {
        '.png'    : 0,
        '.mjpeg'  : 0,
        '.jpeg'   : 0,
        '.bmp'    : 0,
        '.gif'    : 0,
        '.tif'    : 0,
        '.webp'   : 0,
        '.heic'   : 0,
        '.heif'   : 0
        }
    #
    image_list = get_image_stream_index_type(m4v_file)
    file_lists = {key :[] for key in image_count.keys()}
    if title is None:
        title = m4v_file.stem
    for stream, image_type in image_list:
        output_file = m4v_file.with_stem(title+"-"+str(image_count[image_type])+"-poster").with_suffix(image_type)
        if output_file.exists() and overwrite_artwork==False:
            # print("The output file={} already exists and overwrite_artwork is={}.".format(output_file, overwrite_artwork))
            pass
        #
        else:
            try:
                # Use ffmpeg to extract the artwork
                (
                    ffmpeg
                    .input(m4v_file)
                    .output(str(output_file), map='0:{}'.format(stream), vframes=1)
                    .run(overwrite_output=overwrite_artwork, capture_stdout=True, capture_stderr=True, quiet=True)
                )
                # print("Artwork extracted and saved as {}".format(output_file))
                if image_type =='.mjpeg':
                    input_file = output_file
                    output_file =  output_file.with_suffix(".jpg")
                    frame_number = 0
                    try:
                        out, err = ffmpeg.input(str(input_file)) \
                            .filter('select', f'eq(n,{frame_number})') \
                            .output(str(output_file), vframes=1, qscale=1) \
                            .run(overwrite_output=overwrite_artwork, capture_stdout=True, capture_stderr=True, quiet=True)
                        if output_file.exists():
                            # print("    ...successfully extracted frame {} to {}".format(frame_number, output_file))
                            file_lists[image_type].append(output_file)
                            image_count[image_type] +=1
                        else:
                            print("extract_artwork: NO jpg extracted from mjpeg with ffmpeg:\n OUT={} \n ERROR={}".format(out.decode('utf8'), err.decode('utf8')))
                    except ffmpeg.Error as e:
                        print("extract_artwork: Error extracting jpg frame from mjpeg with ffmpeg: {}".format(e.stderr.decode('utf8')))
                    input_file.unlink()
                else:
                    file_lists[image_type].append(output_file)
                    image_count[image_type] +=1
            except ffmpeg.Error as e:
                error_message = e.stderr.decode()
                print("An error occurred in extract_artwork:")
                if " already exists. Overwrite? [y/N] Not overwriting - exiting" in error_message :
                    print("---> The output file={} already exists and overwrite_artwork is={}".format(output_file, overwrite_artwork))
                else:
                    print("----> {}".format(error_message))
    #########
    poster_list = []
    fanart_list = []
    #
    for file_type in image_count.keys():
        art_file_1 = None
        art_file_2 = None
        second     = None
        if image_count[file_type] > 0 :
            art_file_1 = file_lists[file_type][0]
            art_file_2 = file_lists[file_type][0]
            second     = file_lists[file_type][0]
            for i in range(image_count[file_type]):
                    if file_lists[file_type][i].stat().st_size > art_file_1.stat().st_size:
                        second     = art_file_1
                        art_file_1 = file_lists[file_type][i]
                    if file_lists[file_type][i].stat().st_size > second.stat().st_size and file_lists[file_type][i].stat().st_size < art_file_1.stat().st_size  :
                            art_file_2 = file_lists[file_type][i]
                            second = file_lists[file_type][i]
        if art_file_1 is not None:
            poster_list.append(art_file_1)
        if art_file_2 is not None:
            fanart_list.append(art_file_2)
    poster = None
    fanart = None
    for file in poster_list:
        if poster is None:
            poster = file
        else:
            if poster.stat().st_size < file.stat().st_size:
                poster = file
    for file in fanart_list:
        if fanart is None:
            fanart = file
        else:
            if fanart.stat().st_size < file.stat().st_size:
                fanart = file
    if poster is not None:
        if poster.exists():
            suff = poster.suffix
            if  nfo_type=="movie":
                new_file = m4v_file.with_stem(title+"-poster").with_suffix(suff)
                if new_file.exists():
                    new_file.unlink()
                poster = poster.rename(m4v_file.with_stem(title+"-poster").with_suffix(suff)).name
            elif nfo_type=="episodedetails":
                new_file = m4v_file.with_stem(title+"-thumb").with_suffix(suff)
                if new_file.exists():
                    new_file.unlink()
                poster = poster.rename(m4v_file.with_stem(title+"-thumb").with_suffix(suff)).name
        else:
            poster = None
    if fanart is not None:
        if fanart.exists():
            suff = fanart.suffix
            fanart = fanart.rename(m4v_file.with_stem(title+"-fanart").with_suffix(suff)).name
        else:
            fanart = None
    return poster, fanart

def replace_slash(text):
    if type(text) == str:
        return text.replace(' / ',', ')
    else:
        return text

def download_poster(poster_path, save_dir):
    """Download and save the poster image to the specified directory."""
    if not poster_path:
        print("No poster path provided.")
        return None
    # Construct full URL (w500 size for decent quality)
    base_url = "https://image.tmdb.org/t/p/w500"
    poster_url = f"{base_url}{poster_path}"
    image_ext = Path(poster_path).suffix
    poster_name = "poster"+image_ext
    poster_file = os.path.expanduser(save_dir / poster_name)

    # Download the image
    try:
        response = requests.get(poster_url, stream=True)
        response.raise_for_status()  # Check for HTTP errors
        with open(poster_file, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Saved poster to {poster_file}")
        return poster_file
    except requests.RequestException as e:
        print(f"Failed to download poster: {e}")
        return None


def fetch_tv_metadata(series_name, series_path, season_num=None, episode_num=None, show=None, details=None, save_poster=False):
    """Fetch TV show metadata from TMDb."""
    if not(show):
        search_results = tv.search(series_name)['results']
        if len(search_results) == 0:
            metadata = {
                "title": str(series_name),
                "plot": "This Show is about {}".format(series_name),
                "mpaa": "NR",
                "genre": "Sui Generis",
                "studio": "No Studio Data",
                "season": "0",
                "episode": "0",
                "no_data": True
            }
            print ("ERROR: no metadata in TMDB for {}.".format(series_name))
            return metadata, None, None
        #
        if len(search_results) == 1:
            show = search_results[0]  # Take the only match
        else:
            print("Multiple SHows found for the Series Name={}, Select the correct one:\n".format(series_name))
            for showindex in range(len(search_results)):
                show = search_results[showindex]
                print('SHOW #={} \nNAME={}\nOVERVIEW={}\n'.format(showindex, show.name, show.overview))
            response = input("ENTER THE CORRECT SHOW # FOR {}: : ".format(series_name))
            if int(response) in range(len(search_results)):
                    show = search_results[int(response)]
                    show_id = show["id"]
                    details = tv.details(show_id)
            else:
                metadata = {
                    "title": str(series_name),
                    "plot": "This Show is about {}".format(series_name),
                    "mpaa": "NR",
                    "genre": "Sui Generis",
                    "studio": "No Studio Data",
                    "season": "0",
                    "episode": "0",
                    "no_data": True
                }
                print ("ERROR: invalid Show Number Response for {}.".format(series_name))
                return metadata, None, None
        #
    if show.poster_path and save_poster:
        download_poster(show.poster_path, series_path)
    #
    show_id = show["id"]
    details = tv.details(show_id)
    #
    metadata = {
        "title": details["name"],
        "plot": details["overview"],
        "year": details["first_air_date"].split("-")[0] if details["first_air_date"] else None,
        "mpaa": details.get("content_ratings", {}).get("results", [{}])[0].get("rating"),
        "genre": [g["name"] for g in details["genres"]],
        "studio": details["networks"][0]["name"] if details["networks"] else None,
    }

    if season_num and episode_num:
        # Fetch episode data (example: Season 1, Episode 1)
        season_details = season.details(show_id, season_num=int(season_num) )  #, int(episode_num))
        details = season_details.episodes[int(episode_num)-1]
        metadata.update({
            "showtitle" : str(series_name),
            "title": details['name'],
            "season": str(details["season_number"]),
            "episode": str(details["episode_number"]),
            "plot": details["overview"],
        })
    return metadata, show, details

def extract_metadata(m4v_file, overwrite=True, nfo_type="movie", series_name=None):
    """Extract metadata from M4V file, supporting both movies and TV shows."""
    # Movie fields
    title = None
    genre = None
    plot = None
    year = None
    mpaa = None
    director = None
    producer = None
    studio = None
    screenplay = None
    runtime = None
    cast = []
    language = []
    subtitles = []
    country = None
    # TV-specific fields
    showtitle = None
    episode_title = None
    season = None
    episode = None
    aired = None
    poster = None
    fanart = None
    thumb = None
    no_data = False

    try:
        media_info = MediaInfo.parse(m4v_file)
    except Exception as e:
        print(f"-------> extract_metadata: ERROR parsing {m4v_file}: {e}")
        # Fallback title if parsing fails
        title = str(m4v_file.stem)
        metadata = _build_metadata(title, nfo_type, m4v_file, overwrite)
        return metadata, poster, fanart, thumb

    for track in media_info.tracks:
        if track.track_type == "General":
            # Common fields
            title = sanitize_filename(track.title) or str(m4v_file.stem)
            if isinstance(track.genre, str):
                genre = track.genre.split(', ')
            elif isinstance(track.genre, list):
                genre = track.genre
            else:
                genre = [str(track.genre)]
            plot = track.description or track.longdescription
            date = track.recorded_date or track.encoded_date
            if isinstance(date, str):
                year = date.split('-')[0]
            mpaa = track.contentrating or track.law_rating
            director = replace_slash(track.director)
            producer = replace_slash(track.producer)
            studio = track.production_studio or track.publisher
            screenplay = replace_slash(track.screenplay_by or track.written_by)
            duration_ms = track.duration
            if is_numeric(duration_ms):
                runtime = str(int(round(float(duration_ms) / 60000, 0)))
            actor = track.actor or track.performers
            if isinstance(actor, str):
                actor = actor.split(' / ')
            elif not actor:
                actor = []

            # TV-specific parsing
            if nfo_type == "episodedetails":
                showtitle = series_name  # Often series name   sanitize_filename(track.album)
                title = sanitize_filename(track.track_name) or track.title
                season = track.season
                episode = track.episode
                aired = track.recorded_date or track.encoded_date
                if not season and track.track:  #
                    season = track.track
                elif not season:
                    season = '1'
                if not episode and track.part:  # Fallback: 'Track' might be episode
                    episode = track.part

        elif track.track_type == "Audio":
            if track.language:
                language.append(track.language)
        elif track.track_type == "Text":
            if track.language:
                subtitles.append(track.language)

    # Fallback for missing title
    if not title:
        print(f"-------> extract_metadata: ERROR, {nfo_type}={m4v_file.stem} has NO TITLE, using filename.")
        title = str(m4v_file.stem)
        no_data = True
    if nfo_type == "episodedetails" and not showtitle:
        showtitle = title
        no_data = True

    # Extract artwork
    poster, fanart = extract_artwork(m4v_file, str(m4v_file.stem), overwrite_artwork=overwrite,  nfo_type=nfo_type)
    thumb = poster
    # Build metadata dictionary based on type
    metadata = _build_metadata(title, nfo_type, m4v_file, overwrite,
                               genre=genre, plot=plot, year=year, mpaa=mpaa,
                               director=director, producer=producer, studio=studio,
                               screenplay=screenplay, runtime=runtime, actor=actor,
                               country=country, language=language, subtitles=subtitles,
                               poster=poster, fanart=fanart,
                               showtitle=showtitle,
                               season=season,
                               episode=episode,
                               aired=aired,
                               thumb=thumb,
                               no_data=no_data
                               )
    # print(metadata)
    return metadata, poster, fanart, thumb

def _build_metadata(title, nfo_type, m4v_file, overwrite, **kwargs):
    """Helper to construct metadata dictionary based on nfo_type."""
    base_metadata = {
        'title': title,
        'genre': kwargs.get('genre'),
        'plot': kwargs.get('plot'),
        'year': kwargs.get('year'),
        'mpaa': kwargs.get('mpaa'),
        'director': kwargs.get('director'),
        'producer': kwargs.get('producer'),
        'studio': kwargs.get('studio'),
        'screenplay': kwargs.get('screenplay'),
        'runtime': kwargs.get('runtime'),
        'actor': kwargs.get('actor', []),
        'country': kwargs.get('country'),
        'language': kwargs.get('language', []),
        'subtitles': kwargs.get('subtitles', []),
        'poster': str(kwargs.get('poster', '')),
        'fanart': str(kwargs.get('fanart', '')),
        'no_data': kwargs.get('no_data')
    }
    if nfo_type == "episodedetails":
        base_metadata.update({
            'showtitle': kwargs.get('showtitle'),
            'season': kwargs.get('season'),
            'episode': kwargs.get('episode'),
            'aired': kwargs.get('aired')
        })
    return base_metadata



def create_nfo(metadata, output_file, overwrite=True, nfo_type='movie'):
    """Create an NFO file from the extracted metadata."""
    # rename in case movie filename  is not the same as the movie title in metadata
    # new_name =  output_file  # .with_stem(metadata['title'])
    if output_file.exists() and overwrite==False:
            # print("NFO file ={} already exists and overwrite={}".format(output_file, overwrite))
            return

    #
    root = ET.Element(nfo_type)
    #
    for key, value in metadata.items():
        if isinstance(value, list):
            if key == 'actor':
                for name in value:
                    actor = ET.SubElement(root, "actor")
                    ET.SubElement(actor, "name").text = name
                    ET.SubElement(actor, "role").text = ""
                    ET.SubElement(actor, "order").text = ""
                    ET.SubElement(actor, "thumb").text = ""
            elif key == 'genre':
                    for genre in value:
                        # print ('Found GENRE ={}'.format(genre))
                        ET.SubElement(root, key).text = str(genre)
            else:
                for item in value:
                    ET.SubElement(root, key).text = str(item)
            #
        elif key == 'producer':
            ET.SubElement(root, "credits").text = 'Producer: ' + str(value)
        elif key == 'screenplay':
            ET.SubElement(root, "credits").text = 'Screenplay: ' + str(value)
        else:
            ET.SubElement(root, key).text = str(value)
    #
    tree = ET.ElementTree(root)
    tree.write(str(output_file), encoding='utf-8', xml_declaration=True)
    print("SAVED NFO file ={}".format(output_file))
    return

def is_mp4(m4v_file):
    #
    m4v_file= Path(m4v_file)
    if m4v_file.suffix =='.mp4' or m4v_file.suffix =='.m4v':
        return True
    return False

def is_mkv(mkv_file):
    #
    mkv_file= Path(mkv_file)
    if mkv_file.suffix =='.mkv' or mkv_file.suffix =='.MKV':
        return True
    return False


def is_kodi_compliant(filename, season, episode):
    """Check if filename ends with SxxExx and matches given season/episode."""
    # Pattern: S followed by 2 digits, E followed by 2 digits, before extension
    pattern = r"S(\d{2})E(\d{2})(?=\.\w+$)"
    pattern_match = re.search(pattern, filename, re.IGNORECASE)

    if not pattern_match:
        return False  # No SxxExx pattern found

    # Extract season and episode from filename
    file_season, file_episode = pattern_match.groups()

    # Compare with passed metadata (padded to 2 digits)
    return file_season == str(season).zfill(2) and file_episode == str(episode).zfill(2)

def rename_for_kodi(m4v_file, season, episode):
    """Rename file to append SxxExx only if not already compliant."""
    m4v_path = Path(m4v_file)
    current_name = m4v_path.name  # e.g., "01 From Pole to Pole (1080p HD).m4v"

    if is_kodi_compliant(current_name, season, episode):
        print(f"{current_name} is already Kodi-compliant.")
        return m4v_path  # No rename needed

    # Append SxxExx before the extension
    new_name = f"{m4v_path.stem} S{season.zfill(2)}E{episode.zfill(2)}{m4v_path.suffix}"
    new_path = m4v_path.parent / new_name
    m4v_path.rename(new_path)
    print(f"Renamed {current_name} to {new_name}")
    return new_path

def get_nfo (m4v_file, overwrite=True, nfo_type='movie', series_name=None, show=None):
    #
    m4v_file = Path(m4v_file)
    #
    # Clean FileName
    new_name = m4v_file.with_stem(clean_filename(sanitize_filename(m4v_file.stem)))
    if new_name != m4v_file:
        print("\n---------->  RENAMED MOVIE file from={} to={}".format(m4v_file, new_name))
        m4v_file = m4v_file.rename(new_name)
        #
    print("\n---------->  CREATING NFO file for={}".format(m4v_file))
    if not Path.exists(m4v_file):
        error_msg = "File {} does not exist.".format(m4v_file)
        print(error_msg)
        return(error_msg)
    # Extract metadata
    metadata, poster, fanart, thumb = extract_metadata(m4v_file, overwrite=overwrite, nfo_type=nfo_type, series_name=series_name)
    if metadata['no_data'] == True:
        if nfo_type== "episodedetails":
            season_num, episode_num = extract_season_episode(m4v_file)
            metadata, show, details = fetch_tv_metadata(series_name, series_path=m4v_file.parent, season_num=season_num, episode_num=episode_num, show=show, details=None, save_poster=True)
        elif nfo_type =='movie':
            pass
        else:
            pass
    #
    # Create NFO file name
    if nfo_type == "episodedetails":
        season  = metadata['season'] or "0"
        episode = metadata['episode'] or "0"
        if not is_kodi_compliant(str(m4v_file), season, episode):
            m4v_file= rename_for_kodi(m4v_file, season, episode)
    #
    nfo_file = m4v_file.with_suffix('.nfo')
    if nfo_file.exists() and overwrite==False:
            # print("NFO file ={} already exists and overwrite={}".format(nfo_file, overwrite))
            return
   # Create NFO file
    create_nfo(metadata, nfo_file, overwrite=overwrite, nfo_type=nfo_type)
    return


def extract_season_episode(file_path: Path) -> tuple[int, int] | None:
    """
    Extract season and episode numbers from a file name with format sNNeNN (case-insensitive).

    Args:
        file_path: Path object representing the file

    Returns:
        Tuple of (season_num, episode_num) or None if no match found
    """
    pattern = r'[sS](\d{1,2})[eE](\d{1,2})'
    match = re.search(pattern, file_path.stem)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None

def do_nfos(directory, do_subdirectories=False, replace_nfos=False, nfo_type="movie", series_name=None, show=None, details=None):
    #
    if do_subdirectories:
        directory_list = [item for item in directory.iterdir() if item.is_dir()]
        for subdir in directory_list:
            do_nfos(directory = subdir, do_subdirectories=do_subdirectories, replace_nfos=replace_nfos, nfo_type=nfo_type, series_name=series_name, show=show, details=details)
    #
    mp4_video_files = []
    mkv_video_files = []
    #
    if directory.exists() and directory.is_dir():
        # If empty, delete
        if not any(directory.iterdir()):
            print("Directory={} is empty, erasing.".format(directory))
            directory.rmdir()
        else:  # Extract videos
            mp4_video_files = [item for item in directory.iterdir() if is_mp4(item)]
            mkv_video_files = [item for item in directory.iterdir() if is_mkv(item)]
    else:
        print("Directory={} is invalid.".format(directory))
    #
    for video in mp4_video_files:
        get_nfo( m4v_file=video, overwrite=replace_nfos, nfo_type=nfo_type, series_name=series_name, show=show)
    # show = None
    # details = None
    for video in mkv_video_files:
        if nfo_type == 'episodedetails':
            season_num, episode_num = extract_season_episode(video)
            if season_num and episode_num:
                metadata, show, details = fetch_tv_metadata(series_name=series_name, series_path=directory, season_num=season_num, episode_num=episode_num, show=show, details=details)
                nfo_file = video.with_suffix('.nfo')
                if nfo_file.exists() and replace_nfos==False:
                    # print("NFO file ={} already exists and overwrite={}".format(nfo_file, overwrite))
                    return
                # Create NFO file
                create_nfo(metadata, nfo_file, overwrite=replace_nfos, nfo_type=nfo_type)
            else:
                print("Invalid Season/Episode data={}/{} for show={} in filename={}".format(season_num, episode_num, series_name, video))
        else:
            print("Invalid nfo_type={} for for MKV filename={}".format(nfo_type, video))
    return

def find_directories_without_nfo_art(directory_list):
    subdir_count = 0
    empty_list = []
    print("There are ={} SUBDIRECTORIES".format(len(directory_list)))
    for subdir in directory_list:
        if subdir.exists() and subdir.is_dir():
            subdir_count += 1
            file_count =0
            file_count = sum(1 for entry in subdir.iterdir() if entry.is_file())
            if file_count < 2:
                empty_list.append(subdir)
                print('----> VACIO = {}'.format(subdir))
    print("FOUND  ={} SUBDIRECTORIES".format(subdir_count))
    return empty_list


def do_series_nfos(dir_list, replace_nfos=True):
    for showdir in dir_list:
        show = None
        details = None
        series_name = showdir.name
        file_name = 'tvshow.nfo' #  showdir.name+".nfo"
        output_file = showdir / file_name
        if output_file.exists() and replace_nfos==False:
            pass
        else:
            metadata, show, details = fetch_tv_metadata(series_name, showdir, save_poster=True)
            create_nfo(metadata, output_file, overwrite=replace_nfos, nfo_type='tvshow')
        nfo_type = 'episodedetails'
        do_nfos(directory=showdir, do_subdirectories=True, replace_nfos=replace_nfos, nfo_type=nfo_type, series_name=series_name, show=show, details=details)
    return



if __name__ == "__main__":
    #
    print("Select Download Localion:")
    print("1: Local")
    print("2: NAS")
    download_type = input("Enter choice (1 or 2): ").strip()
    #
    process = ''
    response = input("DO YOU WANT TO CREATE NFOS FOR MOVIES (M/n) OR TV Shows (S/s): ")
    if response=='M' or response=='m'  :
        process = "movie"
    elif response=='S' or response=='s'  :
        process = "tvshow"
    else:
        print("Invalid Response ={}".format(response))

    #
    file_system = os.name
    if file_system == "posix" or file_system == "darwin" or file_system == "linux" :
        if download_type == '2':
            path_prefix = "/mnt/Media/Boris_iTunes"
        elif download_type == '1':
            path_prefix = "~/Downloads"
    elif file_system == "nt" or file_system == "win32" or file_system == "win64" :
        if download_type == '2':
            path_prefix = "K:/Boris_iTunes"
        elif download_type == '1':
            path_prefix = "C:/C_Temp/"

    else:
        print("Error: Unknown OS name ={}>".format(file_system))
        sys.exit(1)
    #
    if process == 'movie':
        video_library_directory = Path(path_prefix + '/Movies/')
    elif process == 'tvshow':
        video_library_directory = Path(path_prefix + '/TV Shows/')
    #
    response = input("Use DEFAULT video_library (y/n): ")
    while response=='n' or response=='N'  :
        new_dir = input("    Enter NEW Video Directory ---> ")
        try:
            video_library_directory = Path(new_dir)
            break
        except:
            print("Error: Invalid Path ={}>".format(new_dir))
            print("  TRY AGAIN!")
    #

    print("Creating NFOs for video_library={}".format(video_library_directory))
    #
    replace_nfos = False
    response = input("Replace existing NFOs and Artwork (y/n): ")
    if response=='y' or response=='Y'  :
        replace_nfos = True
    #
    if process == 'movie':
        if video_library_directory == Path(path_prefix + '/Boris_iTunes/Movies/'):
            do_subdirectories = True
        else:
            do_subdirectories = False
        do_nfos(directory=video_library_directory, do_subdirectories=do_subdirectories, replace_nfos=replace_nfos, nfo_type=process)

    elif process == 'tvshow':
        do_subdirectories = True
        if video_library_directory == Path(path_prefix + '/Boris_iTunes/TV Shows/'):
            dir_list = [item for item in video_library_directory.iterdir() if item.is_dir()]
            do_series_nfos(dir_list, replace_nfos=replace_nfos)
        else:
            do_series_nfos([video_library_directory], replace_nfos=replace_nfos)
