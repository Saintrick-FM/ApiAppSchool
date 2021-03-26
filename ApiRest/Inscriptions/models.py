from django.db import models
from datetime import date
from ApiRest.Classe.models import Classe, SCOLARITE

SEXE = (
    ('Masculin', 'Masculin'),
    ('Feminin', 'Feminin')
)


class Eleve(models.Model):
    now = date.today()
    anneeActuelle = int(now.strftime("%Y"))

    age = lambda today, yearBirth=1995: f'{today - yearBirth} ans'

    nom = models.CharField(max_length=255, unique=True, help_text="Tapez tous les noms et prénoms", null=False)
    sexe = models.CharField(choices=SEXE, max_length=255, default='', null=False)
    naissance = models.DateField(auto_now_add=True, null=False)
    age = models.CharField(max_length=20, default=age(anneeActuelle))
    lieuNaiss = models.CharField(max_length=50, default='Brazzaville', db_column="lieuDeNaissance")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="classeEleve", null=False)
    dateInscrit = models.DateField(auto_now_add=True)
    scolarite= models.CharField(max_length=50, default='', editable=False)

    def __str__(self):
        return f'{self.nom} {self.prenoms} '
