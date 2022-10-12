# Spotify-Playlist-Maker
Creates a playlist in your spotify account that contains the top 100 songs of the date you input.

This code uses the spotipy module. 

use the self.make_playlist(self, date) to make a playlist that has the top 100 songs of the given date.

use the self.search_song(self, song, artist=None, year=None, album=None, genre=None) method to search for a song and get the id of the top result. 

use the self.create_playlist(self, name, description, public=False) to create a playlist in yout spotify account.

use the self.add_songs(self, playlist_id, song_id) to add a song to a playlist.

use the self.get_songs(self, date) method to webscrape the top 100 songs of a date from billboard.com.

use the self.get_song_ids(self, songs, artists) to ge tthe song ids from a list of song titles and artists.

