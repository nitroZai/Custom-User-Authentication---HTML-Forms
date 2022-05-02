from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Student

# Create your views here.


def home(request):
    return render(request, 'home.html')

def loginn(request):
    if request.method == "POST":
        name = request.POST.get('name')
        x = request.POST.get('x')
        y = request.POST.get('y')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        student = Student()

        if password1 != password2:
            return HttpResponse("<h2> Wrong Password </h2>")
        else:
            student.name = name
            student.active = True
            student.x = x
            student.y = y
            student.set_password(password1)
            student.save()

    return render(request, 'login.html')


def loggedin(request):

    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        student = authenticate(name = name, password = password)

        if student:
            print(student)
            login(request, student)
            return render(request, 'logoutt.html')
        else:
            return HttpResponse('Failed')


def goingback(request):

    logout(request)

    return redirect('home')