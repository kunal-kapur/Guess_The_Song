import requests
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from Find_lyrics import get_lyrics


def update_songs():
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
    count = 1
    for song_info in top_50:
        artist = song_info['track']['artists'][0]['name']
        name = song_info['track']['name']
        print(count,artist,name)
        count += 1
        recieved_lyrics = get_lyrics(artist, name)
        if recieved_lyrics:
            songs[(artist,name)] = get_lyrics(artist, name)

    return songs


    



