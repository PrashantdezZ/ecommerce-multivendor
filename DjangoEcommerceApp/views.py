from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demoPage(request):
    return HttpResponse("demo page")

def adminLogin(request):
    return render(request,"admin_template/signin.html")
