from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    GENERO_CHOICES = [
        ('H', 'Homem'),
        ('M', 'Mulher'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    idade = models.PositiveIntegerField(blank=False, default=0)
    altura = models.FloatField(blank=False, default=0)
    peso = models.FloatField(blank=False, default=0)
    metabolismo_basal = models.FloatField(blank=False, default=0)
