from django.contrib import admin
from profiles.models import *

# Register your models here.
@admin.register(Profile)
class AllPostAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'profile_picture' ,'category', 'sub_category','location','budget', 'created_at'
    ];