import json
import boto3
from datetime import timedelta
import psycopg2
from psycopg2 import sql
from validation import SpotifyValidation
from db_connection import DatabaseConnector
import sqlStatements

try:
    # read file Songs.json from the AWS s3 bucket as file and loads data in spotify_json
    # insert your AWS Access credential
    s3 = boto3.client('s3',aws_access_key_id = "YOUR AWS ACCESS KEY",aws_secret_access_key = "YOUR AWS SECRET KEY")

    bucket_name = "YOUR BUCKET NAME" # Insert your bucket name
    file_name = "YOUR FILE NAME"# MINE WAS Songs.json

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    file = response['Body'].read()
    spotify_json = json.loads(file)
except FileNotFoundError:
    print("file Songs.json is not found.")
    exit()

# create function for convert duration time from millisecond to minutes
def duration_time(ms):
    t = timedelta(milliseconds= ms)
    min = int(t.seconds / 60)
    sec = int(t.seconds % 60)
    return f"{min}:{sec:02d}"

#creating empty list
genre_names = []

 # inserting value in table if and only all details are true
if SpotifyValidation.is_valid_json(spotify_json):
    # Connection to database
    db_connector = DatabaseConnector(
        dbname="DatabaseName",  # Insertyourdatabasename
        user="UserName",  # Insertyourusername
        password="Password",  # InsertYourpassword
        host="HostName",  # InsertYourHostName
        port="Portnumber"  # InsertYourportnumber
    )
    db_connector.database_connect()
    curr = db_connector.cursor

    # Create table playlist if it doesn't exist in database
    curr.execute(sql.SQL(sqlStatements.playlist_create_table_query))

    # Create table album if it doesn't exist in database
    curr.execute(sql.SQL(sqlStatements.album_create_table_query))

    # Create table tracks if it doesn't exist in database
    curr.execute(sql.SQL(sqlStatements.tracks_create_table_query))

    # Create table genres if it doesn't exist in database
    curr.execute(sql.SQL(sqlStatements.genres_create_table_query))

    # Create table track_genres if it doesn't exist in database
    curr.execute(sql.SQL(sqlStatements.track_genres_create_table_query))

    for playlist_data in spotify_json:
        try:
            # Insert values from the  json data to playlist  table  in database
            curr.execute(sql.SQL(sqlStatements.playlist_insert_query),
                (
                    playlist_data['playlist_name'],
                    playlist_data['description'],
                    playlist_data['creator']['username'],
                    playlist_data['creator']['email']
                ))
        except psycopg2.Error as e:
            print("Error occur while inserting in playlist table", e)

        for track in playlist_data['tracks']:
            # Create new variable to store genres data as single string
            genres_str = ','.join(track['genres'])
            try:
                #retrieve playlist_id
                curr.execute(
                    sql.SQL(sqlStatements.playlist_id_retrieve_query),
                    (playlist_data['playlist_name'], playlist_data['creator']['username'])
                )
                result = curr.fetchone()
                playlist_id = result[0] if result else None

                if playlist_id is not None:
                    # Insert album data into the album table
                    curr.execute(sql.SQL(sqlStatements.album_insert_query), (
                        track['album']['name'],
                        track['album']['release_date']
                    ))
                    # Get the album_id
                    curr.execute(sql.SQL(sqlStatements.album_id_retrieve_query), (
                        track['album']['name'],
                        track['album']['release_date']
                    ))
                    album_id = curr.fetchone()[0]

                    #insert value into track table
                    curr.execute(sql.SQL(sqlStatements.track_insert_query),
                        (
                            track['track_name'],
                            playlist_id,
                            track['artist'],
                            track['album']['name'],
                            track['album']['release_date'],
                            duration_time(track['duration_ms']),
                            track['popularity'],
                            genres_str,
                            track['explicit_content'],
                            album_id
                        ))
                    # track_id retrieve
                    curr.execute(sql.SQL(sqlStatements.track_id_retrieve_qurey), (
                        track['track_name'],
                        track['artist']
                    ))
                    track_id = curr.fetchone()[0]
            except psycopg2.Error as e:
                print("Error occur while inserting data in track table", e)

            # Extract genre names from the JSON data
            genre_names.extend(track['genres'])

        # Remove duplicate genre
        genre_names = list(set(genre_names))

        for genre_name in genre_names:
            try:
                # Insert genre data into the genre table
                curr.execute(sql.SQL(sqlStatements.genres_insert_query), (genre_name,))

                # genre_id retrieve and insert in track_genres table
                curr.execute(sql.SQL(sqlStatements.track_genres_insert_query), (
                    track_id,
                    genre_name
                ))
            except psycopg2.Error as e:
                print("Error occur while inserting data in genres table", e)

        db_connector.database_commit()
else:
    print("validation failed.")

# Close the cursor and connection
db_connector.database_disconnect()
