from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def adminLogin(request):
    return render(request,"admin_template/signin.html")

def AdminLoginProcess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in Login! Please Enter the valid Username and Password")
        return HttpResponseRedirect(reverse("admin_login"))

def AdminLogoutProcess(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return HttpResponseRedirect(reverse("admin_login")) 

    

