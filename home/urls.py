from django.urls import path
from home.views import *

urlpatterns = [
    path('', homePage, name='homepage'),
]
