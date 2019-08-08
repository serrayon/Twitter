from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
  return HttpResponse("You are home")

def json_res(request):
  return JsonResponse({ "status": "OK"})