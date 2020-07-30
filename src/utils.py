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