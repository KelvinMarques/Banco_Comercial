
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .forms import CadastroForm
from .models import PerfilUsuario, PerfilUsuarioManager


# Create your views here.

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            # Lógica após o salvamento bem-sucedido
            return redirect('contas:login_view')
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

    
def poscadastro_view(request):
    # Lógica para a página pós-cadastro aqui
    return render(request, 'poscadastro.html')



def login_view(request):
    if request.method == 'POST':
        
        
        email = request.POST.get('input_email')
        senha = request.POST.get('input_password')
        # print(PerfilUsuario.objects.filter(email=email).exists() and PerfilUsuario.objects.filter(senha=senha).exists())
        if PerfilUsuario.objects.filter(email=email).exists() and PerfilUsuario.objects.filter(senha=senha).exists() :
            emaiBanco = PerfilUsuario.objects.get(email=email).email
            user = PerfilUsuario.objects.authenticate(request, email=emaiBanco, password=senha)
            
            print(f"USER ESTÁ FUNCIONANDO OU NÃO: {user}")
            if user is not None:
                print("Autenticou")
                login(request, user)
                # Redireciona para a URL nomeada da view do dashboard
                print(reverse('dashboard:saldo_view'))

            return redirect('/client/saldo/')
        else:
            print("Não Autenticou")
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')

def redict_home(request):
    # Lógica adicional, se necessário
    # ...
    url = reverse('principal:home_view')
    # Redireciona para a view do outro app
    return redirect(url)
@login_required
def dashboard_view(request):
    # Adicione lógica adicional conforme necessário
    return render(request, 'dashboard/dashboard.html')