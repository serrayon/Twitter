from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
  path('', views.home, name='home'),
  path('status', views.json_res, name='status')
]
=======
# second part to routes
urlpatterns = [
    path('',views.home, name='home'),
    path('', views.post_list, name = 'post_list'),
    path('posts/<int:pk>', views.post_detail,name='post_detail'),
    path('comments', views.comment_list, name='comment_list' ),
    path('status',views.json_res, name='status' )
       
]


    
    
>>>>>>> eea53fbca0adc26fc6e331a58c585bff83e1aafd
