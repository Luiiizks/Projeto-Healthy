from django.urls import path
from . import views

app_name = 'calculos'

urlpatterns = [
    path('metabolismo/', views.calcular_metabolismo_basal, name='metabolismo_basal'),

]
