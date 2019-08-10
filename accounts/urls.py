from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD

  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout')
=======
 path('register/', views.register, name='register'),
 path('login/', views.login, name='login'),
 path('logout/', views.logout, name='logout')
>>>>>>> 765c87c5395f7596e68579c968504d13eeab495f
]