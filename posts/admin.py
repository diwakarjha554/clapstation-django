from django.contrib import admin
from posts.models import *

# Register your models here.

@admin.register(Post)
class AllPostAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'created_at'
    ];


@admin.register(LikedPost)
class AllPostAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'post', 'created_at'
    ];
    
@admin.register(Comment)
class AllPostAdmin(admin.ModelAdmin):
    list_display = [
        'author', 'parent_post', 'body', 'created_at'
    ];
