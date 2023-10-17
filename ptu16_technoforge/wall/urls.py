from django.urls import path
from . import views

urlpatterns = [
    path('wall/post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('wall/create_post/', views.create_post, name='create_post'),
    path('wall/create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('wall/post_list.html', views.PostListView.as_view(), name='post_list'),
]