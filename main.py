import json
from datetime import timedelta
import pandas as pd

with open("Songs.json", 'r') as file:
    spotify_json = json.load(file)

# duration_time = spotify_json['tracks'][0]['duration_ms'] #280000

# total_sec = duration_time / 1000
# min = int(total_sec / 60)
# sec = int(total_sec % 60)
# print(f"The duration time is {min} minute and {sec} second")

def duration(ms):
    t  = timedelta(milliseconds= ms)
    min = int(t.seconds / 60)
    sec = int(t.seconds % 60)
    return f"{min}:{sec:02d}"
# print(duration(900000))

track_list = []

for i in spotify_json['tracks']:
    track = {
        'Playlist name' : spotify_json['playlist_name'],
        'Track name': i['track_name'],
        'Duration(min:sec)': duration(i['duration_ms'])
    }
    track_list.append(track)
df = pd.DataFrame(track_list)
df.to_csv('songs.csv', index = False)


