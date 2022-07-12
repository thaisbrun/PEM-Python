from django.shortcuts import render, redirect
from .forms import AnimalForm
from .forms import PlanteForm
from .models import Animaux
from .models import Plantes
def index(request):
    animal = Animaux.objects.all()
    plante = Plantes.objects.all()
    return render(request, 'index.html', {'animal':animal, 'plante':plante})

def updateAnimal(request, animal_id):
    animal = Animaux.objects.get(pk=animal_id)
    form = AnimalForm(request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'updateAnimal.html', {'animal': animal,
                                                 'form': form})

def delete_animal(request, animal_id):
    animal = Animaux.objects.get(pk=animal_id)
    animal.delete()
    print("L'animal sélectionné a été supprimé")
    return render(request, 'index.html', {'animal': animal})

def delete_plante(request, plante_id):
    plante = Plantes.objects.get(pk=plante_id)
    plante.delete()
    print("La plante sélectionnée a été supprimée")
    return render(request, 'index.html', {'plante': plante})

def addAnimal(request):
   return render(request, 'addAnimal.html', {})

def addPlantes(request):
    return render(request, 'addPlantes.html',{})