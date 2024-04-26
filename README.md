First we created database and tables in postgresql with the help of pgadmin.
Then in python we import psycopg2 package to provide connection with database.
We connect database and insert values in table with the help of python.
The issue we faced is connect table with each other and also not able to print list value which are in dictionary in table for one column playlist_id.
to solve this issue we make playlist_id a foreign key in track table, so we successfully establish a relation between two tables playlist and track. and fetch the playlist_id from playlist table and print in track table.
When we closely monitor the data in table we saw that everytime we run the code it rewrite the data in tables means duplicate datas, so to solve this first we use turncate in sql to remove data and then we use constrain and conflict in our code to stop rewrite duplicate data and we successfully solve this issue.
We created unittest cases for function in unit.py file.
We add more data in json file.
then create for loop for playlist.
We removed 2 column(duration_min & duration_sec) in track table and create one new column duration_time, and print value for duration time.
create one new table track_genres for relationship between track and genres. add two column track_id and genres_id and successfully print value inside table.
Create album table and successfully insert all values in album table.
Then we add try except blocks for exception handling.
We add a email validation for the playlist table, so whenever we try to insert email value in playlist table it check that email is valid or not if the email is valid then it insert the value for all column otherwise it skip that data and move to the next data, and print output like ('Email is not valid please check your email data. ',email).
