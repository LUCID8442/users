
# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        User.objects.create(username=username, email=email, password=hashed_password)
        return redirect('login')
    return render(request, 'start/register.html')

def login(request):
    # Handle login logic here
    return render(request, 'start/login.html')
