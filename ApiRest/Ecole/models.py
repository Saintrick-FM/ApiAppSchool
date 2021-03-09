from django.db import models

# Create your models here.

class Administrateurs (models.Model):
    nom = models.CharField(max_length = 150)
    statut = models.CharField(max_length=150)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
