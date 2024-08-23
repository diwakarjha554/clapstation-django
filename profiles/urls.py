from django.urls import path
from profiles.views import *

urlpatterns = [
    # path('profile/<str:email>', user_prof, name='user_profile'),
    path('profile', user_profile, name='user_profile')
]