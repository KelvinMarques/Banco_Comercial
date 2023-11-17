from django.db import models

# Create your models here.
# dashboard/models.py
from django.db import models
from django.contrib.auth.models import User  # Se você estiver usando autenticação de usuário do Django


# Cartão
class CartaoDebito(models.Model):
    nome = models.CharField(max_length=255)
    numero = models.CharField(max_length=16)
    titular = models.CharField(max_length=255)
    data_vencimento = models.DateField()

class CartaoCredito(models.Model):
    nome = models.CharField(max_length=255)
    numero = models.CharField(max_length=16)
    titular = models.CharField(max_length=255)
    data_vencimento = models.DateField()
# ========


class Configuracao(models.Model):
    # Campos específicos para a tela de configuração
    opcao1 = models.CharField(max_length=255)
    # Adicione outros campos necessários

class Dados(models.Model):
    # Campos específicos para a tela de dados
    informacao1 = models.CharField(max_length=255)
    # Adicione outros campos necessários

class Emprestimo(models.Model):
    # Campos específicos para a tela de empréstimo
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    # Adicione outros campos necessários

# Adicione modelos para as outras telas (Extrato, Investir, Notificações, Pagamento, Transferir, etc.)
