## Project Description:

Our project endeavors to develop a comprehensive and efficient database management system tailored for music playlist management. Leveraging PostgreSQL as the database engine and Python for backend scripting, we implemented a suite of features to ensure seamless data management, robust relationships, and reliable data validation.

## Database Setup:

##### 1] Creating Database in PostgreSQL using pgAdmin.

Created database in PostgreSQL using pgAdmin.

Imported psycopg2 package in Python to establish connection with the database.

Connected to the database then create tables and inserted values into tables using Python.

##### 2] Creating Database in AWS Redshift service.

Create cluster on AWS Redshift then create database in it.

Get the crediantial details for that database and connect it with using python code.

## Establishing Relationships:

Made playlist_id,album_id a foreign key in the track table to establish a relationship between playlist table and track table, album table and track tables.

Made track_id,genre_is a foreign key in the track_genres table to establish a relationship between track_genres table and track table, genres table and track_genres tables.

Successfully fetched playlist_id, album_id from the playlist table, album table and displayed it in the track table. Also fetched genre_id, track_id from the genres table, tracks table and displayed it in the track_genres table.

![ER Diagram for tables](https://github.com/Meet260721/Songs/blob/main/ER%20Diagram.jpg)

## Preventing Data Duplication and Modification:

Implemented constraints and conflict resolution in the code to prevent rewriting duplicate data.

Used SQL's Drop command to delete existing table before creating table and inserting new data again.

Removed two columns (duration_min & duration_sec) in the track table and created a new column, duration_time.

#### Indexing in SQL

Create index which improve the performance of queries that involve searching for specific tracks by name or artist, as well as queries that involve sorting or grouping by track name and artist.

However, it's important to consider the overall database design and usage patterns before creating indexes, as they can consume additional storage space and may impact the performance of write operations (such as inserts, updates, and deletes) due to the overhead of maintaining the index.

## Unit Testing:

Created unittest cases for functions in the unit.py file to ensure code reliability.

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

## Tableau Dashboard Setup

This section describes how to set up and visualize the PostgreSQL tables in Tableau.

#### Prerequisites

###### Ensure you have the following before starting:

Database with the tables playlist, tracks, genres, album, and track_genres.

Connection details for your PostgreSQL database (host, port, database name, username, and password). If you are using AWS Redshift intance then get the connection details from the AWS Redshift cluster.

#### Connecting to PostgreSQL Database

##### 1] Open Tableau Desktop:

Launch Tableau Desktop.

##### 2] Connect to PostgreSQL:

On the start page, under Connect, select PostgreSQL. If you are using AWS Redshift then under Connect, select Amazon Redshift.

Enter your  connection details:

        Server: The hostname (e.g., localhost or 192.168.1.100).
        
        Port: 5432 (or your custom port).
        
        Database: Your database name.
        
        Username: Your PostgreSQL username.
        
        Password: Your PostgreSQL password.
        
Click Sign In to establish the connection.

#### Importing and Joining Tables

##### 1] Select Tables:

Once connected, you will see a list of schemas and tables in your PostgreSQL database.

Drag and drop the following tables into the canvas area: playlist, tracks, genres, album, and track_genres.

##### 2] Define Joins:

Join the tables to create a comprehensive view:

        tracks table with playlist table on playlist_id.
        
        tracks table with album table on album_id.
        
        track_genres table with tracks table on track_id.
        
        track_genres table with genres table on genre_id.

#### Creating Sheets

##### 1] Sheet 1: Playlists Overview:

        Columns: playlist_name
        
        Rows: COUNT(tracks.track_id) to show the number of tracks per playlist.
        
        Color: creator_username to differentiate by creator.
        
##### 2] Sheet 2: Album Popularity:

        Columns: album_name
        
        Rows: SUM(tracks.popularity) to show the total popularity of each album.
        
        Color: release_date to show albums by release year.
        
##### 3] Sheet 3: Track Genre Distribution:

        Columns: genre_name
        
        Rows: COUNT(tracks.track_id) to show the number of tracks per genre.
        
#### Building the Dashboard

##### 1] Create a New Dashboard:

Click on the New Dashboard icon in Tableau.

##### 2] Add Sheets to the Dashboard:

Drag and drop the created sheets (Sheet 1, Sheet 2, Sheet 3) onto the dashboard.

##### 3] Arrange Sheets:

Arrange the sheets within the dashboard to create a cohesive layout.

Use Vertical or Horizontal Layout Containers to manage the positioning of sheets.

##### 4] Add Titles and Formatting:

Add titles to each section for clarity.

Adjust the formatting to ensure a clean and professional appearance.

#### Example Dashboard Layout

**Top Left Section : Playlist Overview**

Show the number of tracks per playlist, color-coded by creator username.

**Top Right Section: Track Genre Distribution**

Display the distribution of tracks across different genres.

**Bottom Section: Album Popularity**

Visualize the total popularity of each album, with a color gradient representing the release year.

#### Dashboard Created in tableu

![Dashboard in Tableu](https://github.com/Meet260721/Songs/blob/main/Tableu%20Dashboard.jpeg) 

## Steps to Run

##### 1] If you are creating Database in PostgreSQL using pgAdmin.

Create database in PostgreSQL with help of pgAdmin.

In `main.py` update the below details according to your database.

        dbname="DatabaseName",  # Insertyourdatabasename
        
        user="UserName",  # Insertyourusername
        
        password="Password",  # InsertYourpassword
        
        host="HostName",  # InsertYourHostName
        
        port="Portnumber"  # InsertYourportnumber

##### 2] If you are creating Database in AWS Redshift service.

Create cluster and database in AWS Redshift service.

In `main.py` update the below details according to your database.

        RS_HOST = " YOUR AWS REDSHIFT HOST NAME"  # Insert Your AWS Redshift Host Name
        
        RS_DATABASE = "YOUR AWS REDSHIFT DATABASE NAME" # Insert your AWS Redshift database name
        
        RS_USER = "YOUR AWS REDSHIFT USER NAME" # Insert your AWS Redshift username
        
        RS_PORT = "YOUR AWS REDSHIFT PORT NAME" # Insert Your AWS Redshift port number
        
        RS_PASSWORD = "YOUR AWS REDSHIFT PASSWORD " # Insert Your AWS Redshift password

### Set up AWS S3 bucket 

Set up an S3 bucket in AWS and upload the `Songs.json` file to the bucket.

Configure the AWS credentials in your environment or directly in the code using AWS CLI or SDK.

Install AWSCLI :- 

        pip install awscli

Create users in AWS with the help of service IAM. you can create YOUR AWS ACCESS KEY there. make sure to download your ACCESS KEY
.csv file because you can see YOUR AWS SECRET ACCESS KEY only once while you are creating it.

Update the below details according to your YOUR AWS ACCESS KEY,  YOUR AWS SECRET ACCESS KEY, YOUR BUCKET NAME and YOUR JSON FILE NAME .

        s3 = boto3.client('s3',aws_access_key_id = "YOUR AWS ACCESS KEY",aws_secret_access_key = "YOUR AWS SECRET ACCESS KEY")

        bucket_name = "YOUR BUCKET NAME" # Insert your bucket name
        file_name = "YOUR JSON FILE NAME"# MINE WAS Songs.json


Run the `main.py` script by executing below command in terminal.

        python3 main.py        
