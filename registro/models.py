from django.db import models
from django.contrib.auth.models import User

class RegistroDiario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    nota = models.TextField()

    def __str__(self):
        return f"Registro de {self.user.username} em {self.data}"
