from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.db.models import Q


def sign_out(request):
    logout(request)
    return redirect('/')

def sign_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'userauth.html',{'title':'sign-in','message':'incorrect credetial: email or password is incorrect','post':request.POST['userename']})        
    return render(request,'userauth.html',{'message':'Welcome back Dear User','title':'sign-in'})

def sign_up(request):
    if request.method=='POST':
        email=request.POST['useremail']
        password=request.POST['password']
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        
        if User.objects.filter(Q(email=email)| Q(username=username)).exists():
            return render(request,'userauth.html',{'message':'User with this username or email already exists','title':'sign-up','post':request.POST})
        else:
            user=User.objects.create_user(email=email,password=password,username=username)
            user.first_name=fname
            user.last_name=lname
            user.save()
            login(request,user)
            return redirect('/')

    return render(request,'userauth.html',{'message':'sign up to start your journey with us.','title':'sign-up'})    