from django.shortcuts import render
from .forms import AnimalForm
from .models import Animaux
from .models import Plantes
def index(request):
    animal = Animaux.objects.all()
    plante = Plantes.objects.all()
    return render(request, 'index.html', {'animal':animal, 'plante':plante})


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
    submitted = False
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
           # return HttpResponseRedirect('addAnimal.html?submitted=True')
        else:
            form = AnimalForm
            if 'submitted' in request.GET:
                submitted = True

        return render(request, 'addAnimal.html', {'form':form, 'submitted':submitted})
