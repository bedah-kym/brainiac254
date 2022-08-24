from django.contrib import admin
from django.urls import path
from . import views

app_name='polls'

urlpatterns = [
    path('home/',views.homeview.as_view(),name="home"),
    path('result/<int:pk>/',views.result.as_view(),name="result"),
    path('create/',views.newchoice.as_view(),name="create"),
    path('delete/<int:pk>/',views.deletenewpoll.as_view(),name="delete"),
    path('details/<int:pk>/',views.details.as_view(),name="detail"),
    path('vote/<int:question_id>/',views.vote,name="vote"),
]
