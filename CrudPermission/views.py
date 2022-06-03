from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.conf import settings
from Authh .models import User
from django.contrib.auth.decorators import user_passes_test


def super(request):
    return render(request, "super/super.html")

class CreateUser(View):
    @method_decorator(login_required(login_url="login"))
    # @user_passes_test(lambda User: User.is_superuser)
    def get(self, request):
        return render(request, "super/user.html")

    def post(self, request):
        mobile = request.POST.get("mobile")
        username = request.POST.get("username")
        password = make_password(request.POST.get("password"))
       
        User.objects.create(mobile=mobile, username=username, password=password)
        messages.success(request, "User created successful")
        return redirect("dashboard")

class UpdateUser(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, "super/update_user.html", {"user": user})

    def post(self, request, id):
        mobile = request.POST.get("mobile")
        username = request.POST.get("username")
        password = make_password(request.POST.get("password"))

        User.objects.filter(id=id).update(mobile=mobile,
            username=username, password=password
            )
        return redirect("dashboard")

class DeleteUser(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, "super/delete_user.html", {"user": user})

    def post(self, request, id):
        user = User.objects.get(id=id)
        user.delete()
        return redirect("dashboard")