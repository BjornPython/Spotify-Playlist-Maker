import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup


class PlaylistMaker:

    def __init__(self, client_id, client_secret, redirect_uri, user_id):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri
        self.USER_ID = user_id
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=self.REDIRECT_URI,
                client_id=self.CLIENT_ID,
                client_secret=self.CLIENT_SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )

    def search_song(self, song, artist=None, year=None, album=None, genre=None):
        q = (
            {
                "track": song
            }
        )

        if artist is not None:
            q["artist"] = artist
        if year is not None:
            q["year"] = year
        if album is not None:
            q["album"] = album
        if genre is not None:
            q["genre"] = genre

        query = urlencode(q)

        search_result = self.sp.search(q=query, type="track")

        try:
            song = search_result["tracks"]["items"][0]["uri"]
        except IndexError:
            song = None
        return song

    def create_playlist(self, name, description, public=False):
        response = self.sp.user_playlist_create(user=self.USER_ID, name=name, public=public, description=description)
        return response["id"]

    def add_songs(self, playlist_id, song_id):
        response = self.sp.playlist_add_items(playlist_id=playlist_id, items=song_id, position=0)
        return response

    def get_songs(self, date):
        website = f"https://www.billboard.com/charts/hot-100/{date}/"

        response = requests.get(website).text

        soup = BeautifulSoup(response, "html.parser")

        titles = soup.find_all(name="h3", class_="a-no-trucate")
        songs = [song.getText().strip() for song in titles]

        artists = soup.find_all(name="span", class_="a-no-trucate")
        artists = [artist.getText().strip() for artist in artists]

        return songs, artists

    def get_song_ids(self, songs, artists):
        song_id = []
        for index in range(len(songs)):
            print(index)
            id = self.search_song(songs[index], artist=artists[index])
            if id is not None:
                song_id.append(id)
        return song_id

    def make_playlist(self, date):
        songs, artists = self.get_songs(date)
        song_ids = self.get_song_ids(songs, artists)

        playlist_id = self.create_playlist(f"{date} Top 100", f"The top songs of {date}")

        response = self.add_songs(playlist_id=playlist_id, song_id=song_ids)
        return response
