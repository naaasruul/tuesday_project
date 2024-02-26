from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

from intervention.models import Mentor, Student, Admin, Report, Appointment  # Import the Student model

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
                return redirect('adminPage', adminId=admin.adminId)
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
        # student = Student.objects.get(studentId=studentId)
        student = Student.objects.filter(studentId=studentId).values()
        report = Report.objects.filter(student= studentId).values()
        appointment = Appointment.objects.filter(student=studentId).values()
        mentorDetails = Mentor.objects.all().values
        totalRepo = Report.objects.filter(student=studentId).count()
        totalApp = Appointment.objects.filter(student=studentId).count()
        studentDetails = Student.objects.get(studentId=studentId)
        
        student_details = {
            'studentDetails': student,
            'studentDetails1':studentDetails,
            'reports': report,
            'appointmentDetails': appointment,
            'mentorDetails':mentorDetails,
            'totalReport':totalRepo,
            'totalApp':totalApp,
        }

        return render(request, 'student_page.html', student_details)
    except Student.DoesNotExist:
        # Handle case where student with specified ID doesn't exist
        return HttpResponse("Student not found")

def lecturerPage(request, mentorId):
    try:

        lecturer = Mentor.objects.get(mentorId=mentorId)
        report = Report.objects.all().values
        studentDetails = Student.objects.all().values
        appointment = Appointment.objects.filter(mentor=mentorId).values()
        totalPendingApp = Appointment.objects.filter(status="Pending...", mentor=mentorId).count()

        lecturer_details = {
            'lecturerDetails': lecturer,
            'reports': report,
            'studentDetails':studentDetails,
            'appointmentDetails': appointment,
            'totalPendingApp':totalPendingApp
        }
        return render(request, 'lecturer_page.html', lecturer_details)
    except Mentor.DoesNotExist:
        # Handle case where mentor with specified ID doesn't exist
        return HttpResponse("Lecturer not found")


def viewsReport(request, mentorId):
    displayMentor = Mentor.objects.get(mentorId=mentorId)
    displayAllStudent = Student.objects.all().values()
    displayStudent = Student.objects.filter(mentor=mentorId)
    mentorDetails = {
        'mentorId': displayMentor,
        'studentId': displayAllStudent
        }

    return  render(request,'lectReport.html', mentorDetails)

# START REPORT SECTION
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


def viewUpdateReport(request,repId):
    repoDetails= Report.objects.get(id=repId)  # get the details of the
    displayAllStudent = Student.objects.all().values()

    mentorId = repoDetails.mentor
    repoId = repoDetails.id
    repoStudent = repoDetails.student
    displayMentor = Mentor.objects.get(mentorId=mentorId.mentorId)
    displayStudent = Student.objects.filter(mentor=mentorId.mentorId)


    appointmentDetails = {
        'mode':'update',
        'mentorId': displayMentor,
        'studentId': displayAllStudent,
        'repo':repoId,
        'a': mentorId,
        'repoStudent': repoStudent
    }  

    return render(request,"lectReport.html",appointmentDetails)

def submitUpdateReport(request, repId):
    repoDetails= Report.objects.get(id=repId)  # get the details of the
    # updateid = Appointment.objects.get(id = appId)

    menId = request.POST['reportMentorId']
    studentId = request.POST['reportStudentId']
    datetime = request.POST['reportDate']
    category = request.POST['reportCategory']
    description = request.POST['reportDesc']


    mentorID = Mentor.objects.get(mentorId=menId)
    stuID = Student.objects.get(studentId=studentId)

    repoDetails.mentor=mentorID
    repoDetails.student=stuID
    repoDetails.date=datetime
    repoDetails.reportCategory=category
    repoDetails.reportText=description

    repoDetails.save()

    return redirect('lecturerPage',mentorId=menId)
    # return render(request,"lectReport.html",appointmentDetails)

def viewDeleteReport(request, repId, mentorId):
    repoDetails= Report.objects.get(id=repId)
    repoDetails.delete()

    return redirect('lecturerPage',mentorId=mentorId)

def searchReport(request, mentorId):
    # searchData = Student.objects.get(mentor=mentorId)
    searchName = Student.objects.filter(Q(studentName=request.GET.get('searchItem')))


    lecturer = Mentor.objects.get(mentorId=mentorId)
    report = Report.objects.all().values
    studentDetails = Student.objects.all().values
    appointment = Appointment.objects.filter(mentor=mentorId).values()

    lecturer_details = {
        'mode':'search',
        'lecturerDetails': lecturer,
        'reports': report,
        'studentDetails':studentDetails,
        'searchName': searchName,
        'appointmentDetails': appointment,
    }

    return render(request,'lecturer_page.html', lecturer_details)



