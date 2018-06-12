from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate

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
    return render(request, 'accounts/login.html')
    
def register(request):
    return render(request, 'accounts/register.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")