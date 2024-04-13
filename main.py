import json
from datetime import timedelta
import pandas as pd

# read file from Songs.json as file and store data in spotify_json
with open("Songs.json", 'r') as file:
    spotify_json = json.load(file)

# create function for convert duration time from millisecond to minutes
def duration_min(ms):
    t  = timedelta(milliseconds= ms)
    min = int(t.seconds / 60)
    return min

# create function for convert duration time from millisecond to second
def duration_sec(ms):
    t  = timedelta(milliseconds= ms)
    sec = int(t.seconds % 60)
    return sec

#create empty list to store data
track_list = []

#run for loop for read data from spotify_json['tracks'] and append in track_list = [] list
for i in spotify_json['tracks']:
    track = {
        'Playlist Name' : spotify_json['playlist_name'],
        'Description' :spotify_json['description'],
        'User Name':spotify_json['creator']['username'] ,
        "Email":spotify_json['creator']['email'],
        'Track Name': i['track_name'],
        "Artist": i['artist'],
        "Album": i['album'],
        "Album Name": i['album']['name'],
        "Release Date": i['album']['release_date'],
        'Duration(min)': duration_min(i['duration_ms']),
        'Duration(sec)': duration_sec(i['duration_ms']),
        "Popularity": i['popularity'],
        "Genres": i['genres'],
        "Explicit Content": i['explicit_content']
    }
    track_list.append(track)




