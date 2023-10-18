from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('view_user_profile/<str:username>/', views.view_user_profile, name='view_user_profile'), 
    path('edit_user_profile/', views.UserProfileUpdateView.as_view(), name='edit_user_profile'),
    path('login/', 'django.contrib.auth.views.login', name='login'),
    path('logout/', 'django.contrib.auth.views.logout', name='logout'),
    path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    path('password_change/', 'django.contrib.auth.views.password_change', name='password_change'),
    path('password_change/done/', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    path('password_reset/', 'django.contrib.auth.views.password_reset', name='password_reset'),
    path('password_reset/done/', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    path('password_reset/complete/', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]