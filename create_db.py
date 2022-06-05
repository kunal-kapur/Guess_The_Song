from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_info.db'
db = SQLAlchemy(app)

db.create_all()

print("refreshed")
class Song_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    
    lyrics = db.Column(db.Text(),nullable = False)

