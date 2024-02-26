from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("masuk", views.masuk, name="masuk"),  # This is fine
    path("mentor", views.masuk, name="mentor"),  # Rename this to a different view
]
