from django.db import models

# Create your models here.
class Authors(models.Model):
    authorID = models.AutoField(primary_key=True,unique=True, blank=False)
    firstName = models.TextField(max_length=128)
    lastName = models.TextField(max_length=128,blank=True)

class Book(models.Model):
    bookID = models.AutoField(primary_key=True, unique=True, blank=False)
    title = models.TextField(max_length=128)
    authorID = models.ForeignKey(Authors, on_delete=models.CASCADE)
    genre = models.TextField(max_length=128)
    pages = models.PositiveIntegerField()
    bookStatus = models.CharField(max_length = 128,default="Not Approved")

class Readers(models.Model):
    readerID = models.AutoField(primary_key=True, unique=True, blank=False)
    firstName = models.TextField(max_length=128)
    lastName = models.TextField(max_length=128,blank=True)