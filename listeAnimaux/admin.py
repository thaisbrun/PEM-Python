from django.contrib import admin
from .models import Animaux

class AnimauxAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'dureeVie', 'image_url', 'description', 'nombrePattes')
admin.site.register(Animaux, AnimauxAdmin)
