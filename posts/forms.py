from django import forms
from django.forms import ModelForm
from posts.models import Post

class CreatePostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = [
            'postContent',
            'postImage'
        ]
        required = ("")
        widgets = {
            
            'postContent': forms.Textarea(attrs={
                "placeholder":"Share your content.....",
            }),

            'postImage': forms.FileInput(attrs={
                "class":"home-img-upload",
                "id":"img-input",
            })

        }