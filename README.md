
## Project Description:

Our project endeavors to develop a comprehensive and efficient database management system tailored for music playlist management. Leveraging PostgreSQL as the database engine and Python for backend scripting, we implemented a suite of features to ensure seamless data management, robust relationships, and reliable data validation.

## Database Setup:

Created database in PostgreSQL using pgAdmin.

Imported psycopg2 package in Python to establish connection with the database.

Connected to the database then create tables and inserted values into tables using Python.

## Establishing Relationships:

Made playlist_id,album_id a foreign key in the track table to establish a relationship between playlist table and track table, album table and track tables.

Made track_id,genre_is a foreign key in the track_genres table to establish a relationship between track_genres table and track table, genres table and track_genres tables.

Successfully fetched playlist_id, album_id from the playlist table, album table and displayed it in the track table. Also fetched genre_id, track_id from the genres table, tracks table and displayed it in the track_genres table.




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

## Steps to Run

Create database in PostgreSQL with help of pgAdmin.

In db_connection.py update the 

        dbname="DatabaseName",  # Insertyourdatabasename
        
        user="UserName",  # Insertyourusername
        
        password="Password",  # InsertYourpassword
        
        host="HostName",  # InsertYourHostName
        
        port="Portnumber"  # InsertYourportnumber

according to your database details.

Make sure that Songs.json file located in same folder where is main.py . 

Set up an S3 bucket in AWS and upload the `Songs.json` file to the bucket.

Configure the AWS credentials in your environment or directly in the code using AWS CLI or SDK.

Install AWSCLI :- 
pip install awscli

Check Version :- 
aws --version

Run the `main.py` script by executing `python main.py` or `python3 main.py` in your terminal.

