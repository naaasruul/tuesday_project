from django.contrib import admin
from .models import Student
from .models import Mentor
from .models import TopManagement

# Register your models here.
admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(TopManagement)
