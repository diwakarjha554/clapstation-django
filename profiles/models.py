from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="avatars/")
    email = models.EmailField(unique=True, null=True)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    budget = models.IntegerField()
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.email)

    @property
    def avatar(self):
        try:
            avatar = self.profile_picture.url
        except:
            avatar = static('img/noprofile.png')
        return avatar
    
    @property
    def name(self):
        name = f"{self.user.first_name} {self.user.last_name}"
        return name