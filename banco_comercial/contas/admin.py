from django.contrib import admin
from .models import PerfilUsuario
# Register your models here.
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'senha','email', 'telefone', 'rg', 'cpf', 'data_nascimento', 'cep')
    search_fields = ('nome', 'email', 'cpf')  # Adicione campos que você deseja pesquisar
