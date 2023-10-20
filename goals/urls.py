from django.urls import path

from . import views

urlpatterns = [
    path("water_goal/", views.water_goal, name="water_goal"),
    path("weight_goal/", views.weight_goal, name="weight_goal"),

    path("goals", views.goals, name="goal"),
]
