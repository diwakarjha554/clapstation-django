from django.contrib import admin
from home.models import *

# Register your models here.

class UserDetailAdmin(admin.ModelAdmin):
    list_display = [
        'boxTitle', 'created_at',
    ]

admin.site.register(UserDetail, UserDetailAdmin);


class Advertisement_sectionAdmin(admin.ModelAdmin):
    list_display = [
        'boxTitle', 'created_at',
    ]

admin.site.register(Advertisement_section, Advertisement_sectionAdmin);


class Upcoming_events_sectionAdmin(admin.ModelAdmin):
    list_display = [
        'boxTitle', 'created_at',
    ]

admin.site.register(Upcoming_events_section, Upcoming_events_sectionAdmin);