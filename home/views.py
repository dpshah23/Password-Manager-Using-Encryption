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
            authemail=os.getenv('email')
            authpassword=os.getenv('password')
            # print(authemail,authpassword)
            user=auth.sign_in_with_email_and_password(authemail,authpassword)
            authuser=auth.sign_in_with_email_and_password(email,password)
            getname=db.child('users').get().val()
            for user_id, user_data in getname.items():
                if user_data['email']==email:
                    name=user_data['name']
                    break
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

def signup(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        print(email,password,name)
        authemail=os.getenv('email')
        authpassword=os.getenv('password')
        print(authemail,authpassword)
        try:
            auth.create_user_with_email_and_password(email,password)
            user=auth.sign_in_with_email_and_password(authemail,authpassword)
            print(user)
            
            data={
                'name':name,
                'email':email,
                'mobile':mobile,
                'password':password

            }
            db.child('users').push(data)
            messages.success(request,f"Account Created Successfully")
            return redirect("/login")
        except Exception as e:
            print(e)
            messages.error(request,"Email Already Exist")
            return render(request,'signup.html')
    return render(request,'signup.html')
# Create your views here.

def addnewpassword(request):
    if 'email' not in request.session:
        return redirect('/login')
    if request.method=="POST":
        name=request.POST.get('name')
        emailused=request.POST.get('email')
        password=request.POST.get('password')
        data={
            'email':request.session['email'], 
            'name':name,
            'emailused':emailused,
            'password':password
        }
        db.child('passwords').push(data)
        messages.success(request,"Password Added Successfully")
        return redirect('/')
    return render(request,'addnewpassword.html')

def logout(request):

    request.session.flush()
    return redirect('/login')

def error_404(request,exception):
    return render(request,'404.html')
