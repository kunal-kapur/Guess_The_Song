from bs4 import BeautifulSoup

import requests

import re

website_string = "https://www.azlyrics.com/lyrics/"

def find_lyric_page(artist, song):
    artist = artist.lower().replace(" ", "")
    song = song.lower().replace(" ", "")
    #print(artist)

    if (artist[0:3] == "the"):
        artist = artist[3:]
    lyric_link = website_string + artist + "/" + song + ".html"

    page = requests.get(lyric_link)
    #print(lyric_link)
    return page

def scrape_lyrics(artistname, songname):
    artistname2 = str(artistname.replace(' ','-')) if ' ' in artistname else str(artistname)
    songname2 = str(songname.replace(' ','-')) if ' ' in songname else str(songname)
    url = 'https://genius.com/'+ artistname2 + '-' + songname2 + '-' + 'lyrics'
    print("url", url)
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics1 = html.find("div", class_="lyrics")
    lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-6 jYfhrf")
    if lyrics1:
        lyrics = lyrics1.get_text()
    elif lyrics2:
        lyrics = lyrics2.get_text()
    elif lyrics1 == lyrics2 == None:
        lyrics = None
    return lyrics

def clean_lyrics(lyrics):
    new_lyrics = ""
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    exlcuding = False
    print(lyrics)
    for i in range(len(lyrics)):
        if (lyrics[i] == "["):
            exclusion = True
            continue
        elif (lyrics[i] == "]"):
            exclusion  = False
            new_lyrics += " "
            continue

        if (lyrics[i] not in punc and not exclusion):
            new_lyrics += (lyrics[i])
            if (i != len(lyrics) - 1):
                if (lyrics[i+1].isupper()):
                    new_lyrics += " "

    return new_lyrics


def get_lyrics(artist, song):
    scraped_lyrics = scrape_lyrics(artist, song)
    cleaned_lyrics = clean_lyrics(scraped_lyrics)
    print(cleaned_lyrics)

get_lyrics("Harry Styles", "As it was")
