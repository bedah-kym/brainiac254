from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            username= reg_form.cleaned_data.get('username')
            reg_form.save()
            return redirect('polls:home')
            messages.success(request,"Account created, you can now log in")
    else:
        reg_form = UserCreationForm()
    return render(request,'USERS/register.html',{"form":reg_form})


def login(request):
    pass
