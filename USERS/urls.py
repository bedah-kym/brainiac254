
from django.contrib import admin
from django.urls import path
from . import views

app_name='USERS'
urlpatterns = [
    path('register/',views.register,name="user-register"),
    path('login/',views.login,name="user-login")

]
