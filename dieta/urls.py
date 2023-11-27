from django.urls import path
from . import views

app_name = 'dieta'

urlpatterns = [
    path('criar_dieta/', views.criar_dieta, name='criar_dieta'),
    path('editar_dieta/<int:dieta_id>/', views.editar_dieta, name='editar_dieta'),
    path('excluir_dieta/<int:dieta_id>/', views.excluir_dieta, name='excluir_dieta'),
    path('atualizar_calorias/<int:dieta_id>/', views.atualizar_calorias, name='atualizar_calorias'),
    path('lista_dietas/', views.lista_dietas, name='lista_dietas'),
    path('definir_meta_calorias/', views.definir_meta_calorias, name='definir_meta_calorias'),

]
