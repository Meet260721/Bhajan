"""This file for all validation"""

from datetime import datetime, date
from email_validator import validate_email,EmailNotValidError

# function for validating release_date
def is_valid_date(input_date):
    try:
        dateObject = datetime.strptime(input_date, "%Y-%m-%d")
        if dateObject.date() <= date.today():
            return True
        else:
            # raise ValueError("Date cannot be in the future")
            print(f"Date cann't be in the future ' {input_date} ', enter past or present date.")
            return False
    except ValueError:
        # raise ValueError("Incorrect date formate for , it should be YYYY-MM-DD")
        print(f"Incorrect date formate for ' {input_date} ', it should be YYYY-MM-DD")
        return False

# create function to validate the value(must be alphabet and space)
def is_valid_alpha(input_data):
    input_dec = input_data.replace('.', '')
    # Check if description contains only alphabets and spaces
    if input_dec.replace(' ', '').isalpha():
        if len(input_dec) >= 6:
            return True
        else:
            print(f"Length of  ' {input_data} ' must be >=6.")
            return False
    else:
        print(f" ' {input_dec} ' must contain only alphabets and spaces.")
        return False

# create function to validate the value(must be alphabet, space and punctuation)
def is_valid_special_character(input_data):
    # Check if description contains only alphabets,special character(punctuation) and spaces
    if input_data.isascii():
        if len(input_data) >= 6:
            return True
        else:
            print(f"Length of  ' {input_data} ' must be >=6.")
            return False
    else:
        print(f" ' {input_data} ' must contain alphabets,punctuation and spaces.")
        return False

# Validating the value of playlist username
def is_valid_username(input_data):
    input_under = input_data.replace('_', '')
    # Check if username contains only alphabets, numbers, and underscores
    if input_under.isalnum():
        if len(input_under) >= 6:
            return True
        else:
            print(f"Length of Username ' {input_data} ' must be >=6.")
            return False
    else:
        print(f"Username ' {input_data} ' must contain only alphabets, numbers, or underscores.")
        return False

# Validating the value of paylist Email
def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

#CHECK IF INPUT_DATA IS INTEGER OR NOT
def is_valid_integer(input_data):
    if isinstance(input_data, int):
        return True
    else:
        print(f"'{input_data}' is not an integer")
        return False

# Validate playlist details
def is_valid_playlist(playlist_data):
    """This function for validate a playlist data"""
    input_playlist_name = playlist_data['playlist_name']
    input_description = playlist_data['description']
    input_username = playlist_data['creator']['username']
    email = playlist_data['creator']['email']
    return all([is_valid_alpha(input_playlist_name),
                is_valid_alpha(input_description),
                is_valid_username(input_username),
                is_valid_email(email)])

# Validate track details
def is_valid_track(track):
    """This function for validate a track data"""
    input_track_name = track['track_name']
    input_artist = track['artist']
    input_album_name = track['album']['name']
    input_date = track['album']['release_date']
    input_popularity = track['popularity']
    input_durationtime = track['duration_ms']
    return all([is_valid_special_character(input_track_name),
                is_valid_alpha(input_artist),
                is_valid_special_character(input_album_name),
                is_valid_date(input_date),
                is_valid_integer(input_durationtime),
                is_valid_integer(input_popularity)])

# Validate all json details
def is_valid_json(spotify_json):
    """This function for validate a json data"""
    for playlist_data in spotify_json:
        if is_valid_playlist(playlist_data):
            for track in playlist_data['tracks']:
                if is_valid_track(track):
                    pass
                else:
                    print("Validation failed for track details.")
                    return False
        else:
            print("Validation failed for playlist details.")
            return False
    return True
