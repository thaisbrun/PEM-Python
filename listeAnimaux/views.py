from django.shortcuts import render
from .forms import AnimalForm
from .models import Animaux

def index(request):
    animal = Animaux.objects.all()
    return render(request, 'index.html', {'animal':animal})


def delete_animal(request, animal_id):
    animal = Animaux.objects.get(pk=animal_id)
    animal.delete()
    print("L'animal sélectionné a été supprimé")
    return render(request, 'index.html', {'animal': animal})

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
