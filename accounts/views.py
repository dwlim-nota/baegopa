from django.shortcuts import render, redirect, HttpResponse
from .models import Member
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

# Create your views here.
def register(req):
    if req.method == "POST":
        user_id = req.POST["id"]
        user_name = req.POST["name"]
        user_pw = req.POST["password"]
        bank_name = req.POST["bank_name"]
        bank_account_number = req.POST["bank_account_number"]
        new_user = Member.objects.create_user(
            user_id=user_id,
            name=user_name,
            password=user_pw,
            bank_name=bank_name,
            bank_account_number=bank_account_number
        )
        auth_login(req, user=new_user)
        return redirect("order:order")
    else:
        return render(req, "accounts/register.html")

def login(req):
    if req.method == "POST":
        user_id = req.POST["id"]
        user_pw = req.POST["password"]
        user = authenticate(user_id=user_id, password=user_pw)
        if user != None:
            auth_login(req, user=user)
            return redirect("order:order")
        else:
            return HttpResponse('login failed! try again.')
    else:
        print(req.user)
        return render(req, "accounts/login.html")

def logout(req):
    auth_logout(req)
    return redirect("order:order")

def info(req):
    return render(req, "accounts/info.html")

def update(req):
    return render(req, "accounts/info.html")