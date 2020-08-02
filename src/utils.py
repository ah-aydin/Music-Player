from app import App
import os

def convert_miliseconds(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds - minutes * 60
    minutes = str(minutes)
    seconds = str(seconds)
    if len(minutes) == 1:
        minutes = "0" + minutes
    if len(seconds) == 1:
        seconds = "0" + seconds
    
    return minutes + ":" + seconds

def get_tracks_from_directory(dir):
    if not os.path.exists(dir):
        App.remove_track_dir(dir)
        print("This directory does not exist.")
        return []
    track_list = []
    # Walk through the directory
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for filename in filenames:
            t_name, ext = os.path.splitext(filename)
            # If the file is not a track continue on to the next iteration of the loop
            if ext not in [".wav", ".mp3"]:
                continue
            data = {'dirpath': os.path.join(dirpath, filename), 'filename': t_name}
            track_list.append(data)
    # Sort the tracks in alphabetical order according to their filename
    track_list = sorted(track_list, key=lambda x: x['filename'])
    return track_list

def get_tracks_from_multiple_directories(dirs):
    track_list = []
    for dir in dirs:
        track_list += get_tracks_from_directory(dir)
    track_list = sorted(track_list, key=lambda x: x['filename'])
    return track_list