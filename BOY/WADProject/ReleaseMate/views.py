from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request, "login.html")

def about(request):
    return render(request, "about.html")

def masuk(request):
    return render(request, "masuk.html")

def masuk(request):
    displaydata = Student.objects.all().values()
    if request.method == 'POST':
        # Assuming the form fields are named 'student_id', 'student_name', and 'course'
        Student_ID = request.POST.get('StudentID')
        Student_Name = request.POST.get('StudentName')
        Course = request.POST.get('course')
        new_student = Student(StudentId=Student_ID, StudentName=Student_Name, course=Course)
        # new_student.save()

        context = {
            'displaydata':displaydata,
            'message':'DATA SAVE !',
        }

        return render(request, "masuk.html", context)
    else:
        # If the request method is not POST, render the form page
        return render(request, 'masuk.html')