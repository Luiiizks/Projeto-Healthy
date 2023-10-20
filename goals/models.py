from django.contrib.auth.models import User
from django.db import models


class WaterGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liters = models.FloatField()

    def __str__(self):
        return f"Meta de água de {self.user}: {self.liters} litros"

class WeightGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()

    def __str__(self):
        return f"Meta de peso de {self.user}: {self.weight} quilos"