from django.contrib.auth.backends import ModelBackend
from .models import PerfilUsuario

class PerfilUsuarioBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = PerfilUsuario.objects.get(email=email)
        except PerfilUsuario.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
