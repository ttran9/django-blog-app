from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add means you can never modify the date_posted field.
    date_posted = models.DateTimeField(default=timezone.now())
    # if a user is deleted then delete the post.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

