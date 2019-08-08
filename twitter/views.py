from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Comment
# from .forms import PostForm
# Create your views here.

def home(request):
    return HttpResponse("You are home")

def json_res(request):
    return JsonResponse({ "status" : "Ok" })

def post_list(request):
    post = Post.objects.all()
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
    return render(request, 'post_form.html', {'form': form,'header': 'New Post'})