from django.urls import path
from . import views
urlpatterns =[
    path("index.html", views.index , name="index"),
    path("about.html", views.home , name="about")
    ]

    # ni untuk routing