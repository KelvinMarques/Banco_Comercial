from django.shortcuts import render
from contas.models import PerfilUsuario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from contas.models import PerfilUsuario
from django.contrib.auth.decorators import login_required
# Create your views here.

def get(self, request, *args, **kwargs):
        # Obtenha o perfil do usuário diretamente usando self.request.user
        usuario = self.request.user
        try:
            # Certifique-se de que o campo correto seja usado ('nome' em vez de 'usuario')
            perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
            context = {'user_profile': perfil_usuario}
        except PerfilUsuario.DoesNotExist:
            # Lide com o caso em que o perfil do usuário não existe
            context = {'user_profile': None}
class UserProfileMixin:
    template_name = None  # Substitua por seu template desejado

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
            context['user_profile'] = perfil_usuario
        except PerfilUsuario.DoesNotExist:
            context['user_profile'] = None

        return context

    def post(self, request, *args, **kwargs):
        # Lógica para lidar com um pedido POST
        # Por exemplo, atualizar as configurações do usuário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        
        # Lógica para atualizar os dados do usuário no banco de dados

        return redirect('dashboard:configuracoes_view')



def dados_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'dados.html', context)

def extrato_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'extrato.html', context)

def pagar_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'pagar.html', context)

def transferir_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'transferir.html', context)

def investir_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'investir.html', context)

def emprestimo_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'emprestimo.html', context)

def saldo_view(request):
    context = {'user_profile': request.user}
    return render(request, 'principal.html', context)

def notificacoes_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'notificacoes.html', context)

def configuracoes_view(request):
    # Lógica para lidar com um pedido POST, se necessário
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        # Lógica para atualizar os dados do usuário no banco de dados
        return redirect('dashboard:configuracoes_view')

    # Lógica para lidar com um pedido GET
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'configurar.html', context)

def cartoes_view(request):
    usuario = request.user
    try:
        perfil_usuario = PerfilUsuario.objects.get(nome=usuario)
        context = {'user_profile': perfil_usuario}
    except PerfilUsuario.DoesNotExist:
        context = {'user_profile': None}
    return render(request, 'cartao.html', context)
