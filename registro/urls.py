from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('listar_registros/', views.listar_registros, name='listar_registros'),
    path('criar_registro/', views.criar_registro, name='criar_registro'),
    path('editar_registro/<int:registro_id>/', views.editar_registro, name='editar_registro'),
    path('excluir_registro/<int:registro_id>/', views.excluir_registro, name='excluir_registro'),
]
