from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileForm

def home(request):
    return HttpResponse("You are home")

def json_res(request):
    return JsonResponse({ "status" : "Ok" })

def post_list(request):
    posts = Post.objects.all()
    post = posts.first()
    # comments = Comment.objects.filter(post=post.pk)
    # print(post.comments_post.all().first().message)
    # print(comments)
    return render(request, 'post_list.html', {"posts": posts})
    

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {"comments": comments})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {"post":post})


def post_create(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'post_form.html', {'form': form, 'header': f'New Post'})

def post_edit(request, pk):
  post = Post.objects.get(id=pk)
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'post_form.html', {'form': form, 'header':f'Edit {post.content}'})

def post_delete(request, pk):
  Post.objects.get(id=pk).delete()
  return redirect('post_list')

def comment_create(request, pk):
  post = Post.objects.get(id=pk)
  if request.method =='POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post_detail', pk=comment.post.pk)
  else:
    form = CommentForm()
  return render(request, 'post_form.html', {'form': form, 'header':f'Add comment for {post.user}'})

  def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    return render(request, 'profile.html', {'posts': posts})