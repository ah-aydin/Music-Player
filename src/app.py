from random import randint
import os

class App:
    window = None
    @classmethod
    def init(cls, window):
        cls.window = window
        # If the track_dirs.txt exists get all the track directories
        if os.path.exists("track_dirs.txt"):
            with open("track_dirs.txt", "r") as f:
                cls.track_dirs = f.readlines()
            # Get rid of the '\n' character that is red from the file
            for i in range(len(cls.track_dirs)):
                cls.track_dirs[i] = cls.track_dirs[i].rstrip("\n")
        else: # Otherwise create the track_dirs.txt file
            open("track_dirs.txt", "w").close()

    """
    Variables and functions to manipulate the track directories
    """
    track_dirs = []
    @classmethod
    def add_track_dir(cls, dir):
        cls.track_dirs.append(dir)
        # Clear the track_dirs.txt file
        open("track_dirs.txt", "w").close()
        # Than fill it
        with open("track_dirs.txt", "w") as f:
            for dir in cls.track_dirs:
                f.write(dir + "\n")
    
    @classmethod
    def remove_track_dir(cls, dir):
        cls.track_dirs.remove(dir)
        # Clear the track_dirs.txt file
        open("track_dirs.txt", "w").close()
        # Than fill it
        with open("track_dirs.txt", "w") as f:
            for dir in cls.track_dirs:
                f.write(dir + "\n")
    
    """
    Variables and functions to manipulate the playlist
    """

    shuffle = False
    playlist = []
    playlist_index = 0
    @classmethod
    def toggle_shuffle(cls):
        if cls.shuffle == False:
            if len(cls.playlist) != 0:
                cls.gen_random_playlist(cls.track_list.index(cls.playlist[cls.playlist_index]))
            cls.shuffle = True
        else:
            cls.shuffle = False
    @classmethod
    def add_tracks_to_playlist(cls, track_list):
        cls.playlist += track_list
    
    @classmethod
    def clear_playlist(cls):
        cls.playlist = []
    
    @classmethod
    def remove_tracks_from_playlist(cls, track_list):
        for track in track_list:
            try:
                cls.playlist.remove(track)
            except:
                print('Track is not in playlist')

    @classmethod
    def start_playlist_from_track(cls, track_to_start):
        cls.clear_playlist()
        cls.playlist_index = 0
        if cls.shuffle == True:
            cls.gen_random_playlist(track_to_start)
            return
        start = track_to_start
        counter = 0
        while counter < len(cls.track_list):
            cls.add_tracks_to_playlist([cls.track_list[start % len(cls.track_list)]])
            start += 1
            counter += 1
        cls.window.OnPlaylistChange()

    @classmethod
    def gen_random_playlist(cls, track_to_start):
        cls.clear_playlist()
        cls.playlist_index = 0
        tracks = cls.track_list.copy()
        cls.add_tracks_to_playlist([tracks[track_to_start]])
        tracks.remove(tracks[track_to_start])
        while len(tracks) > 0:
            random_track_index = randint(0, len(tracks) - 1)
            cls.add_tracks_to_playlist([tracks[random_track_index]])
            tracks.remove(tracks[random_track_index])
        cls.window.OnPlaylistChange()

    @classmethod
    def get_next_track(cls):
        cls.playlist_index += 1
        if cls.playlist_index >= len(cls.playlist):
            cls.playlist_index = 0
        return cls.playlist[cls.playlist_index]
    
    @classmethod
    def get_prev_track(cls):
        cls.playlist_index -= 1
        if cls.playlist_index < 0:
            cls.playlist_index = len(cls.playlist) - 1
        return cls.playlist[cls.playlist_index]
    
    @classmethod
    def get_current_track(cls):
        return cls.playlist[cls.playlist_index]

    @classmethod
    def get_playlist(cls):
        return cls.playlist.copy()

    @classmethod
    def change_current_playlist_track(cls, id):
        cls.playlist_index = id

    """
    Variables and functions to manipulate available tracks
    """
    track_list = []
    @classmethod
    def add_tracks_to_track_list(cls, track_list):
        cls.track_list += track_list
    
    @classmethod
    def clear_track_list(cls):
        cls.track_list.clear()

