from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.db import transaction  # Import transaction module
from .models import User
def login(request):
    # Handle login logic here
    return render(request, 'start/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Hash the password using Django's make_password function
        hashed_password = make_password(password)
        
        # Wrap database operations in a transaction
        with transaction.atomic():
            try:
                # Create a new User object and save it to the database
                user = User.objects.create(username=username, email=email, password=hashed_password)
                
                # Perform additional operations if needed
                # For example, you might want to create related objects or perform other tasks within the same transaction
                
            except Exception as e:
                # Handle any exceptions that may occur during database operations
                # For example, you might want to log the error or display a user-friendly error message
                return render(request, 'start/error_template.html', {'error_message': str(e)})
        
        # Redirect the user to the login page after successful registration
        return redirect('login')
    
    # Render the registration form template for GET requests
    return render(request, 'start/register.html')
