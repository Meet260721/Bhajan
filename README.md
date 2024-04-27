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
We add a email validation for the playlist table, so whenever we try to insert email value in playlist table it check that email is valid or not if the email is valid then it insert the value for all column otherwise it skip that data and move to the next data, and print output like ('Email is not valid please check your email data. ',email). At this point first we face one issue with validate_email package cheking  but  email_validator library give us normalizing email addresses and validating against a list of common disposable email services.
Then we continue to add code for date validation for the release_date in track table and album table. For it we use the datetime package and its different class. First we specify the formate of date like "%Y-%m-%d" with use of 'datetime.strptime' and we also checked that date must present or in past. if it's fututre date then it will don't allow to insert value in table means the validation is false.
We add code for the integer value validation for the duration_ms and popularity. we checked that popularity must be in between 0 to 100 and its integer and duration time must be >= 100000 in ms and integer. if not than it don't allow to insert the data in table.
Then we write code for the alphabet validation for playlist_name, description and artist. The issue we got is space and "." in string, so we replace the space and "." with ""(no space, no ".") and cheked alphabet validation. we used isalpha() module for the validation.
we also cheked alphabet and numeric validate for username. in this validation we allow alphabet, numeric and '_' in username. we used isalnum() module for the validation.
punctuation validation for track_name,album_name. in this validation we allow some special (punctuation) like '(', ')', '.' and etc.we used isascii() module for the validation.
