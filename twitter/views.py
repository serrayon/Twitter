from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
  return HttpResponse("You are home")

def json_res(request):
  return JsonResponse({ "status" : "Ok" })

def welcome_page(request):
  return render(request, 'welcome_page.html')

def about(request):
  return render(request, 'about.html')

def post_list(request):
  posts = Post.objects.all()
  post = posts.first()
  form = PostForm()
  # comments = Comment.objects.filter(post=post.pk)
  # print(post.comments_post.all().first().message)
  # print(comments)
  return render(request, 'post_list.html', {"posts": posts, "form": form})
    

def comment_list(request):
  comments = Comment.objects.all()
  return render(request, 'comment_list.html', {"comments": comments})

def post_detail(request, pk):
  post = Post.objects.get(id=pk)
  comments = Comment.objects.filter(post=post)
  print(comments)
  return render(request, 'post_detail.html', {"post":post, "comments": comments})


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
  return render(request, 'post_list.html', {'form': form, 'header': f'New Post'})

# def profile(request, pk):
#   if request.method == 'POST':
#     form = ProfileForm(request.POST)
#     if form.is_valid():
#       profile = form.save(commit=False)
#       profile.user = request.user
#       profile.save()
#       return redirect('post_detail', pk=profile.pk)
#   else:
#     form = ProfileForm()
#   return render(request, 'profile.html', {'form': form, 'header': f'Profile Picture'})


def post_edit(request, pk):
  post = Post.objects.get(id=pk)
  if request.method == 'POST':
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

# def search(request):        
#     if request.method == 'POST':      
#         post_detail =  request.POST.getlist('search')      
#         try:
#             status = Add_prod.objects.filter(comment__icontains=comment)
#             #Add_prod class contains a column called 'bookname'
#         except Add_prod.DoesNotExist:
#             status = None
#         return render(request,"search.html",{"posts":status})
#     else:
#         return render(request,"search.html",{})
