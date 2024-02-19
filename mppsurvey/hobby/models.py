from django.db import models

# Create your models here.
class Mentor(models.Model):
    mentorId = models.CharField(max_length=5)
    mentorName = models.TextField(max_length=200)
    roomNo = models.CharField(max_length=5)

# class Student