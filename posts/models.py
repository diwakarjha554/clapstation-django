import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()


# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    postContent = models.CharField(max_length=500, blank=True)
    postImage = models.FileField(null=True, blank=True, upload_to='images/')
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user} : {self.postContent}"
    
    class Meta:
        ordering = ['-created_at']
    

class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.email} : {self.post.postContent}'
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        try:
            return f"{self.author.email} : {self.body[:30]}"
        except:
            return f"no author : {self.body[:30]}"