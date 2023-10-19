from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import UserForge
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    return render(request, 'registration/login.html', {'form': form})

def user_registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            user_forge = UserForge(
                first_login=None, 
                phone=user_form.cleaned_data['phone'],
                avatar=user_form.cleaned_data['avatar'],
                bio=user_form.cleaned_data['bio'],
                birthday=user_form.cleaned_data['birthday'],
                github=user_form.cleaned_data['github'],
                gender=user_form.cleaned_data['gender']
            )
            user_forge.save()
            new_user.userforge = user_forge
            new_user.save()

            return render(request, 'registration/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form})



class UserProfileDetailView(generic.DetailView):
    """
    View for displaying the user profile details.
    """
    model = UserForge
    template_name = 'technoforge/user_profile.html'

class UserProfileUpdateView(generic.UpdateView):
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
    return render(
        request, 'technoforge/user_profile.html', {'user_profile': user_profile}
        )

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

def user_profile(request):
    return render(request, "technoforge/user_profile.html")