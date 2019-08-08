from django.urls import path
from . import views
# second part to routes
urlpatterns = [
    path('',views.home, name='home')
    # path('', views.post_list, name = 'post_list'),
    # path('post/<int:pk>', views.post_detail,name='post_detail'),
    # path('post', views.post_list, name='post_list' ),
    # path('status',views.json_res, name='status' )
]