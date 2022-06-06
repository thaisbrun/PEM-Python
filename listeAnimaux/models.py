from django.db import models
class Animaux(models.Model):
    nom=models.CharField(max_length=20)
    nombrePattes=models.IntegerField()
    dureeVie=models.IntegerField()
    image_url=models.ImageField(null=True, blank=True, upload_to="images/")
    description=models.TextField()

