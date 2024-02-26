from django.contrib import admin
from .models import Lecturer,Student,Report, Message

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Report)
admin.site.register(Message)
