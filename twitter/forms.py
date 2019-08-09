from django import forms
from .models import Post, Comment, Profile

class ProfileForm(forms.ModelForm):
  
  class Meta:
    model = Profile
    fields = ('avatar',)

class PostForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = ('content', 'photo_url', 'date', 'user')

class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('message', 'post', 'user', 'date')

