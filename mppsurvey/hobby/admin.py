from django.contrib import admin
from .models import Mentor,Student,Report,Appoinment

# Register your models here.
admin.site.register(Mentor,Student,Report,Appoinment)

