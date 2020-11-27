from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    avatar = CloudinaryField('image', default="media/avater.png", validators=[
                             FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    bio = models.TextField(max_length=500, blank=True,
                           default=f'Hello, I am new here!')

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Project(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image', validators=[
                            FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    live_link = models.URLField()
    description = models.TextField(blank=True)
    developer = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title[:90])


Rating_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
)
class Rating(models.Model):
    design = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    user_expirience = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    content = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project)
