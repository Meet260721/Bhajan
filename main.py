import json
from datetime import timedelta
import psycopg2
from psycopg2 import sql
import pandas as pd

# read file from Songs.json as file and store data in spotify_json
with open("Songs.json", 'r') as file:
    spotify_json = json.load(file)

 #Connection to database
connection = psycopg2.connect(
    dbname="Demo",
    user="postgres",
    password="Meet@2712",
    host="localhost",
    port="5432"
)
curr = connection.cursor()
# create function for convert duration time from millisecond to minutes
def duration_min(ms):
    t = timedelta(milliseconds= ms)
    min = int(t.seconds / 60)
    return min

# create function for convert duration time from millisecond to second
def duration_sec(ms):
    t  = timedelta(milliseconds= ms)
    sec = int(t.seconds % 60)
    return sec

curr.execute(sql.SQL("""
    INSERT INTO playlist (playlist_name, description, creator_username, creator_email)
    VALUES (%s, %s, %s, %s)"""),
    (
        spotify_json['playlist_name'],
        spotify_json['description'],
        spotify_json['creator']['username'],
        spotify_json['creator']['email']
    ))

for track in spotify_json['tracks']:
    curr.execute(sql.SQL("""
        INSERT INTO track (track_name, artist, album_name, release_date, duration_min, popularity, explicit_content, duration_sec)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""),
        (
            track['track_name'],
            track['artist'],
            track['album']['name'],
            track['album']['release_date'],
            duration_min(track['duration_ms']),
            track['popularity'],
            # track['genres'],
            track['explicit_content'],
            duration_sec(track['duration_ms'])
        ))

# Extract genre names from the JSON data
genre_names = []
for track in spotify_json['tracks']:
    genre_names.extend(track['genres'])

# Remove duplicate genre
genre_names = list(set(genre_names))

# Insert genre names into the genre table
for genre_name in genre_names:
    curr.execute(sql.SQL("""
        INSERT INTO genre (genre_name)
        VALUES (%s)"""), (genre_name,))


connection.commit()

# Close the cursor and connection
curr.close()
connection.close()

