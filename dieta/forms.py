from django import forms
from .models import Dieta

class DietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = ['notas', 'calorias']
