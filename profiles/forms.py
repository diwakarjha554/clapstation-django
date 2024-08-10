from .models import *
from django.forms import ModelForm

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            ''
        }
