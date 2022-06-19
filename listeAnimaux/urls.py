from . import views
from django.urls import path

urlpatterns=[
    path('', views.index),
    path('addAnimal', views.addAnimal, name="addAnimal"),
    path('delete_animal/<animal_id>', views.delete_animal, name='delete-animal'),
    path('delete_plante/<plante_id>', views.delete_plante, name='delete-plante'),
    path('updateAnimal/<animal_id>', views.updateAnimal, name='updateAnimal')
]