# END REPORT SECTION

def displayStudent(request, mentorId):

    mentorDetails = Mentor.objects.filter(mentorId=mentorId).values()
    mentorId = Mentor.objects.filter(mentorId=mentorId).values('mentorId')

    student = Student.objects.all().values
    allMentor = Mentor.objects.all().values()
    
    
    studentDetails = {
        'studentDetails':student,
        'mentorDetails':mentorId,
        'lecturerDetails':mentorDetails,
        'allMentor': allMentor,
        'mode': 'allStudent'
    }
    return render(request,'myStudent.html',studentDetails)

def findMyMentee(request, mentorId):
    mentorDetails = Mentor.objects.filter(mentorId=mentorId).values()
    mentorId = Mentor.objects.filter(mentorId=mentorId).values('mentorId')

    allMentor = Mentor.objects.all().values()
    student = Student.objects.filter(mentor=mentorId[0]['mentorId']).values()

    menteeDetails = {
        'studentDetails':student,
        'mentorDetails':mentorId,
        'lecturerDetails':mentorDetails,
        'allMentor': allMentor,
        'mode': 'menteeOnly'        
    }
    return render(request,"myStudent.html",menteeDetails)

def makeAppointment(request, mentorId):
    displayMentor = Mentor.objects.get(mentorId=mentorId)
    displayAllStudent = Student.objects.all().values()
    displayStudent = Student.objects.filter(mentor=mentorId)

    mentorDetails = {
        'mode':"submit",
        'mentorId': displayMentor,
        'studentId': displayAllStudent,
        
        }
    
    return render(request,"myAppointment.html",mentorDetails)

def submitAppointment(request, mentorId):
    if request.method == "POST":
        menId = mentorId
        studentId = request.POST['appointmentStudentId']
        datetime = request.POST['appointmentDate']
        venue = request.POST['appointmentVenue']
        time = request.POST['appointmentTime']
        message = request.POST['appointmentMessage']
        purpose = request.POST['appointmentPurpose']

        mentorID = Mentor.objects.get(mentorId=menId)
        stuID = Student.objects.get(studentId=studentId)

        appointment = Appointment(mentor=mentorID, student=stuID, appointmentDate=datetime, venue=venue, time=time, description=message, purpose=purpose, status="Successfully")
        appointment.save()

    return redirect('lecturerPage', mentorId=mentorId)


def updateAppointment(request, appId):
    
    appDetails= Appointment.objects.get(id=appId)  # get the details of the
    displayAllStudent = Student.objects.all().values()

    mentorId = appDetails.mentor
    appId = appDetails
    displayMentor = Mentor.objects.get(mentorId=mentorId.mentorId)
    displayStudent = Student.objects.filter(mentor=mentorId.mentorId)


    appointmentDetails = {
        'mode':'update',
        'mentorId': displayMentor,
        'studentId': displayAllStudent,
        'app':appId
    }
    return render(request,"myAppointment.html",appointmentDetails)

def submitUpdateAppointment(request, appId):
    updateid = Appointment.objects.get(id = appId)
    menId = request.POST['appMentorId']
    studentId = request.POST['appStudentId']
    datetime = request.POST['appointmentDate']
    venue = request.POST['appointmentVenue']
    time = request.POST['appointmentTime']
    message = request.POST['appointmentMessage']
    purpose = request.POST['appointmentPurpose']

    updateid.appointmentDate = datetime
    updateid.venue = venue
    updateid.time = time
    updateid.description = message
    updateid.purpose = purpose
    updateid.status = "Successfully"

    updateid.save()
    return redirect('lecturerPage',mentorId=menId)

def approveApp(request, appId,mentorId):
    app = Appointment.objects.get(id=appId)
    app.status = "Successfully"
    app.save()
    return redirect('lecturerPage',mentorId=mentorId)

def rejectApp(request, appId, mentorId):
    app = Appointment.objects.get(id=appId)
    app.status = "Rejected"
    app.save()
    return redirect('lecturerPage',mentorId=mentorId)
def viewPendingApp(request, mentorId):
    lecturer = Mentor.objects.get(mentorId=mentorId)
    pendingApp=Appointment.objects.filter(mentor=mentorId).values
    mentorDetails = Mentor.objects.all().values
    pending = {
        'lecturerDetails': lecturer,
        'pendingApp':pendingApp
    }
    return render(request, "appointmentPending.html", pending)
    
def viewDeleteAppo(request,appId, mentorId):
    appoDetails= Appointment.objects.get(id=appId)
    appoDetails.delete()

    return redirect('lecturerPage',mentorId=mentorId)

