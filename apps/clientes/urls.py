from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.ClienteCreateView.as_view(), name='cliente__cria'),
    path('<int:pk>/atualizar/', views.ClienteUpdateView.as_view(), name='cliente__atualiza'),
]