from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=uname, password= password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Wrong Credentials!?')
            return redirect('login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('register')
            else :
                user=User.objects.create_user(username=uname,first_name=fname, last_name=lname, email=email, password=pass1)
                user.save()
                print('user is created!')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('login')
        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')