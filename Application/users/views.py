from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
# Create your views here.
def SignUp(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        try:
            firstName = request.POST['firstName']
            email = request.POST['email']
            password = make_password(request.POST['password'])

            user = User.objects.create(first_name=firstName, email=email, username=email, password=password)
            messages.success(request, 'account created successfully')
            return redirect(Login)
        except IntegrityError:
            messages.error(request, 'user with this email already exits')

    return render(request, 'auth/sigup.html')

def Login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'logged in')
            return redirect(SignUp)
        else:
            messages.warning(request, 'username and or password incorrect')

    return render(request, 'auth/login.html')

def Logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(SignUp)