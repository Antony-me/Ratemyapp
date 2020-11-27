from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar =CloudinaryField('image', default="media/avater.png", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')


class Project(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image',validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    live_link = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
