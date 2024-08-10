from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from home.models import *
from posts.models import *
from posts.forms import CreatePostForm
from django.shortcuts import get_object_or_404


# Create your views here.
def homePage(request):

    # Fetching the Home Page Data from models
    try:
        userDetail = UserDetail.objects.latest("created_at");
        advertisement_section = Advertisement_section.objects.latest("created_at");
        upcoming_events_section = Upcoming_events_section.objects.latest("created_at");

    except ObjectDoesNotExist:
        userDetail = None
        advertisement_section = None
        upcoming_events_section = None


    # Upload Post Form
    uploadPostForm = CreatePostForm(request.POST);  



    # Set up pagination
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)



    # Fetching LoggedIn UserName
    loggedInUser = request.user


    # Sending the Context Name Dictionary
    context = {
        'titles':'Home - Clap Station',
        'userDetail':userDetail,
        'advertisement_section':advertisement_section,
        'upcoming_events_section':upcoming_events_section,
        'uploadPostForm':uploadPostForm,
        'page_obj':page_object,
        'loggedInUser':loggedInUser,
       
    }

  

    return render(request, 'index.html', context=context)

