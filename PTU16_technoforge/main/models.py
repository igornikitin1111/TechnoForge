from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserForge(AbstractUser):
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='media/avatars/')
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
