import pickle
import os

class App:
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
            print(cls.track_dirs)
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
