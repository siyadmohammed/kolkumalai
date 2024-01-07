from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *  #to link the class file in models.py with views.py


# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def registernew(request):
    return render(request,'registernew.html')
def adminlogin(request):
    return render(request,'adminlogin.html')
def adminlogincheck(request):
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/admin_homepage/")
            else:
                return redirect("/loginform/")
def adminhomepage(request):
    return render(request,'adminhomepage.html')

def savedbookings(request):
    if request.method=="POST":
        a = slotbooking()
        a.CHECK_IN_DATE = request.POST.get("indate")
        a.CHECK_OUT_DATE = request.POST.get("outdate")
        a.NUMBER_OF_PERSON = request.POST.get("count")
        a.STATUS = "Pending"
        a.save()
        return redirect("/")
def checkavailability(request):
    data={}
    c=request.GET.get("b")
    if slotbooking.objects.filter(CHECK_IN_DATE=c).exists():
        data["message"]="error"
        return JsonResponse(data)
    else:
        data["message"]="success"
        return JsonResponse(data)
def viewbooking(request):
    g = slotbooking.objects.all()
    return render(request, "viewbookings.html", {'g': g})
def savedguestmessage(request):
    if request.method=="POST":
        c = guestmessage()
        c.Name = request.POST.get("cname")
        c.Email = request.POST.get("cemail")
        c.Message = request.POST.get("cmessage")
        c.save()
        return redirect("/")
def viewguestmessage(request):
    f = guestmessage.objects.all()
    return render(request,"viewguestenquiry.html",{'f':f})