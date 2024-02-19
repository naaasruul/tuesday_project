from django.urls import path
from . import views

urlpatterns = [
 path('login_users',views.login_user, name="login")
]