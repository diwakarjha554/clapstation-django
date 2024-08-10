from django.urls import path
from posts.views import *

urlpatterns = [
    path('', create_post, name="post-create"),
    path('delete/<pk>', delete_post, name="post-delete"),
    path('<pk>/like', like_post, name="post-like"),
]
