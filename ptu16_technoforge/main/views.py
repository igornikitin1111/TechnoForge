from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import UserForge
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserProfileUpdateForm
from PIL import Image
from django.core.exceptions import ValidationError
import os
from django.conf import settings
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Authenticated successfully')
                    return redirect('index')
                else:
                    messages.error(request, 'Account is disabled.')
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Invalid form data. Please check your input.')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            avatar = form.cleaned_data['avatar']
            if avatar:
                try:
                    image = Image.open(avatar)
                    image.thumbnail((70, 70), Image.LANCZOS)
                    avatar_path = f"avatars/{user.username}_avatar.png"
                    avatar_file = os.path.join(settings.MEDIA_ROOT, avatar_path)
                    image.save(avatar_file, 'PNG')
                    user.avatar = avatar_path
                except Exception as e:
                    raise ValidationError("Invalid image file. Please upload a valid image.")
                
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

class UserProfileDetailView(generic.DetailView):
    """
    View for displaying the user profile details.
    """
    model = UserForge
    template_name = 'technoforge/user_profile.html'
    def get_object(self, queryset=None):
        return self.request.user


UserProfileDetailView = login_required(UserProfileDetailView.as_view())

class UserProfileUpdateView(generic.UpdateView):
    """
    View for updating the user profile details.
    """
    model = UserForge
    form_class = UserProfileUpdateForm  # Используем созданную форму
    template_name = 'technoforge/edit_user_profile.html'
    success_url = reverse_lazy('user_profile') 

    def get_object(self, queryset=None):
        return self.request.user

UserProfileUpdateView = login_required(UserProfileUpdateView.as_view())



def view_user_profile(request, username):
    """
    View for displaying the user profile of a specific user.
    """
    # Get the profile of the user by their username
    user_profile = get_object_or_404(UserForge, username=username)
    return render(
        request, 'technoforge/view_user_profile.html', {'user_profile': user_profile}
        )

def index(request):
    return render(request, "technoforge/index.html")

def user_blog(request):
    return render(request, "technoforge/user_blog.html")