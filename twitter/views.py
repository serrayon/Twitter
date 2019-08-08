from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Post, Comment

def home(request):
    return HttpResponse("You are home")

def json_res(request):
    return JsonResponse({ "status" : "Ok" })


def post_list(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', {"post": post})

def post_detail(request):
    post = Comment.objects.all()
    return render(request, 'comment_list.html', {"post": post})