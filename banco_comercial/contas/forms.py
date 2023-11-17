from django import forms
from .models import PerfilUsuario
from django.core.exceptions import ValidationError

class CadastroForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = PerfilUsuario
        fields = ['nome', 'email', 'telefone', 'senha', 'confirmar_senha', 'rg', 'cpf', 'data_nascimento', 'cep']
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            raise ValidationError("As senhas não correspondem. Por favor, verifique.")

        return cleaned_data