from django.db import models
from ApiRest.Ecole import models as modelEcole


# Create your models here.

class AbstractClasse(models.Model):
    identifiant = models.CharField(primary_key=True, unique=True, help_text='taper la salle Ex: 3e',
                                   max_length=50)
    referenceSite = models.ForeignKey(modelEcole.Site, on_delete=models.CASCADE)
    heuresCours = models.CharField(default="7h30-13h", max_length=100)
    nbreEleves = models.IntegerField(null=False)
    nbreSalles = models.IntegerField(default=1, null=False)
    contenance = models.IntegerField(null=False)
    totalFilles = models.IntegerField(null=False)
    totalGarcons = models.IntegerField(null=False)
    matieresEnseigne = models.TextField(max_length=800)
    redoublants = models.IntegerField(default=0, null=False)
    nouveaux = models.IntegerField(default=0, null=False)
    elevesVenuDailleurs = models.IntegerField(default=0, null=False)
    inscrits = models.IntegerField(null=False)
    scolarite= models.CharField(help_text="Frais à payer mensuellement Eg: 8000F", null=False, max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)

    class Meta:
        abstract = True


class Classe(AbstractClasse, models.Model):
    def __str__(self):
        return 'Classe {}'.format(self.identifiant)

