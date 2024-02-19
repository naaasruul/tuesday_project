from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("newMentor", views.newMentor, name="newMentor"),
    path("update/<str:mentorId>", views.update, name="update"),
    path("update/updatedata/<str:mentorId>", views.updateData, name="update"),
    path("viewdelete/<str:mentorId>", views.viewDelete, name="viewdelete"),
    path("viewdelete/deletedata/<str:mentorId>", views.delete, name="delete"),
    path("searchpage", views.searchpage, name="searchpage"),
]