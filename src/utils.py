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
    track_list = []
    # Walk through the directory
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for filename in filenames:
            t_name, ext = os.path.splitext(filename)
            # If the file is not a track continue on to the next iteration of the loop
            if ext not in [".wav", ".mp3"]:
                continue
            data = {'dirpath': os.path.join(dirpath, filename), 'filename': filename}
            track_list.append(data)
    track_list = sorted(track_list, key=lambda x: x['filename'])
    return track_list