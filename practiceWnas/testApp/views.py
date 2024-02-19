from django.shortcuts import render
from testApp.models import Student

# Create your views here.
def index(request):
    a = Student.objects.all().values()

    if request.method == "POST":
        stuId = request.POST["idstu"]
        stuName = request.POST["namestu"]
        stuAge = request.POST["agestu"]
        stuGender = request.POST["genderstu"]

        data = Student(stuId=stuId, name=stuName,age=stuAge, gender=stuGender)
        data.save()

    stuObject = {
        'students':a
    }
    return render(request,"index.html", stuObject)

