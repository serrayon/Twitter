from django.urls import path
from . import views
# second part to routes
urlpatterns = [
    path('',views.home, name='home'),
    path('', views.post_list, name = 'post_list'),
    path('posts/<int:pk>', views.post_detail,name='post_detail'),
    path('comments', views.comment_list, name='comment_list' ),
    path('status',views.json_res, name='status' )
       
]


    
    