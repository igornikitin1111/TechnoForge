from django.contrib.auth.backends import ModelBackend
from .models import UserForge
import logging
logger = logging.getLogger(__name__)

class UserForgeAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserForge.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserForge.DoesNotExist:
            return None