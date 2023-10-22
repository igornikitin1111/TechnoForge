from . import models
from django import forms
from PIL import Image



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput
        )
    second_password = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput
        )
    gender = forms.ChoiceField(
        label='Gender',
        choices=models.UserForge.GENDER,
        widget=forms.Select,
    )
    birthday = forms.DateField(
        label='Birthday',
        widget=forms.SelectDateWidget(years=range(1900, 2023)),
    )
    github = forms.URLField(
        label='GitHub',
        required=False   
    )
    bio = forms.CharField(
        label='Bio',
        widget=forms.Textarea,
        required=False
    )
    avatar = forms.ImageField(
        label='Avatar',
        required=False,
    )

    class Meta:
        model = models.UserForge
        fields = (
            'username','first_name', 'last_name', 'email',
            'phone', 'avatar', 'bio', 'birthday', 'github',
            'gender',
            )
        
    def clean_second_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['second_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['second_password']
    

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.UserForge
        fields = ('email','phone', 'avatar', 'bio', 'birthday', 'github', 'gender')