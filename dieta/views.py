from django.shortcuts import render, redirect
from .models import Dieta, CaloriasMeta
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

@login_required
def criar_dieta(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        notas = request.POST.get('notas')
        calorias = request.POST.get('calorias')

        if not titulo or not notas or not calorias:
            return HttpResponseBadRequest("Campos em branco não são permitidos.")

        Dieta.objects.create(user=request.user, titulo=titulo, notas=notas, calorias=calorias)
        return redirect('dieta:lista_dietas')
    return render(request, 'dieta/criar_dieta.html')

@login_required
def editar_dieta(request, dieta_id):
    try:
        dieta = Dieta.objects.get(pk=dieta_id, user=request.user)
    except Dieta.DoesNotExist:
        return HttpResponseBadRequest("Dieta não encontrada.")

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        notas = request.POST.get('notas')
        calorias = request.POST.get('calorias')

        if not titulo or not notas or not calorias:
            return HttpResponseBadRequest("Campos em branco não são permitidos.")

        dieta.titulo = titulo
        dieta.notas = notas
        dieta.calorias = calorias
        dieta.save()
        return redirect('dieta:lista_dietas')
    else:
        # Preencha o contexto com os valores existentes da dieta
        context = {
            'dieta': dieta,
        }
        return render(request, 'dieta/editar_dieta.html', context)

@login_required
def excluir_dieta(request, dieta_id):
    try:
        dieta = Dieta.objects.get(pk=dieta_id, user=request.user)
    except Dieta.DoesNotExist:
        return HttpResponseBadRequest("Dieta não encontrada.")

    dieta.delete()
    return redirect('dieta:lista_dietas')

@login_required
def atualizar_calorias(request, dieta_id):
    try:
        dieta = Dieta.objects.get(pk=dieta_id, user=request.user)
    except Dieta.DoesNotExist:
        return HttpResponseBadRequest("Dieta não encontrada.")

    if request.method == 'POST':
        calorias = request.POST.get('calorias')

        if not calorias:
            return HttpResponseBadRequest("Campo em branco não é permitido.")

        dieta.calorias = calorias
        dieta.save()

    return redirect('dieta:lista_dietas')

@login_required
def lista_dietas(request):
    dietas = Dieta.objects.filter(user=request.user)
    calorias_meta = CaloriasMeta.objects.filter(user=request.user).first()


    return render(request, 'dieta/lista_dietas.html', {'dietas': dietas, 'calorias_meta': calorias_meta})

@login_required
def definir_meta_calorias(request):
    calorias_meta = CaloriasMeta.objects.filter(user=request.user).first()
    print(calorias_meta)  # Adicione esta linha para imprimir o valor

    if request.method == "POST":
        meta_diaria = request.POST.get("calorias_meta")

        if calorias_meta is not None:
            calorias_meta.meta_diaria = meta_diaria
            calorias_meta.save()
        else:
            calorias_meta = CaloriasMeta(user=request.user, meta_diaria=meta_diaria)
            calorias_meta.save()

        return redirect('dieta:lista_dietas')

    return render(request, 'dieta/definir_meta_calorias.html', {'calorias_meta': calorias_meta})
