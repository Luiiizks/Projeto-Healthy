from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from treino.models import Treino
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    treinos = {
        'segunda': None,
        'terça': None,
        'quarta': None,
        'quinta': None,
        'sexta': None,
        'sábado': None,
        'domingo': None
    }

    treinos_existentes = Treino.objects.filter(usuario=request.user)
    for treino in treinos_existentes:
        treinos[treino.dia_da_semana] = treino

    return render(request, 'treino/index.html', {'treinos': treinos})

@login_required
def dia(request, dia_da_semana):
    try:
        treino = Treino.objects.get(dia_da_semana=dia_da_semana, usuario=request.user)
    except Treino.DoesNotExist:
        treino = Treino(dia_da_semana=dia_da_semana, usuario=request.user)

    if request.method == 'POST':
        treino.texto = request.POST['texto']
        treino.save()
        return redirect('treino:index')

    return render(request, 'treino/dia.html', {'treino': treino})

@login_required
def editar_treino(request, dia_da_semana):
    try:
        treino = Treino.objects.get(dia_da_semana=dia_da_semana, usuario=request.user)
        if not treino.editavel:
            return HttpResponseNotFound("Treino não é editável.")
    except Treino.DoesNotExist:
        return HttpResponseNotFound("Treino não encontrado.")

    if request.method == 'POST':
        treino.texto = request.POST['texto']
        treino.save()
        return redirect('treino:index')

    return render(request, 'treino/editar_treino.html', {'treino': treino})

@login_required
def excluir_treino(request, dia_da_semana):
    try:
        treino = Treino.objects.get(dia_da_semana=dia_da_semana, usuario=request.user)
        if not treino.editavel:
            return HttpResponseNotFound("Treino não é editável.")
    except Treino.DoesNotExist:
        return HttpResponseNotFound("Treino não encontrado.")

    if request.method == 'POST':
        treino.delete()
        return redirect('treino:index')

    return render(request, 'treino/excluir_treino.html', {'treino': treino})

@login_required
def salvar_treino(request, dia_semana=None):
    if request.method == 'POST':
        texto = request.POST['texto']

        if dia_semana:
            try:
                treino = Treino.objects.get(dia_da_semana=dia_semana, usuario=request.user)
                treino.texto = texto
            except Treino.DoesNotExist:
                treino = Treino(dia_da_semana=dia_semana, texto=texto, usuario=request.user)
        else:
            pass

        treino.save()
        return redirect('treino:index')
    else:
        return redirect('treino:index')
    
    
