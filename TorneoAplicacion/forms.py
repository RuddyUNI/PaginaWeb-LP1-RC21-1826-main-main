from django import forms
from .models import Torneo, Inscripcion

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['torneo']
