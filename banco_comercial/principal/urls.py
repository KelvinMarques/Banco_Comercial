from django.urls import path
from .views import home_view

app_name = 'principal'
urlpatterns = [
    path('', home_view, name='home_view'),
    # path('redict_for_login/', login_view_redict, name='login_view_redict'),
    # ... outras URLs ...
]
