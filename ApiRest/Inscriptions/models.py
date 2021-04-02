from django.db import models
from django.utils import timezone
from ApiRest.Classe.models import Classe
from datetime import date

SEXE = (
    ('Masculin', 'Masculin'),
    ('Feminin', 'Feminin')
)


class Eleve(models.Model):

    classe = models.ForeignKey(
        Classe, on_delete=models.CASCADE, related_name="eleve")
    eleveNumber = models.AutoField(
        primary_key=True, auto_created=True, db_column='n°', verbose_name='n°:')
    nom = models.CharField(unique=True, max_length=255,
                           help_text="Tapez tous les noms et prénoms", null=False)
    sexe = models.CharField(
        choices=SEXE, max_length=255, default='', null=False)
    naissance = models.CharField(max_length=50, help_text='Tappez juste la date de Naissance Eg: 11-Mai-1995',
                                 null=False)
    age = models.CharField(max_length=50, editable=False,
                           null=True, blank=True)
    lieuNaiss = models.CharField(
        max_length=50, default='Brazzaville', db_column="lieuDeNaissance")
    dateInscrit = models.DateField(auto_now_add=True)
    scolarite = models.CharField(max_length=50, default='', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_column='updated_at')

    def __str__(self):
        return f'{self.nom}'
