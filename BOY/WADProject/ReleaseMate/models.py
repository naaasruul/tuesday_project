from django.db import models

class Student(models.Model):
    StudentId = models.CharField(max_length=100, primary_key=True)
    StudentName = models.TextField(max_length=100)
    course = models.TextField(max_length=100)

class Mentor(models.Model):
    MentorID = models.CharField(max_length=100, primary_key=True)
    MentorName = models.TextField(max_length=100)
    LectRoom = models.CharField(max_length=10)

class TopManagement(models.Model):
    staffNo = models.CharField(max_length=1000, primary_key=True)
    staffName = models.TextField(max_length=100)

class Application(models.Model):
    AppsID = models.AutoField(primary_key=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    Program= models.TextField(max_length=1000)
    Status = models.TextField(max_length=10)
    ApplicationDate = models.DateField()
