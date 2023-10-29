from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    GENERO_CHOICES = [
        ('H', 'Homem'),
        ('M', 'Mulher'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    idade = models.PositiveIntegerField()
    altura = models.FloatField()  # Permite valores nulos
    peso = models.FloatField()
    metabolismo_basal = models.FloatField()
