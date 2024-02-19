from django.db import models

# Create your models here.
class Student(models.Model):
    stuId = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.BooleanField(default=True)  # True: male, False: female