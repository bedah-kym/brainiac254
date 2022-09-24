
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as vw

app_name='USERS'
urlpatterns = [
    path('register/',views.register,name="user-register"),
    path('login/',vw.LoginView.as_view(template_name='USERS/login.html'),name='login'),
    path('logout/',vw.LogoutView.as_view(template_name='polls/index.html'),name='logout'),

]
