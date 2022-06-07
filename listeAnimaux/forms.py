from django import forms
from django.forms import ModelForm
from .models import Animaux

class AnimalForm(ModelForm):
    class Meta:
        model = Animaux
        fields = ('nom', 'nombrePattes', 'dureeVie', 'image_url', 'description')
