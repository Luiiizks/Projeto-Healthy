from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PerfilUsuario

@login_required
def calcular_metabolismo_basal(request):
    if request.method == 'POST':
        genero = request.POST['genero']
        idade = int(request.POST['idade'])
        altura = float(request.POST['altura'])
        peso = float(request.POST['peso'])
        # Cálculo do metabolismo basal com base no gênero
        if genero == 'H':  # Homem
            metabolismo_basal = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
        else:  # Mulher
            metabolismo_basal = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
        # Salvar o metabolismo basal no banco de dados
        perfil_usuario, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
        perfil_usuario.genero = genero
        perfil_usuario.idade = idade
        perfil_usuario.altura = altura
        perfil_usuario.peso = peso
        perfil_usuario.metabolismo_basal = metabolismo_basal
        perfil_usuario.save()

        return render(request, 'calculos/result_metabolismo.html', {'metabolismo_basal': metabolismo_basal})

    else:
        # Lógica para lidar com solicitações GET (mostrar o formulário)
        return render(request, 'calculos/calculo_metabolismo_basal.html')
