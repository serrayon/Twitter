from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
<<<<<<< HEAD

# Create your views here.

def home(request):
  return HttpResponse("You are home")

def json_res(request):
  return JsonResponse({ "status": "OK"})
=======
# Create your views here.
from .models import Post, Comment

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
>>>>>>> eea53fbca0adc26fc6e331a58c585bff83e1aafd
