from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
  avatar = models.TextField()
<<<<<<< HEAD
  def __str__(self):
    return self.avatar


=======

  def __str__(self):
    return self.avatar

>>>>>>> eea53fbca0adc26fc6e331a58c585bff83e1aafd
class Post(models.Model):
  content = models.CharField(default= "", max_length=160)
  photo_url = models.TextField(default="")
  date = models.DateTimeField(default=timezone.now())
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='posts')
<<<<<<< HEAD
=======

>>>>>>> eea53fbca0adc26fc6e331a58c585bff83e1aafd
  def __str__(self):
    return f"{self.content}-{self.photo_url}"

class Comment(models.Model):
  message = models.CharField(default="", max_length=160)
  post = models.ForeignKey(Post, default="", on_delete=models.CASCADE, related_name='comments_post')
  user = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='comments_user')
  date = models.DateTimeField(default=timezone.now())
<<<<<<< HEAD
  def __str__(self):
    return f"{self.title}-{self.artist}"
 
 
=======

  def __str__(self):
    return f"{self.title}-{self.artist}"


>>>>>>> eea53fbca0adc26fc6e331a58c585bff83e1aafd
