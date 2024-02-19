from django.shortcuts import render
from hobby.models import Mentor  # Import the Student model
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def index(request):
    displayData = Mentor.objects.all().values()
    context = {"displayData": displayData, "message": "data has been saved"}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def newMentor(request):
    displayData = Mentor.objects.all().values()
    if request.method == "POST":
        mentorId1 = request.POST["mentorId"]
        mentorName1 = request.POST["mentorName"]
        mentorRoom1 = request.POST["mentorRoom"]

        data = Mentor(mentorId=mentorId1, mentorName=mentorName1, roomNo=mentorRoom1)
        data.save()

        context = {"displayData": displayData, "message": "data has been saved"}
    
        return render(request, "new-mentor.html", context)
    else:
        dict = {
            "message": " ",
            "displayData": displayData,
        }
        return render(request, "new-mentor.html", dict)

def newStudent(request):
    displayData = Student.objects.all().values()
    if request.method == "POST":
        mentorId1 = request.POST["mentorId"]
        mentorName1 = request.POST["mentorName"]
        mentorRoom1 = request.POST["mentorRoom"]

        data = Student(mentorId=mentorId1, mentorName=mentorName1, roomNo=mentorRoom1)
        data.save()

        context = {"displayData": displayData, "message": "data has been saved"}
    
        return render(request, "new-mentor.html", context)  # Use a different template for new students
    else:
        dict = {
            "message": " ",
            "displayData": displayData,
        }
        return render(request, "new-mentor.html", dict)  # Use a different template for new students

def update(request,mentorId):
    updateid = Mentor.objects.get(mentorId = mentorId)

    dict={
        'updateid':updateid,
        "nama":"nasrul"
    }
    return render(request,"update.html",dict)

def updateData(request, mentorId):
    updateid = Mentor.objects.get(mentorId = mentorId)
    mentorName = request.POST['mentorName']
    mentorRoom = request.POST['roomNo']
    updateid.mentorName = mentorName
    updateid.roomNo = mentorRoom
    updateid.save()

    dict={
        'updateid':updateid
    }

    return HttpResponseRedirect(reverse("index"))

def viewDelete(request, mentorId):
    datatobedelete = Mentor.objects.get(mentorId=mentorId)
    dict = {
        'datatobedelete':datatobedelete
    }

    return render(request,"delete.html",dict)

def delete(request, mentorId):
    deleteMentor = Mentor.objects.get(mentorId=mentorId)
    deleteMentor.delete()

    return HttpResponseRedirect(reverse("index"))

def searchpage(request):
    search = Mentor.objects.filter(Q(mentorId=request.GET.get('product_name')))
    dict = {
        'findMentor':search
    }


    return render(request,'index.html',dict)