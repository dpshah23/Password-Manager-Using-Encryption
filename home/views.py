from django.shortcuts import render
from passwor_manager.firebase import db

def login(request):
    return render(request,'login.html')


# Create your views here.
