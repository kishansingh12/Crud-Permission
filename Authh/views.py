from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.core.mail import send_mail

## Login & logout & register
def login_user(request):
    if request.method == "POST":
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        user = authenticate(mobile=mobile, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User login Successfully")
            return redirect("super")
        else:
            return render(request, "auth/login.html", {"message": "Invalid Credentials"})

    return render(request, "auth/login.html")

def logoutUser(request):
    logout(request)
    messages.success(request, "User logout")
    return redirect('dashboard')

def registerUser(request):
    print("User", request.user)
    if request.method == "POST":
        print("RES", request.POST)
        try:
            mob = User.objects.get(mobile=request.POST['mobile'])
            context = {
                'mob':mob,
            }
            return render(request, 'signup.html', context)
        except User.DoesNotExist:    
            mob = User.objects.create(mobile=request.POST['mobile'],username=request.POST['username'] ,password=make_password(request.POST['password']))
            login(request, mob)
            mob.save()
            return redirect('dashboard')
    else:
        messages.success(request, 'An error has come during registration. please check Mobile & password') 
    return render(request, 'auth/signup.html') 


## Homepage
def dashboard(request):
    return render(request, "auth/dashboard.html")



## smtp email simple 
# send_mail(
#     'Subject here',
#     'message.',
#     'kishantestcode@gmail.com',
#     ['kishantestcode@gmail.com'],
#     fail_silently=False,
# )    