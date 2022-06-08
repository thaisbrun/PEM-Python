from django.db import models

class Animaux(models.Model):
    nom=models.CharField(max_length=20)
    nombrePattes=models.IntegerField()
    dureeVie=models.IntegerField()
    image_url=models.CharField(max_length=2000)
    description=models.TextField()

class Plantes(models.Model):
    nom=models.CharField(max_length=20)
    nomScientifique=models.CharField(max_length=50)
    image_url=models.CharField(max_length=2000)
    description=models.TextField()
