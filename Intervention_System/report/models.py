from django.db import models

# class Mentor(models.Model):
#     mentorId = models.CharField(max_length=5, primary_key=True)
#     mentorName = models.CharField(max_length=200)  # Changed TextField to CharField for consistency
#     password = models.CharField(max_length=128)

# class Student(models.Model):
#     studentId = models.CharField(max_length=5, primary_key=True)
#     studentName = models.CharField(max_length=200)
#     password = models.CharField(max_length=128)

# class Admin(models.Model):
#     adminId = models.CharField(max_length=5, primary_key=True)
#     adminName = models.CharField(max_length=200)
#     password = models.CharField(max_length=128)

# class Appointment(models.Model):
#     mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     appointmentDate = models.DateField()
#     # Add any other fields relevant to the appointment

# class Report(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     reportCategory = models.CharField(max_length=100)  # Adjusted max_length for consistency
#     reportText = models.TextField()
#     # Add any other fields relevant to the report

class askjd(models.Model):
        appointmentDate = models.DateField()