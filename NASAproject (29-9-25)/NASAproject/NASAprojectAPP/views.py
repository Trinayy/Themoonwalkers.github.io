from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

def aim(request):
    return render(request, "aim.html")

def meet(request):
    return render(request, "meet.html")

def contactus(request):
    return render(request, "contactus.html")

def aboutmoon(request):
    return render(request, "aboutmoon.html")

def factsaboutsolarsystem(request):
    return render(request, "factsaboutsolarsystem.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup")
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")
        if len(password1) < 6:
            messages.error(request, "Password must be at least 6 characters long")
            return redirect("signup")

        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "sign_up.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login1.html")


def logout_view(request):
    logout(request)
    return redirect("home")



def contactus_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        
        if not name or not email or not message:
            messages.error(request, "All fields are required.")
            return redirect("contactus")

        
        User.objects.create(
            username=name,
            email=email,
            first_name=message  
        )

        messages.success(request, "Your details have been saved. Thank you for contacting us!")
        return redirect("contactus")

    return render(request, "contactus.html")
