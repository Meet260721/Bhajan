First we created database and tables in postgresql with the help of pgadmin.
Then in python we import psycopg2 package to provide connection with database.
We connect database and insert values in table with the help of python.
The issue we faced is connect table with each other and also not able to print list value which are in dictionary in table for one column playlist_id.
to solve this issue we make playlist_id a foreign key in track table, so we successfully establish a relation between two tables playlist and track. and fetch the playlist_id from playlist table and print in track table.
When we closely monitor the data in table we saw that everytime we run the code it rewrite the data in tables means duplicate datas, so to solve this first we use turncate in sql to remove data and then we use constrain and conflict in our code to stop rewrite duplicate data and we successfully solve this issue.
We created unittest cases for function in unit.py file.
