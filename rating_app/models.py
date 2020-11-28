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
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()

    def update_bio(self,new_bio):
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id = user_id)
        self.avatar = new_image 
        self.save()              
    


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image', validators=[
                            FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    live_link = models.URLField()
    description = models.TextField(blank=True)
    developer = models.ForeignKey('Profile', on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title[:90])


Rating_CHOICES = (

    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10,10),   
)
 

class Rating(models.Model):
    design_vote = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    ux_vote = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    content_vote = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    review = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()