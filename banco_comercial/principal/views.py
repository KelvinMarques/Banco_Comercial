from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
def home_view(request):
    return render(request, 'index.html')
# def login_view_redict(request):
#     # Lógica da sua view em app1

#     # Agora, vamos redirecionar para a view em contas
#     url = reverse('contas:login_view')  # Certifique-se de usar o namespace adequado
#     return redirect(url)