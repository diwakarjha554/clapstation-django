from django.urls import path
from authentication.views import *

urlpatterns = [
    path('signup', signupPage, name="signup"),
    path('login', loginPage, name="login"),
    path('logout', logOut, name='logOut'),
]
