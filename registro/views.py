from django.shortcuts import render, redirect
from .models import RegistroDiario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

@login_required
def listar_registros(request):
    registros = RegistroDiario.objects.filter(user=request.user)
    return render(request, 'registro/listar_registros.html', {'registros': registros})

@login_required
def criar_registro(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        nota = request.POST.get('nota')

        if not data or not nota:
            return HttpResponseBadRequest("Campos em branco não são permitidos.")

        RegistroDiario.objects.create(user=request.user, data=data, nota=nota)
        return redirect('registro:listar_registros')

    return render(request, 'registro/criar_registro.html')

@login_required
def editar_registro(request, registro_id):
    try:
        registro = RegistroDiario.objects.get(pk=registro_id, user=request.user)
    except RegistroDiario.DoesNotExist:
        return HttpResponseBadRequest("Registro não encontrado.")

    if request.method == 'POST':
        data = request.POST.get('data')
        nota = request.POST.get('nota')

        if not data or not nota:
            return HttpResponseBadRequest("Campos em branco não são permitidos.")

        registro.data = data
        registro.nota = nota
        registro.save()
        return redirect('registro:listar_registros')
    else:
        context = {'registro': registro}
        return render(request, 'registro/editar_registro.html', context)

@login_required
def excluir_registro(request, registro_id):
    try:
        registro = RegistroDiario.objects.get(pk=registro_id, user=request.user)
    except RegistroDiario.DoesNotExist:
        return HttpResponseBadRequest("Registro não encontrado.")

    registro.delete()
    return redirect('registro:listar_registros')
