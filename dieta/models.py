from django.db import models
from django.contrib.auth.models import User

class Dieta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.TextField(default="Qual Refeição")
    notas = models.TextField()
    calorias = models.IntegerField()

    def __str__(self):
        return self.user.username + "'s Dieta"
    
class CaloriasMeta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meta_diaria = models.IntegerField()

    def __str__(self):
        return f"Meta de calorias diárias de {self.user}: {self.meta_diaria} calorias"
