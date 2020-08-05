import os

class App:
    """
    Variables and functions to manipulate the track directories
    """
    track_dirs = []
    @classmethod
    def init(cls):
        # If the track_dirs.txt exists get all the track directories
        if os.path.exists("track_dirs.txt"):
            with open("track_dirs.txt", "r") as f:
                cls.track_dirs = f.readlines()
            # Get rid of the '\n' character that is red from the file
            for i in range(len(cls.track_dirs)):
                cls.track_dirs[i] = cls.track_dirs[i].rstrip("\n")
        else: # Otherwise create the track_dirs.txt file
            open("track_dirs.txt", "w").close()
    
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
    playlist = []
    playlist_index = 0
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
        start = track_to_start
        counter = 0
        while counter < len(cls.track_list):
            cls.add_tracks_to_playlist([cls.track_list[start % len(cls.track_list)]])
            start += 1
            counter += 1

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

