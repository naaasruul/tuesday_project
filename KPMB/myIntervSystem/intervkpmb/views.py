from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

from intervkpmb.models import Lecturer, Student,Report,Message
# Create your views here.
def login(request):
    if request.method == "POST":
        input_username = request.POST["username"]
        input_password = request.POST["password"]

        try:
            lect = Lecturer.objects.get(lectId=input_username, lectPass=input_password)
            # Redirect to lecturer page upon successful login
            return redirect('mainpage', lectID=lect.lectId)
        except Lecturer.DoesNotExist:
            # Handle invalid lecturer ID or password
            error_message = {"message": "Invalid Lecturer ID or password"}
            return render(request, 'login.html', error_message)

    else:
        return render(request, 'login.html')


def mainpage(request, lectID):
    lect = Lecturer.objects.get(lectId=lectID)
    stu = Student.objects.get(stuLec=lect)
    allstu = Student.objects.all().values
    repo = Report.objects.filter(mentor=lectID)
    message = Message.objects.filter(mentor=lectID)
    obj = {
            'lecturer':lect,
            'student':stu,
            'students':allstu,
            'report':repo,
            'message':message,
        }
    return render(request, 'index.html', obj)

def mystudent(request,lectID):
    allStu = Student.objects.all().values()
    lect = Lecturer.objects.get(lectId=lectID)
    obj = {
        'allStudents' : allStu,
        'lecturer':lect
    }


    return render(request, 'lectstudent.html',obj)

def viewAddStudent(request, lectID):
    lect = Lecturer.objects.get(lectId=lectID)
    allLect = Lecturer.objects.all().values
    obj = {
        # 'allStudents' : allStu,
        'lecturer':lect,
        'allLect':allLect
    }
    return render(request, 'addStudentForm.html', obj)

def submitAddStudent(request, lectID):
    if request.method == "POST":
        stuId = request.POST['studentId']
        stuName = request.POST['studentName']
        stuLect = request.POST['mentorId']
        stuPass = request.POST['password']

        lect = Lecturer.objects.get(lectId = stuLect)

        addStudent = Student(stuId=stuId,stuName=stuName, stuLec=lect, stuPass=stuPass)
        addStudent.save()

    return redirect('mystudent', lectID = lectID)
    # return render(request, 'test.html',context)

def viewReport(request, lectID):
    lect = Lecturer.objects.get(lectId=lectID)
    allLect = Lecturer.objects.all().values

    allStu = Student.objects.all().values()
    obj = {
        # 'allStudents' : allStu,
        'lecturer':lect,
        'allLect':allLect,
        'allStu':allStu
    }
    return render(request, 'addReport.html',obj)

def submitReport(request, lectID):
    if request.method == "POST":
        reportStuId = request.POST['student']
        reportLect = request.POST['mentor']
        reportDate = request.POST['date']
        reportDetail = request.POST['reportdetails']

        lect = Lecturer.objects.get(lectId = reportLect)
        stu = Student.objects.get(stuId=reportStuId)

        addReport = Report(student=stu,mentor=lect,date=reportDate,reportText=reportDetail)
        addReport.save()

    return redirect('mainpage', lectID=lectID)