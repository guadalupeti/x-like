
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Post(models.Model):
    text = models.TextField(max_length = 240)
    image = models.ImageField(null=True, blank=True, default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='Unknown')
    creation_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(null=True, blank=True, default='profile_pics/egg.jpg', upload_to = 'profile_pics/')

    def __str__(self):
        return self.username
    
class Hashtag(models.Model):
    name = models.CharField(max_length=240, unique = True)
    posts = models.ManyToManyField(Post, related_name = 'hashtags')