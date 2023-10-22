from django.urls import path
from . import views

urlpatterns = [
    path('post_detail/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_comment/<int:post_pk>/', views.create_comment, name='create_comment'),
    path('', views.PostListView.as_view(), name='post_list'),  
    path('tag/<str:tag_slug>/', views.PostListView.as_view(), name='post_list_by_tag'),
]