def displayReport(request,adminId):
    admin = Admin.objects.get(adminId=adminId)
    reportDetails = Report.objects.all().values
    studentDetails = Student.objects.all().values
    mentorDetails = Mentor.objects.all().values

    context={
        'adminDetails':admin,
        'reportDetails': reportDetails,
        'studentDetails': studentDetails,
        'mentorDetails': mentorDetails,
        'mode':'displayReport',
    }
    return render(request, 'admin_page.html', context)

def displayApp(request,adminId):
    admin = Admin.objects.get(adminId=adminId)
    reportDetails = Report.objects.all().values
    studentDetails = Student.objects.all().values
    mentorDetails = Mentor.objects.all().values
    appointmentDetails = Appointment.objects.all().values

    context={
        'adminDetails':admin,
        'reportDetails': reportDetails,
        'studentDetails': studentDetails,
        'mentorDetails': mentorDetails,
        'appointmentDetails': appointmentDetails,
        'mode':'displayApp',
    }
    return render(request, 'admin_page.html', context)


def adminDisplayStudent(request,adminId):
    admin = Admin.objects.get(adminId=adminId)
    reportDetails = Report.objects.all().values
    studentDetails = Student.objects.all().values
    mentorDetails = Mentor.objects.all().values
    appointmentDetails = Appointment.objects.all().values

    context={
        'adminDetails':admin,
        'reportDetails': reportDetails,
        'studentDetails': studentDetails,
        'mentorDetails': mentorDetails,
        'appointmentDetails': appointmentDetails,
        'mode':'displayStudent',
    }
    return render(request, 'admin_page.html', context)

def adminDisplayMentor(request,adminId):
    admin = Admin.objects.get(adminId=adminId)
    reportDetails = Report.objects.all().values
    studentDetails = Student.objects.all().values
    mentorDetails = Mentor.objects.all().values
    appointmentDetails = Appointment.objects.all().values

    context={
        'adminDetails':admin,
        'reportDetails': reportDetails,
        'studentDetails': studentDetails,
        'mentorDetails': mentorDetails,
        'appointmentDetails': appointmentDetails,
        'mode':'displayMentor',
    }
    return render(request, 'admin_page.html', context)

def adminAddMentor(request, adminId):
    admin = Admin.objects.get(adminId=adminId)
    reportDetails = Report.objects.all().values
    studentDetails = Student.objects.all().values
    mentorDetails = Mentor.objects.all().values
    appointmentDetails = Appointment.objects.all().values

    context={
        'adminDetails':admin,
        'reportDetails': reportDetails,
        'studentDetails': studentDetails,
        'mentorDetails': mentorDetails,
        'appointmentDetails': appointmentDetails,
        'mode':'displayMentor',
    }
    return render(request, 'addMentor.html', context)

def adminAddStudent(request, adminId):
    admin = Admin.objects.get(adminId=adminId)
    reportDetails = Report.objects.all().values
    studentDetails = Student.objects.all().values
    mentorDetails = Mentor.objects.all().values
    appointmentDetails = Appointment.objects.all().values

    context={
        'adminDetails':admin,
        'reportDetails': reportDetails,
        'studentDetails': studentDetails,
        'mentorDetails': mentorDetails,
        'appointmentDetails': appointmentDetails,
        'mode':'displayMentor',
    }
    return render(request, 'addStudent.html', context)
    
from django.core.exceptions import ObjectDoesNotExist

def adminSubmitAddMentor(request, adminId):
    mentorDetails = Mentor.objects.all().values()
    admin = Admin.objects.get(adminId=adminId)
    messages = {}  # Initialize messages

    if request.method == "POST":
        mentorId = 'L' + request.POST['username']
        mentorName = request.POST['name']
        mentorPass = request.POST['password']
        mentorConfirmPass = request.POST['confirmPassword']

        if mentorPass != mentorConfirmPass:
            messages = {
                "message": "Password doesn't match!",
                'adminDetails': admin,
                'mentorDetails': mentorDetails
            }
        else:
            try:
                # Check if mentorId already exists
                existing_mentor = Mentor.objects.get(mentorId=mentorId)
                messages = {
                    "message": "Mentor ID already exists!",
                    'adminDetails': admin,
                    'mentorDetails': mentorDetails
                }
            except ObjectDoesNotExist:
                try:
                    mentor = Mentor(mentorId=mentorId, mentorName=mentorName, password=mentorPass)
                    mentor.save()
                    return redirect('adminPage', adminId=adminId)
                except:
                    messages = {
                        "message": "Error saving mentor!",
                        'adminDetails': admin
                    }

    return render(request, 'addMentor.html', messages)



