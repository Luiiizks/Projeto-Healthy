from django import forms
from .models import Dieta

class DietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = ['titulo','notas', 'calorias']

    widgets = {
        'titulo': forms.TextInput(attrs={'style': 'width: 100px; height: 100px;'}),
        'notas': forms.TextInput(attrs={'style': 'width: 200px; height: 100px;'}),

    }

