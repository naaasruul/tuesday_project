from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

# from report.models import Mentor, Student, Admin, Report  # Import the Student model

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]

        if role == "1":  # Student login
            try:
                student = Student.objects.get(studentId=username, password=password)
                studentData = {
                    'student': student,
                    "message": "successfully"
                }
                # Redirect to student page upon successful login
                return redirect('studentPage', studentId=student.studentId)
            except Student.DoesNotExist:
                # Handle invalid student ID or password
                message = {"message": "Invalid student ID or password"}
                return render(request, 'login.html', message)

        elif role == "2":  # Lecturer login
            try:
                lecturer = Mentor.objects.get(mentorId=username, password=password)
                lectData = {
                    'mentor': lecturer,
                    "message": "successfully"
                }
                # Redirect to lecturer page upon successful login
                return redirect('lecturerPage', mentorId=lecturer.mentorId)
            except Mentor.DoesNotExist:
                # Handle invalid lecturer ID or password
                lectData = {"message": "Invalid Lecturer ID or password"}
                return render(request, 'login.html', lectData)

        elif role == "3":  # Admin login
            try:
                admin = Admin.objects.get(adminId=username, password=password)
                adminData = {
                    'admin': admin,
                    "message": "successfully"
                }
                # Redirect to admin page upon successful login
                return render(request, 'admin_page.html', adminData)
            except Admin.DoesNotExist:
                # Handle invalid admin ID or password
                adminData = {"message": "Invalid Admin ID or password"}
                return render(request, 'login.html', adminData)

        else:
            # Handle invalid role
            message = {"message": "Invalid role"}
            return render(request, 'login.html', message)
    else:
        return render(request, 'login.html')



def studentPage(request, studentId):
    try:
        student = Student.objects.get(studentId=studentId)
        report = Report.objects.all().values
        student_details = {
            'studentDetails': student,
            'reports': report
        }

        return render(request, 'student_page.html', student_details)
    except Student.DoesNotExist:
        # Handle case where student with specified ID doesn't exist
        return HttpResponse("Student not found")

def lecturerPage(request, mentorId):
    try:
        lecturer = Mentor.objects.get(mentorId=mentorId)
        lecturer_details = {
            'lecturerDetails': lecturer
        }
        return render(request, 'lecturer_page.html', lecturer_details)
    except Mentor.DoesNotExist:
        # Handle case where mentor with specified ID doesn't exist
        return HttpResponse("Lecturer not found")

def adminPage(request, adminId):
    try:
        admin = Admin.objects.get(adminId=adminId)
        admin_details = {
            'adminDetails': admin
        }
        return render(request, 'admin_page.html', admin_details)
    except Admin.DoesNotExist:
        # Handle case where admin with specified ID doesn't exist
        return HttpResponse("Admin not found")

def viewsReport(request, mentorId):
    displayMentor = Mentor.objects.get(mentorId=mentorId)
    displayStudent = Student.objects.all().values()
    mentorDetails = {
        'mentorId': displayMentor,
        'studentId': displayStudent
        }

    return  render(request,'lectReport.html', mentorDetails)

def lectReport(request, mentorId):
    if request.method == "POST":
        menId = mentorId
        studentId = request.POST['reportStudentId']
        datetime = request.POST['reportDate']
        category = request.POST['reportCategory']
        description = request.POST['reportDesc']

        mentorID = Mentor.objects.get(mentorId=menId)
        stuID = Student.objects.get(studentId=studentId)

        report = Report(mentor=mentorID, student=stuID, date=datetime, reportCategory=category, reportText=description)
        report.save()
    
    return  redirect("lecturerPage",mentorId=mentorId)