def adminSubmitAddStudent(request, adminId):
    mentorDetails = Mentor.objects.all().values()
    admin = Admin.objects.get(adminId=adminId)
    if request.method == "POST":
        studentId = "ST" + request.POST['username']
        studentName = request.POST['name']
        studentMentor = request.POST['mentor']
        studentCourse = request.POST['course']
        studentPass = request.POST['password']
        studentConfirmPass = request.POST['confirmPassword']

        menId = Mentor.objects.get(mentorId=studentMentor)
        if studentPass != studentConfirmPass:
            messages = {
                "message": "Password doesn't match!",
                'adminDetails': admin,
                'mentorDetails': mentorDetails
            }
            return render(request, 'addStudent.html', messages)
        else:
            # Check if the studentId already exists
            if Student.objects.filter(studentId=studentId).exists():
                messages = {
                    "message": "Student ID already exists!",
                    'adminDetails': admin,
                    'mentorDetails': mentorDetails
                }
                return render(request, 'addStudent.html', messages)
            else:
                student = Student(studentId=studentId, studentName=studentName, course=studentCourse, mentor=menId, password=studentPass)
                student.save()
                return redirect('adminPage', adminId=adminId)

    return render(request, 'addStudent.html', {'adminDetails': admin, 'mentorDetails': mentorDetails})


def adminPage(request, adminId):
    try:
        admin = Admin.objects.get(adminId=adminId)
        studentDetails = Student.objects.all().values()

        totalmentor = Mentor.objects.all().count()
        totalstudent = Student.objects.all().count()

        admin_details = {
            'adminDetails': admin,
            'studentsDetails': studentDetails,
            'totalMentor':totalmentor,
            'totalStudent':totalstudent,

        }
        return render(request, 'admin_page.html', admin_details)
    except Admin.DoesNotExist:
        # Handle case where admin with specified ID doesn't exist
        return HttpResponse("Admin not found")

def adminDeleteStudent(request, adminId,studentId):
    deleteStudent = Student.objects.get(studentId=studentId)
    deleteStudent.delete()
    return redirect('adminDisplayMentor', adminId = adminId)

def adminDeleteMentor(request,adminId, mentorId):
    deleteMentor = Mentor.objects.get(mentorId=mentorId)
    deleteMentor.delete()
    return redirect('adminDisplayMentor', adminId = adminId)

def viewProfileStudent(request, studentId):
    student = Student.objects.get(studentId=studentId)
    mentor = Mentor.objects.filter(mentorId=student.mentor).values
    studentProfile={
        'studentDetails': student,
    }
    return render(request, 'profileStudent.html', studentProfile)

def editProfileStudent(request, studentId):
    student = Student.objects.get(studentId=studentId)
    mentor = Mentor.objects.filter(mentorId=student.mentor).values()

    studentProfile={
        'studentDetails': student,
        "mentorDetails": mentor,
    }

    return render(request, 'editProfile.html', studentProfile)

def submitEditProfileStudent(request, studentId):
    if request.method == "POST":
        studentId = studentId
        studentName = request.POST['studentName']
        studentCourse = request.POST['studentCourse']
        studentPhone = request.POST['studentPhone']
        studentAdd = request.POST['studentAdd']
        studentMentor = request.POST['studentMentor']

        menID= Mentor.objects.get(mentorId=studentMentor)
        student = Student.objects.get(studentId=studentId)
        # addStudent = Student(studentId=studentId,mentor=menID, course=studentCourse, studentName=studentName,address=studentAdd, phone=studentPhone)
        student.studentName=studentName
        student.course=studentCourse
        student.phone=studentPhone
        student.address=studentAdd
        student.save()

    return redirect('profile', studentId=studentId)

def viewStudentAppointment(request,studentId):
    try:
        student = Student.objects.get(studentId=studentId)
        mentor = Mentor.objects.all().values
        student_details ={
            "studentDetails":student,
            "lecturerDetails":mentor,
        }

        return render(request, 'studentAppointment.html', student_details)
    except Student.DoesNotExist:
        # Handle case where student with specified ID doesn't exist
        return HttpResponse("Student not found")

def submitStudentApp(request, studentId):
    if request.method == "POST":
        stuid = studentId
        mentorid = request.POST["appointmentLecturerId"]
        date = request.POST["appointmentDate"]
        venue = request.POST["appointmentVenue"]
        time = request.POST["appointmentTime"]
        purpose = request.POST["appointmentPurpose"]

        menid = Mentor.objects.get(mentorId=mentorid)
        stu_id = Student.objects.get(studentId=stuid)
        addApp = Appointment(mentor=menid,student=stu_id,appointmentDate=date,venue=venue,time=time,purpose=purpose)
        addApp.save()
    return redirect('studentPage',studentId=studentId)