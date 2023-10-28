from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import WaterGoal, WeightGoal

@login_required
def water_goal(request):
    if request.method == "POST":
        liters = request.POST["liters"]
        water_goal = WaterGoal.objects.filter(user=request.user).first()
        if water_goal is not None:
            water_goal.liters = liters
            water_goal.save()
        else:
            water_goal = WaterGoal(user=request.user, liters=liters)
            water_goal.save()
        return redirect("/goals/water_goal/")

    user_water_goal = WaterGoal.objects.filter(user=request.user).first()

    return render(request, "goals/water_goal.html", {
        "water_goal": user_water_goal
    })


def goals(request):
    return render(request, "goals/goals.html")

@login_required
def weight_goal(request):
    if request.method == "POST":
        weight = request.POST["weight"]

        # Verifica se o usuário já tem uma meta de peso definida
        weight_goal = WeightGoal.objects.filter(user=request.user).first()

        # Se o usuário já tiver uma meta de peso definida, atualize-a
        if weight_goal is not None:
            weight_goal.weight = weight
            weight_goal.save()

        # Se o usuário não tiver uma meta de peso definida, crie uma nova
        else:
            weight_goal = WeightGoal(user=request.user, weight=weight)
            weight_goal.save()

        return redirect("/goals/weight_goal/")

    user_weight_goal = WeightGoal.objects.filter(user=request.user).first()

    return render(request, "goals/weight_goal.html", {
        "weight_goal": user_weight_goal
    })
