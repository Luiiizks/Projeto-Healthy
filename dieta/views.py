from django.shortcuts import render, redirect
from .models import Dieta
from .forms import DietaForm
from django.contrib.auth.decorators import login_required

@login_required
def criar_dieta(request):
    if request.method == 'POST':
        form = DietaForm(request.POST)
        if form.is_valid():
            dieta = form.save(commit=False)
            dieta.user = request.user
            dieta.save()
            return redirect('lista_dietas')
    else:
        form = DietaForm()
    return render(request, 'dieta/criar_dieta.html', {'form': form})

@login_required
def editar_dieta(request, dieta_id):
    dieta = Dieta.objects.get(pk=dieta_id)
    if request.method == 'POST':
        form = DietaForm(request.POST, instance=dieta)
        if form.is_valid():
            form.save()
            return redirect('lista_dietas')
    else:
        form = DietaForm(instance=dieta)
    return render(request, 'dieta/editar_dieta.html', {'form': form})

@login_required
def excluir_dieta(request, dieta_id):
    Dieta.objects.filter(pk=dieta_id).delete()
    return redirect('lista_dietas')

@login_required
def atualizar_calorias(request, dieta_id):
    dieta = Dieta.objects.get(pk=dieta_id)
    if request.method == 'POST':
        dieta.calorias = int(request.POST.get('calorias'))
        dieta.save()
    return redirect('lista_dietas')

@login_required
def lista_dietas(request):
    dietas = Dieta.objects.filter(user=request.user)
    return render(request, 'dieta/lista_dietas.html', {'dietas': dietas})
