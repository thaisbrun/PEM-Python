from . import views
from django.urls import path

urlpatterns=[
    path('', views.index),
    path('delete_animal/<animal_id>', views.delete_animal, name='delete-animal')
]