from django.urls import path
from .views import cadastro_view, poscadastro_view,redict_home, login_view
app_name = 'contas'
urlpatterns = [
    path('cadastro/', cadastro_view, name='cadastro_view'),
    path('pos/', poscadastro_view, name='poscadastro_view'),
    path('login/', login_view, name='login_view'),
    path('redict_home/', redict_home, name='redict_home'),

    # ... outras URLs ...
]
