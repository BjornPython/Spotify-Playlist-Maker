from spotipy_class import *
import os

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("SPOTIFY_REDIRECT_URI")
USER_ID = os.environ.get("SPOTIFY_USER_ID")

test = PlaylistMaker(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, USER_ID)

# Date is a string, and is in the format yyyy-mm-dd example: "1980-10-12"
date = ""
print(test.make_playlist("date"))
