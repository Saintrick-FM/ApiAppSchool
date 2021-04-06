from django.db import models
from django.utils import timezone
from ApiRest.Ecole.models import Classe
from datetime import date

SEXE = (
    ('Masculin', 'Masculin'),
    ('Feminin', 'Feminin')
)
SANTE = (
    ('Apte', 'Apte'),
    ('Inapte', 'Inapte')
)

STATUT = (
    ('Nouveau', 'Nouveau'),
    ('Redoublant', 'Redoublant')
)


class Eleve(models.Model):

    eleveNumber = models.AutoField('n°:',
                                   primary_key=True, auto_created=True, db_column='n°')
    nom = models.CharField(unique=True, max_length=255,
                           help_text="Tapez tous les noms et prénoms", null=False)
    sexe = models.CharField(
        choices=SEXE, max_length=255, default='', null=False)
    naissance = models.CharField(max_length=50, help_text='Tappez juste la date de Naissance Eg: 11-Mai-1995',
                                 null=False)

    lieuNaiss = models.CharField(
        max_length=50, default='Brazzaville', db_column="lieuDeNaissance")
    nationalite = models.CharField(
        max_length=255, default='Congolaise', null=False)
    etat_sanitaire = models.CharField(max_length=20,
                                      choices=SANTE, default=SANTE[0], null=False)
    ecole_d_origine = models.CharField(max_length=255, default='Saint Martin')
    nom_de_maman = models.CharField(max_length=255,
                                    help_text="Tapez tous les noms et prénoms", null=False)
    tel_maman = models.CharField(max_length=15, null=True, blank=True)
    nom_de_papa = models.CharField(max_length=255,
                                   help_text="Tapez tous les noms et prénoms", null=False)
    tel_papa = models.CharField(max_length=15, null=True, blank=True)
    tuteur = models.CharField(max_length=255, null=False)
    tel_tuteur = models.CharField(max_length=15, null=False)
    email_tuteur = models.EmailField(max_length=255, null=True)

    date_inscription = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, db_column='updated_at', editable=False)
    classe = models.ForeignKey(
        Classe, on_delete=models.CASCADE, related_name="eleve")
    redoublant = models.CharField(max_length=25,
                                  choices=STATUT, null=False, default=STATUT[0])
    scolarite = models.CharField(max_length=50, default='', editable=False)

    def __str__(self):
        return f'{self.nom}'
