from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')


class Project(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    live_link = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
