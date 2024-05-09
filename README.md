## Database Setup:

Created database and tables in PostgreSQL using pgAdmin.

Imported psycopg2 package in Python to establish connection with the database.

Connected to the database and inserted values into tables using Python.

## Establishing Relationships:

Made playlist_id a foreign key in the track table to establish a relationship between playlist and track tables.

Successfully fetched playlist_id from the playlist table and displayed it in the track table.

## Preventing Data Duplication:

Implemented constraints and conflict resolution in the code to prevent rewriting duplicate data.

Used SQL's truncate command to remove existing data before inserting new data.

## Unit Testing:

Created unittest cases for functions in the unit.py file to ensure code reliability.

## Enhancements and Modifications:

Added more data to the JSON file and implemented a for loop for playlist creation.

Removed two columns (duration_min & duration_sec) in the track table and created a new column, duration_time.

Created a new table, track_genres, to establish a relationship between track and genres.

## Exception Handling:

Added try-except blocks for exception handling to ensure robustness and graceful error handling.

## Data Validation:

Implemented email validation for the playlist table to ensure the validity of email addresses.

Added date validation for the release_date in the track and album tables to ensure dates are present or in the past.

Implemented integer value validation for popularity and duration_ms columns.

Implemented alphabet validation for playlist_name, description, artist, and username.

Implemented punctuation validation for track_name and album_name.

## Code Organization:

Moved validation methods to a separate file named validation.py for better code organization.

Moved database connection logic to a separate file named db_connection.py.

Shifted PostgreSQL queries to a separate file named sqlStatements.py for better management of database schema changes.

Started creating tables programmatically within Python code using PyCharm for better separation of concerns.
