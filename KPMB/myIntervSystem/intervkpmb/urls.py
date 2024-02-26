from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("mainpage/<str:lectID>", views.mainpage, name="mainpage"),
    path("mainpage/mystudent/<str:lectID>", views.mystudent, name="mystudent"),
    path("mainpage/mystudent/<str:lectID>/addStudent", views.viewAddStudent, name="addStudent"),
    path("mainpage/mystudent/<str:lectID>/addStudent/add", views.submitAddStudent, name="submitAddStudent"),
    
    path("mainpage/addreport/<str:lectID>/view", views.viewReport, name="reportpage"),
    path("mainpage/addreport/<str:lectID>/submit", views.submitReport, name="submitReport"),
]   