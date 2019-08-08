from django.db import models

# Create your models here.
class Profile(models.Model):
  avatar = photo_url = models.TextField()

  def __str__(self):
    return self.avatar
    
class Post(models.Model):
  content = models.CharField(max_length=160)
  photo_url = models.TextField()
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

  def __str__(self):
    return f"{self.content}-{self.photo_url}"

class Comment(models.Model):
  message = models.CharField(max_length=160)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  date = models.DateTimeField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return f"{self.title}-{self.artist}"


