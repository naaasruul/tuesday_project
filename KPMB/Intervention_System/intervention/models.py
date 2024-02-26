from django.db import models

# Create your models here.

class Mentor(models.Model):
    mentorId = models.CharField(max_length=5, primary_key=True)
    mentorName = models.CharField(max_length=200)  # Changed TextField to CharField for consistency
    password = models.CharField(max_length=128)

class Student(models.Model):
    studentId = models.CharField(max_length=5, primary_key=True)
    studentName = models.CharField(max_length=200)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)
    address = models.TextField(blank=True, null=True ,default="Value not set")
    phone = models.CharField(blank=True , default="Value not set", null=True,max_length=15)
    course = models.CharField(blank=True , default="Value not set", null=True,max_length=15)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

class Admin(models.Model):
    adminId = models.CharField(max_length=5, primary_key=True)
    adminName = models.CharField(max_length=200)
    password = models.CharField(max_length=128)

class Appointment(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    appointmentDate = models.DateField()
    venue = models.CharField(max_length=100)
    time = models.TimeField()
    description = models.TextField(blank=True, null=True, default="-")
    purpose = models.TextField(blank=True, null=True, default="-")
    status = models.CharField(max_length=8, default="Pending...")
    # Add any other fields relevant to the appointment

class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reportCategory = models.CharField(max_length=100)  # Adjusted max_length for consistency
    reportText = models.TextField()
    # Add any other fields relevant to the report