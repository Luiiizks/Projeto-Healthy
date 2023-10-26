from django.urls import path

from . import views

app_name = 'treino'

urlpatterns = [
    path('', views.index, name='index'),
    path('dia/<str:dia_da_semana>/', views.dia, name='dia'),
    path('editar/<str:dia_da_semana>/', views.editar_treino, name='editar_treino'),
    path('excluir/<str:dia_da_semana>/', views.excluir_treino, name='excluir_treino'),
    path('salvar/<str:dia_semana>/', views.salvar_treino, name='salvar')

]
