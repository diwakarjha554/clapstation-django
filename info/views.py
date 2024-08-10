from django.shortcuts import render, redirect
from django.contrib import messages
from info.models import *

# Create your views here.
def aboutus(request):
    if request.user.is_authenticated:
        return render(request,'about-us.html')
    else:
        return redirect('login')
    
def contactus(request):
    if request.user.is_authenticated:
       if request.method == "POST":

            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            msg = request.POST.get("msg")

            modelContact = ContactUs(name = name, email = email, phone = phone, msg = msg)
            modelContact.save()
            messages.success(request, ("Message sent successfully"))

            return redirect('contactus');
    
    return render(request,"contact-us.html")