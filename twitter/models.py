from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
  avatar = models.CharField(default="", max_length=140)

  def __str__(self):
    return self.avatar

class Post(models.Model):
  content = models.TextField(default="", max_length=140)
  photo_url = models.CharField(default= "", max_length=250)
  date = models.DateTimeField(default=timezone.now())
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='posts')
  def __str__(self):
    return f"{self.content}-{self.photo_url}"

class Comment(models.Model):
  message = models.TextField(default="", max_length=140)
  post = models.ForeignKey(Post, default="", on_delete=models.CASCADE, related_name='comments_post')
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='comments_user')
  date = models.DateTimeField(default=timezone.now())

  def __str__(self):
    return f"{self.user}-{self.message}"


