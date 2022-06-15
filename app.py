from flask import Flask, render_template, request
#from Get_songs import update_songs
import random

from create_db import Song_Info



app = Flask(__name__)

#current_top_50_info = update_songs()

def get_random_song():
    #entry_list = list(current_top_50_info.items())
    # random_entry = random.choice(entry_list)
    # print("\n",random_entry)
    new_song = ("Swae", "Unforgettable", ["And you are unforgettable", "I need to get you alone",
    "why not"])
    return new_song

#get_random_song()

counter = 1
new_song = get_random_song()

@app.route('/', methods=['GET', 'POST'])
def index():

    if (request.method == "GET"):
        if (request.form['more_lyrics'] == 'More'):
            counter += 1
            return render_template("home.html",lyric_list = new_song[2][0:counter])

    return render_template("home.html",lyric_list = new_song[2]
    )

if __name__ == '__main__':
    app.run(host='localhost', port=3000)




