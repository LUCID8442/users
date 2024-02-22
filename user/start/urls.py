# myproject/urls.py
from django.urls import path
from start.views import register, login

urlpatterns = [
    path('register/', register, name='register'),
    path('', login, name='login'),
]
