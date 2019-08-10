from django.urls import path
from . import views
# second part to routes

urlpatterns = [
    # path('',views.home, name='home'),
    # path('',views.welcome_page, name='welcome_page'),
    path('',views.post_list, name='post_list'),
    path('posts/', views.post_list, name = 'post_list'),
    path('posts/<int:pk>', views.post_detail,name='post_detail'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:pk>/comments/new', views.comment_create, name='comment_create'),
    path('comments', views.comment_list, name='comment_list' ),
    path('status',views.json_res, name='status' ),
    path('profile/', views.profile, name='profile')   
]

