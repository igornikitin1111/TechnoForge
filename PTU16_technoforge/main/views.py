from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .models import UserForge
from django.shortcuts import render, get_object_or_404


class UserProfileDetailView(DetailView):
    """
    View for displaying the user profile details.
    """
    model = UserForge
    template_name = 'technoforge/user_profile.html'

class UserProfileUpdateView(UpdateView):
    """
    View for updating the user profile details.
    """
    model = UserForge
    template_name = 'technoforge/edit_user_profile.html'
    fields = ['phone', 'avatar', 'bio', 'birthday', 'github', 'gender']
    success_url = reverse_lazy('user_profile')  

@login_required
def user_profile(request):
    """
    View for displaying the user profile of the currently logged-in user.
    """
    # Get the profile of the current user
    user_profile = UserForge.objects.get(username=request.user.username)
    return render(request, 'technoforge/user_profile.html', {'user_profile': user_profile})

def view_user_profile(request, username):
    """
    View for displaying the user profile of a specific user.
    """
    # Get the profile of the user by their username
    user_profile = get_object_or_404(UserForge, username=username)
    return render(request, 'technoforge/view_user_profile.html', {'user_profile': user_profile})