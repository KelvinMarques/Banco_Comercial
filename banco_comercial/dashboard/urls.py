from django.urls import path
from .views import (
    dados_view,
    extrato_view,
    pagar_view,
    transferir_view,
    investir_view,
    emprestimo_view,
    saldo_view,
    notificacoes_view,
    configuracoes_view,
    cartoes_view,
)

app_name = 'dashboard'

urlpatterns = [
    path('dados/', dados_view, name='dados_view'),
    path('extrato/', extrato_view, name='extrato_view'),
    path('pagar/', pagar_view, name='pagar_view'),
    path('transferir/', transferir_view, name='transferir_view'),
    path('investir/', investir_view, name='investir_view'),
    path('emprestimo/', emprestimo_view, name='emprestimo_view'),
    path('saldo/', saldo_view, name='saldo_view'),
    path('notificacoes/', notificacoes_view, name='notificacoes_view'),
    path('configuracoes/', configuracoes_view, name='configuracoes_view'),
    path('cartoes/', cartoes_view, name='cartoes_view'),
]
