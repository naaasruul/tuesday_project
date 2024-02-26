from django.db import models

# Create your models here.

# class Lecturer
class Lecturer(models.Model):
    lectId = models.CharField(max_length=5, primary_key=True)
    lectName = models.CharField(max_length=200)  # Changed TextField to CharField for consistency
    lectPass = models.CharField(max_length=128)

# class student
class Student(models.Model):
    stuId = models.CharField(max_length=5, primary_key=True)
    stuName = models.CharField(max_length=200)  # Changed TextField to CharField for consistency
    stuLec = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    stuPass = models.CharField(blank=True , null=True,max_length=15)

# class report
class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reportText = models.TextField()

class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    messageText = models.TextField()

