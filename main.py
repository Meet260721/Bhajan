import json
from datetime import timedelta
import psycopg2
from psycopg2 import sql


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
def duration_time(ms):
    t = timedelta(milliseconds= ms)
    min = int(t.seconds / 60)
    sec = int(t.seconds % 60)
    return f"{min}.{sec:02d}"


# create function for convert duration time from millisecond to second
# def duration_sec(ms):
#     t  = timedelta(milliseconds= ms)
#     sec = int(t.seconds % 60)
#     return sec

genre_names = []
#Insert values from the  json data to  playlist table  in database
for playlist_data in spotify_json:
    curr.execute(sql.SQL("""
        INSERT INTO playlist (playlist_name, description, creator_username, creator_email)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (playlist_name, creator_username) DO NOTHING
        """),
        (
            playlist_data['playlist_name'],
            playlist_data['description'],
            playlist_data['creator']['username'],
            playlist_data['creator']['email']
        ))

    #Insert values from the  json data to  track table  in database
    for track in playlist_data['tracks']:
        genres_str = ','.join(track['genres'])
        curr.execute(
            sql.SQL("SELECT playlist_id FROM playlist WHERE playlist_name = %s AND creator_username = %s"),
            (playlist_data['playlist_name'], playlist_data['creator']['username'])
        )
        result = curr.fetchone()

        playlist_id = result[0] if result else None

        if playlist_id is not None:
            curr.execute(sql.SQL("""
                INSERT INTO track (track_name,playlist_id, artist, album_name, release_date, duration_time, popularity, genres, explicit_content)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (track_name, artist) DO NOTHING
                
                """),
                (
                    track['track_name'],
                    playlist_id,
                    track['artist'],
                    track['album']['name'],
                    track['album']['release_date'],
                    duration_time(track['duration_ms']),
                    track['popularity'],
                    genres_str,
                    track['explicit_content']
                ))
            curr.execute(sql.SQL("""
                        SELECT track_id FROM track 
                        WHERE track_name = %s AND artist = %s
                    """), (
                track['track_name'],
                track['artist']
            ))
            track_id = curr.fetchone()[0]

    # Extract genre names from the JSON data

    for track in playlist_data['tracks']:
        genre_names.extend(track['genres'])

    # Remove duplicate genre
    genre_names = list(set(genre_names))

    # Insert genre names into the genre table
    for genre_name in genre_names:
        curr.execute(sql.SQL("""
            INSERT INTO genre (genre_name)
            VALUES (%s)
            ON CONFLICT (genre_name) DO NOTHING
             """), (genre_name,))

        curr.execute(sql.SQL("""
                        INSERT INTO track_genres (track_id, genre_id)
                        SELECT %s, genre_id FROM genre
                        WHERE genre_name = %s
                    """), (
            track_id,
            genre_name
        ))


connection.commit()

# Close the cursor and connection
curr.close()
connection.close()
