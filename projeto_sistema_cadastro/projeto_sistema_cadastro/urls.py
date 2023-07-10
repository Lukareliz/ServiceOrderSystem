from django.urls import path
from app_sistema_cadastro import views

urlpatterns = [
    path('', views.home,name='home'),
    path('ordens/', views.ordens, name='listagem_os')
]
