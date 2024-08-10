from django.db import models

# Create your models here.
class UserDetail(models.Model):
    boxTitle = models.CharField(max_length=50)
    boxImage = models.ImageField(null=True, blank=True, upload_to='adminImages/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.boxTitle
    
class Advertisement_section(models.Model):
    boxTitle = models.CharField(max_length=50)
    boxImage = models.ImageField(null=True, blank=True, upload_to='adminImages/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.boxTitle
    
class Upcoming_events_section(models.Model):
    boxTitle = models.CharField(max_length=50)
    boxImage = models.ImageField(null=True, blank=True, upload_to='adminImages/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.boxTitle
    
