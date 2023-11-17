from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class PerfilUsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nome, password, **extra_fields)
    
    def authenticate(self, request, email=None, password=None, **kwargs):
        # Implemente a lógica de autenticação personalizada aqui
        try:
            user = self.get(email=email)
        except self.model.DoesNotExist:
            return None

        if user.check_password(password):
            return user
class PerfilUsuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PerfilUsuarioManager()

    USERNAME_FIELD = 'email'

    # Adicione ou altere o related_name para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='perfil_usuarios_groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='perfil_usuarios_permissions',
    )

    def __str__(self):
        return self.nome

# class PerfilUsuario(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     telefone = models.CharField(max_length=15, blank=True, null=True)
#     senha = models.CharField(max_length=100)
#     rg = models.CharField(max_length=20, blank=True, null=True)
#     cpf = models.CharField(max_length=11, unique=True)
#     data_nascimento = models.DateField(blank=True, null=True)
#     cep = models.CharField(max_length=10, blank=True, null=True)

#     def __str__(self):
#         return self.nome
    