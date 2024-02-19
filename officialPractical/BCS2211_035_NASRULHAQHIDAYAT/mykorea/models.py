from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField(max_length=200)
    releaseDate = models.DateField(null=True)
    genre = models.TextField(max_length=200)
    rating = models.IntegerField(default=6)

class Actor(models.Model):
    actorID = models.CharField(max_length=3, primary_key=True)
    actorName = models.TextField(max_length=200)
    actorBirthDate = models.DateField(null=True)

class ActorMovie(models.Model):
    actorID = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    castName = models.TextField(max_length=200)






























#     from django.db import models


# # Create your models here.
# class Singer(models.Model):
#     singerID = models.CharField(max_length=3, primary_key=True)
#     singerName = models.CharField(max_length=128)
#     singerOrigin = models.CharField(max_length=128)


# class Album(models.Model):
#     albumName = models.CharField(max_length=128)
#     singerID = models.ForeignKey(Singer, on_delete = models.CASCADE)
#     albumYear = models.PositiveIntegerField()

# class Song(models.Model): 
#     songID = models.CharField(max_length=6, primary_key =True)
#     albumName = models.ForeignKey(Album, on_delete = models.CASCADE)
#     songName = models.CharField(max_length=128)
#     minutes = models.PositiveIntegerField()
#     songStatus = models.CharField(max_length=128, default="Hit")

