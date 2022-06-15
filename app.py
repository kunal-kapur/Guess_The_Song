from flask import Flask, render_template, request
#from Get_songs import update_songs
import random
from Song_Info import db, Song_Info
from Find_lyrics import clean_lyrics



app = Flask(__name__)

#current_top_50_info = update_songs()

def get_random_song():

    given = Song_Info.query.filter_by(artist='Harry Styles').first()
    artist = given.artist
    song_name=  given.title
    lyrics = clean_lyrics(given.lyrics)
    new_song = (artist, song_name, lyrics)
    return new_song

#get_random_song()

counter = 1
new_song = get_random_song()



@app.route('/', methods = ["GET", "POST"])
def index():
    
    if (request.method == "GET"):
        print(request.args)
        print("HERE")
        print(len(request.form))
        # if (request.form['more_lyrics'] == 'more'):
        #     counter += 1
        #     return render_template("home.html",lyric_list = new_song[2][0:counter])
           
    return render_template("home.html",lyric_list = new_song[2][0:counter])

    #return render_template("home.html",lyric_list = new_song[2])

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)




