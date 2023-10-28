from django.db import models
from django.contrib.auth import get_user_model

class Treino(models.Model):
    dia_da_semana = models.CharField(max_length=10)
    texto = models.TextField()
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    editavel = models.BooleanField(default=True)

    def __str__(self):
        return self.dia_da_semana
