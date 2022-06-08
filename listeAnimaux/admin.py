from django.contrib import admin
from .models import Animaux
from .models import Plantes

class AnimauxAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'dureeVie', 'image_url', 'description', 'nombrePattes')
admin.site.register(Animaux, AnimauxAdmin)

class PlantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'nomScientifique', 'image_url', 'description')
admin.site.register(Plantes, PlantesAdmin)