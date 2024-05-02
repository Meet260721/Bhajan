# Query for create playlist table
playlist_create_table_query = """
                            CREATE TABLE IF NOT EXISTS playlist (playlist_id SERIAL PRIMARY KEY,
                                playlist_name VARCHAR(255),
                                description TEXT,
                                creator_username VARCHAR(255),
                                creator_email VARCHAR(255),
                                CONSTRAINT playlist_unique_constraint UNIQUE (playlist_name, creator_username))
                            """

# Query for create album table
album_create_table_query = """
                            CREATE TABLE IF NOT EXISTS album (album_id SERIAL PRIMARY KEY,
                                name VARCHAR(255),
                                release_date DATE,
                                CONSTRAINT album_unique_constraint UNIQUE (name, release_date))
"""

# Query for create tracks table
tracks_create_table_query = """
                            CREATE TABLE IF NOT EXISTS tracks (track_id SERIAL PRIMARY KEY,
                                playlist_id INTEGER,
                                album_id INTEGER,
                                track_name VARCHAR(255),
                                artist VARCHAR(255),
                                album_name VARCHAR(255),
                                release_date DATE,
                                duration_time VARCHAR(255),
                                popularity INTEGER,
                                genres VARCHAR(255), 
                                explicit_content BOOLEAN,
                                CONSTRAINT tracks_unique_constraint UNIQUE (track_name, artist))
"""

# Query for create genres table
genres_create_table_query = """
                            CREATE TABLE IF NOT EXISTS genres (genre_id SERIAL PRIMARY KEY,
                                genre_name VARCHAR(255),
                                CONSTRAINT genres_unique_constraint UNIQUE (genre_name))
"""

# Query for create track_genres table
track_genres_create_table_query = """
                            CREATE TABLE IF NOT EXISTS track_genres (track_id INTEGER,
                                genre_id INTEGER ,
                                PRIMARY KEY(track_id, genre_id),
                                CONSTRAINT track_genres_unique_constraint UNIQUE (track_id, genre_id))
"""

#Query for insert value in playlist table
playlist_insert_query ="""
                        INSERT INTO playlist (playlist_name, description, creator_username, creator_email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (playlist_name, creator_username) DO NOTHING
                     """

#Query for retrieve playlist_id
playlist_id_retrieve_query ="""
                                SELECT playlist_id FROM playlist 
                                WHERE playlist_name = %s AND creator_username = %s
                            """

#Query for insert value in album table
album_insert_query = """
                        INSERT INTO album (name, release_date)
                        VALUES (%s, %s)
                        ON CONFLICT DO NOTHING
                    """

#Query for retrieve album_id

album_id_retrieve_query = """
                           SELECT album_id FROM album
                           WHERE name = %s AND release_date = %s
                           """

#Query for insert value in track table
track_insert_query = """
                        INSERT INTO tracks (track_name,playlist_id, artist, album_name, release_date, duration_time, popularity, genres, explicit_content, album_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (track_name, artist) DO NOTHING
                        """

#Query for retrieve track_id

track_id_retrieve_qurey = """
                            SELECT track_id FROM tracks
                            WHERE track_name = %s AND artist = %s
                            """

#Query for insert value in genres table
genres_insert_query = """
                        INSERT INTO genres (genre_name)
                        VALUES (%s)
                        ON CONFLICT (genre_name) DO NOTHING
                     """

#Query for retrieve genres_id

track_genres_insert_query = """
                            INSERT INTO track_genres (track_id, genre_id)
                            SELECT %s, genre_id FROM genres
                            WHERE genre_name = %s
                            """
