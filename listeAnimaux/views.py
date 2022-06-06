from django.shortcuts import render
from .models import Animaux
def index(request):
    animal=Animaux.objects.all()
    return render(request, 'index.html', {'animal':animal})