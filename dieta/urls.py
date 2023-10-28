from django.urls import path
from . import views

app_name = 'dieta'

urlpatterns = [
    path('criar-dieta/', views.criar_dieta, name='criar_dieta'),
    path('editar-dieta/<int:dieta_id>/', views.editar_dieta, name='editar_dieta'),
    path('excluir-dieta/<int:dieta_id>/', views.excluir_dieta, name='excluir_dieta'),
    path('atualizar-calorias/<int:dieta_id>/', views.atualizar_calorias, name='atualizar_calorias'),
    path('lista-dietas/', views.lista_dietas, name='lista_dietas'),  # Adicione esta linha
]
