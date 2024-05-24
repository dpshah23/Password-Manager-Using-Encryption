from django.shortcuts import render,redirect
from passwor_manager.firebase import *
from django.contrib import messages
from dotenv import load_dotenv
import os

load_dotenv()

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        
        try:
            # authemail=os.getenv('email')
            # authpassword=os.getenv('password')
            # print(authemail,authpassword)
            # user=auth.sign_in_with_email_and_password(authemail,authpassword)
            authuser=auth.sign_in_with_email_and_password(email,password)
            getname=db.child('users').child(email).get(authuser['idToken']).val()
            name=getname['name']
            request.session['name']=name
            request.session['email']=email
            request.session['logged_in']=True
            messages.success(request,f"Sign In Successful")
            return redirect("/")
        except Exception as e:
            print(e)
            messages.error(request,"User Or Password Are Incorrect")
            return render(request,"login.html")
    
    return render(request,'login.html')

def home(request):
    if 'email' not in request.session:
        return redirect('/login')
    else:
        
        return render(request,'home.html')


# Create your views here.
