from django.urls import path
from profiles.views import *

urlpatterns = [
    # path('profile/<str:email>', user_profile, name='user-profile'),
    path('profile', user_profile, name='user_profile')
]