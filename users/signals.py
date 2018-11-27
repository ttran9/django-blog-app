from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# user is the sender because it is sending the signal
# a receiver is a function which gets the signal and then performs a task.

# we take in a signal into the decorator and a sender.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
        For this method when a user is created then send in the post_save signal into the function below
        which acts as a receiver and the function takes in the arguments from our post_save signal where
        one of the arguments is the instance of the user and created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
        saves the profile whenever the user is saved.
    """
    instance.profile.save()
