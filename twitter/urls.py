from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('status', views.json_res, name='status')
]