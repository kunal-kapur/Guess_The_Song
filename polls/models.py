from django.db import models
import json
# Create your models here.

class song_info(models.Model):
    artist = models.CharField(max_length=200)
    song_name = models.CharField(max_length=200)
    lyric_list = models.JSONField()

    def _str_(self):
        return "Artist: " + self.artist + "\nSong: " + self.song_name


