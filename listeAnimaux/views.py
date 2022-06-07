from django.shortcuts import render
from .models import Animaux

def index(request):
    animal = Animaux.objects.all()
    return render(request, 'index.html', {'animal':animal})


def delete_animal(request, animal_id):
    animal = Animaux.objects.get(pk=animal_id)
    animal.delete()
    print("L'animal sélectionné a été supprimé")
    return render(request, 'index.html', {'animal': animal})