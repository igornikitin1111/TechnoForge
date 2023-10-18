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
        widget=forms.SelectDateWidget,
    )
    github = forms.URLField(
        label='GitHub',   
    )

    class Meta:
        model = models.UserForge
        fields = (
            'username','first_name', 'last_name', 'email',
            'phone', 'avatar', 'bio', 'birthday', 'github',
            'gender',
            )
        
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            img = Image.open(avatar)
            max_size = (70, 70)
            if img.width > max_size[0] or img.height > max_size[1]:
                img.thumbnail(max_size, Image.ANTIALIAS)
                img.save(avatar.path)
        return avatar

    def clean_second_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['second_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['second_password']