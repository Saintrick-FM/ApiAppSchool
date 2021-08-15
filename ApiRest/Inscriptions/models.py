from django.db import models
from ApiRest.Utils.models import TimeStamp
from ApiRest.Ecole.models import Classe, AnneeScolaire
from datetime import date

SEXE = (('Masculin', 'Masculin'), ('Feminin', 'Feminin'))
SANTE = (
    ('Apte', 'Apte'),
    ('Inapte', 'Inapte')
)

STATUT = (
    ('Nouveau', 'Nouveau'),
    ('Redoublant', 'Redoublant')
)

now = date.today()


def anneeAcademique(annee=now):
    return f'{annee.strftime("%Y")}-{(int(annee.strftime("%Y")) + 1)}'


class Eleve(TimeStamp):

    eleveNumber = models.AutoField('n°:',
                                   primary_key=True, auto_created=True, db_column='n°')
    nom = models.CharField(unique=True, max_length=255,
                           help_text="Tapez tous les noms et prénoms", null=False)
    sexe = models.CharField(
        choices=SEXE, max_length=255, default='', null=False)
    dateLieuNaissance = models.CharField(max_length=100, help_text='Tapez  la date et le lieu de Naissance Eg: 11-Mai-1995 à Brazzaville',
                                 null=False)

    adresse= models.CharField('Domicile de l\'élève', max_length=250, null=False)

    etatSanitaire = models.CharField('Etat sanitaire', max_length=20,
                                     choices=SANTE, default=SANTE[0], null=False)
    ecoleDorigine = models.CharField(
        "Ecole d'origine", max_length=255, default='Saint Martin')
    nomMaman = models.CharField('Nom de la mère', max_length=255,
                                help_text="Tapez tous les noms et prénoms", null=True)
    telMaman = models.CharField(
        'Tel de la mère', max_length=15, null=True, blank=True)
    nomPapa = models.CharField('Nom du père', max_length=255,
                               help_text="Tapez tous les noms et prénoms", null=True)
    telPapa = models.CharField(
        'Tel du la père', max_length=15, null=True, blank=True)
    tuteur = models.CharField(max_length=255, null=False)
    telTuteur = models.CharField('Tel du tuteur', max_length=15, null=False)
    emailTuteur = models.EmailField(
        'email du tuteur', max_length=255, blank=True, null=True)

    dateInscription = models.DateField(
        "Date d'inscription", auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(
        auto_now=True, db_column='updated_at', editable=False)
    classe = models.ForeignKey(
        Classe, on_delete=models.CASCADE, related_name="eleve")
    redoublant = models.CharField(max_length=25,
                                  choices=STATUT, null=False, default=STATUT[0])
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='eleve_annee_scolaire', editable=False)

    # scolarite = models.CharField(max_length=50, default='', editable=False)

    def __str__(self):
        return f'{self.nom}'
