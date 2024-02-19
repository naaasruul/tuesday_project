from django.db import models


# Create your models here.
class Singer(models.Model):
    singerID = models.CharField(max_length=3, primary_key=True)
    singerName = models.CharField(max_length=128)
    singerOrigin = models.CharField(max_length=128)


class Album(models.Model):
    albumName = models.CharField(max_length=128)
    singerID = models.ForeignKey(Singer, on_delete = models.CASCADE)
    albumYear = models.PositiveIntegerField()

class Song(models.Model): 
    songID = models.CharField(max_length=6, primary_key =True)
    albumName = models.ForeignKey(Album, on_delete = models.CASCADE)
    songName = models.CharField(max_length=128)
    minutes = models.PositiveIntegerField()
    songStatus = models.CharField(max_length=128, default="Hit")