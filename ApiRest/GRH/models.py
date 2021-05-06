from django.db import models
from ApiRest.Utils.models import TimeStamp
from ApiRest.Ecole.models import STATUT_SOCIAL, CIVILITE, MODE_PAIEMENT

"""
CIVILITE = (
    ('Masculin', 'Masculin'),
    ('Feminin', 'Feminin')
)
MODE_PAIEMENT = (
    ('Manuel', 'Manuel'),
    ('Virement', 'Virement Bancaire')
)
"""
CATEGORIE_PERSONNEL = (
    ('Surveillant', 'Surveillant'),
    ('Caissier', 'Caissier'),
    ('Directeurs', (
        ('PDG', 'Promoteur'),
        ('DG', 'Directeur Général'),
        ('DE', 'Directeur des Etudes'),
    )
    ),
    ('Agent De propreté', 'Agent de propreté'),
    ('Agent de sécurité', 'Agent de sécurité')
)


class ConfigurationSalairePersonnel(TimeStamp):
    categoriePersonnel = models.CharField(
        "Catégorie d'employé :", max_length=50, choices=CATEGORIE_PERSONNEL, null=False)
    salaireDefini = models.FloatField('Salaire défini', null=False)

    def __str__(self):
        return f'{self.categorie_personnel} => {self.salaire_defini}'


class Personnel(TimeStamp):
    personnelNumero = models.AutoField('N°:',
                                       primary_key=True, auto_created=True, db_column='n°')
    nom = models.CharField(unique=True, max_length=255,
                           help_text="Tapez tous les noms et prénoms", null=False)
    civilite = models.CharField(
        choices=CIVILITE, max_length=255, default='', null=False)
    dateNaissance = models.CharField('Date de Naissance', max_length=50, help_text='Tappez juste la date de Naissance Eg: 11-Mai-1995',
                                     null=False)
    lieuNaissance = models.CharField('Lieu de Naissance',
                                     max_length=50, default='Brazzaville', db_column="lieuDeNaissance", blank=True)
    statutMatrimonial = models.CharField(
        'Statut matrimonial', max_length=50, choices=STATUT_SOCIAL)
    nationalite = models.CharField(
        max_length=255, default='Congolaise', null=False)
    adresse = models.CharField(max_length=255, null=False)
    telephone = models.CharField(max_length=15, null=False, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    dateEmbauche = models.DateField("Date d'embauche", null=False)
    posteOccupe = models.CharField(
        'Embauché en qualité de :', max_length=50, choices=CATEGORIE_PERSONNEL)

    modePaiement = models.CharField(
        'Mode de paiement', max_length=100, choices=MODE_PAIEMENT, null=False, default=MODE_PAIEMENT[0])
    intituleCompte = models.CharField('Intitulé du compte banquaire',
                                      max_length=250, unique=True, blank=True, help_text="Ecrire le nom du compte bancaire de l'enseignant", null=True)
    numeroCompteBancaire = models.CharField('Numero du compte bancaire',
                                            max_length=250, unique=True, blank=True, null=True)
    numeroCnss = models.CharField('Numero Cnss',
                                  max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-cree_le']
