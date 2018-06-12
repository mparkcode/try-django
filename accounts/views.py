from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            auth.login(request, user)
            return redirect("/")
        return HttpResponse("That user or password is wrong Dumbass")
    login_form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':login_form})
    
def register(request):
    registration_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':registration_form})
    
def logout(request):
    auth.logout(request)
    return redirect("/")