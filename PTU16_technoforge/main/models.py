from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserForge(AbstractUser):
    GENDER = (
        ('Male', _('Male')),
        ('Female', _('Female')),
    )

      
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='media/avatars/', null=True, blank=True) 
    bio = models.TextField( blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_forge_set',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_forge_set',
        blank=True,
        verbose_name='user permissions',
    )
    gender = models.CharField(max_length=10, choices=GENDER, default='Male')
