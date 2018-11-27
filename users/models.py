from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    # enforce a user to have a one to one relationship with a profile.
    # if we delete the user delete the profile but not necessarily the inverse.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
