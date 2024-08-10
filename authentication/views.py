from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authentication.models import *
from datetime import datetime


# Create your views here.
def loginPage(request):

    context = {
        'titles': 'Login | Clap Station',
    }

    if not request.user.is_authenticated:

        if request.method == 'POST':
            email = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
        
            if user is not None:
                login(request,user)
                return redirect('homepage')
        
            else:
                messages.success(request, ("There was an error Logging In, Try Again..."))
                return redirect('login')
        
        else:
            return render(request, 'login.html', context=context)
    
    else:
        return redirect('homepage')


def signupPage(request):

    context = {
        'titles': 'Signup | Clap Station',
    }

    if not request.user.is_authenticated:

        if request.method=="POST":
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            day = request.POST.get("birthday_day")
            month = request.POST.get("birthday_month")
            year = request.POST.get("birthday_year")
            date_string = f"{year}-{month}-{day}"
            dob = datetime.strptime(date_string, "%Y-%m-%d")
            gender=request.POST.get('gender')
            designation=request.POST.get('designation')
            password = request.POST.get('password')
            user=CustomUser.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,date_of_birth=dob,gender=gender,designation=designation)
            user.save()
            messages.success(request,'Acoount has been created successfully')
            return redirect('login')
        return render(request,"signup.html", context)
    
    else:
        return redirect('homepage')
    


def logOut(request):
    logout(request)
    return redirect('homepage')

