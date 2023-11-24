from django.urls import path
from . import views
from .views import calcular_ingestao_agua

app_name = 'calculos'

urlpatterns = [
    path('metabolismo/', views.calcular_metabolismo_basal, name='metabolismo_basal'),
    path('agua/', views.calcular_ingestao_agua, name='agua'),
   

]
