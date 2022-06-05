from flask import Flask, render_template
#from Get_songs import update_songs
import random



app = Flask(__name__)

#current_top_50_info = update_songs()


@app.route('/')
def index():

    return render_template("home.html",lyric_list = ["here", "there", "Everywhere"])



# def get_random_song():
#     #entry_list = list(current_top_50_info.items())
#     random_entry = random.choice(entry_list)
#     print("\n",random_entry)

#get_random_song()
if __name__ == '__main__':
    app.run(host='localhost', port=3000)




