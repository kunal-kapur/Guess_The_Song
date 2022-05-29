import requests
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from Find_lyrics import extract_lyrics

file = open(".gitignore")
lines = file.readlines()
for i in list(lines):
    lines.pop(0)
    lines.append(i[0:len(i)-1])
cid = lines[0]
secret = lines[1]
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
songs = {}
top_50 = sp.playlist("37i9dQZEVXbLRQDuF5jeBp")['tracks']['items']

for song_info in top_50:
    artist = song_info['track']['artists'][0]['name']
    name = song_info['track']['name']
    print(artist,name)
    songs[(artist,name)] = extract_lyrics(artist, name)

print(songs)


