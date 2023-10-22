from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    # path('user_profile/', views.user_profile, name='user_profile'),

    path('user_blog/', views.user_blog, name='user_blog'),
    path('user_profile/', views.UserProfileDetailView, name='user_profile'),
    path('view_user_profile/<str:username>/', views.view_user_profile, name='view_user_profile'), 
    path('edit_user_profile/', views.UserProfileUpdateView, name='edit_user_profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),  
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),  
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.user_registration, name='register'),  
]