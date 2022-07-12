from django import forms
from django.forms import ModelForm
from .models import Animaux
from .models import Plantes

class AnimalForm(ModelForm):
    class Meta:
        model = Animaux
        fields = ('nom', 'nombrePattes', 'dureeVie', 'image_url', 'description')

class PlanteForm(ModelForm):
    class Meta:
        model = Plantes
        fields = ('nom', 'nomScientifique', 'image_url', 'description')