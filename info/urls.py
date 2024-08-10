from django.urls import path
from info.views import *

urlpatterns = [
    path('about', aboutus, name="aboutus"),
    path('contact', contactus, name="contactus"),
]
