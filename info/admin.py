from django.contrib import admin
from info.models import *

# Register your models here.
@admin.register(ContactUs)
class AllPostAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'email' ,'phone', 'msg', 'created_at',
    ];