from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
    path('view_user_profile/<str:username>/', views.view_user_profile, name='view_user_profile'),    # noqa: E501
    path('edit_user_profile/', views.UserProfileUpdateView.as_view(), name='edit_user_profile'),  # noqa: E501
]