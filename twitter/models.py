from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
  avatar = models.CharField(default="", max_length=160)

  def __str__(self):
    return self.avatar

class Post(models.Model):
  content = models.CharField(default= "", max_length=160)
  photo_url = models.TextField(default="")
  date = models.DateTimeField(default=timezone.now())
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='posts')

  def __str__(self):
    return f"{self.content}-{self.photo_url}"

class Comment(models.Model):
  message = models.CharField(default="", max_length=160)
  post = models.ForeignKey(Post, default="", on_delete=models.CASCADE, related_name='comments_post')
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='comments_user')
  date = models.DateTimeField(default=timezone.now())

  def __str__(self):
    return f"{self.title}-{self.artist}"


