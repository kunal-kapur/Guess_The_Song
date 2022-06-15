from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_info.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Song_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    lyrics = db.Column(db.Text(),nullable = False)

    def _repr_(self):
        return '<Artist %>' % self.artist

