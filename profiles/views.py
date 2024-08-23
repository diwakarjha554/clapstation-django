from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from posts.models import *
from home.models import *
from profiles.models import *
from .forms import *


from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def user_profile(request):
    
    profile = request.user.profile

    form = ProfileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    
    context = {
        'profile': profile,
        'form': form,
    }
    
    return render(request, 'profile.html', context=context)




def user_prof(request,email):
    
    profile = User.objects.get(email=email)

    form = ProfileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    
    context = {
        'profile': profile,
        'form': form,
    }
    
    return render(request, 'profile.html', context=context)




# def user_profile(request,email):
    
#     if request.user.is_authenticated:
        
#         try:
#             profile = Profile.objects.get(user=User.objects.get(email=email))
#         except ObjectDoesNotExist:
#             profile = None
#         use=User.objects.get(email=email)
#         obj = Post.objects.filter(user=User.objects.get(email=email)).order_by('-id')
#         try:
#             add = Advertisement_section.objects.latest('created_at')
#         except ObjectDoesNotExist:
#             add = None
            
        
#         context = {
#             'obj':obj,
#             'add':add,
#             'profile':profile,
#             'user':use
#         }

    
#         return render(request, 'profile.html', context=context)
    
#     else:
#         return redirect('login')