from django.db import models
from django.contrib.auth import get_user_model

class Treino(models.Model):
    dia_da_semana = models.CharField(max_length=10)
    texto = models.TextField()
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    editavel = models.BooleanField(default=True)  # Adicione um campo para indicar se o treino é editável

    def __str__(self):
        return self.dia_da_semana

# class UsuarioTreino(models.Model):
#     usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Using get_user_model()
#     treino = models.ForeignKey(Treino, on_delete=models.CASCADE)  # No single quotes around 'treino.Treino'
