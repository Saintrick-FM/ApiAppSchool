from django.db import models
from ApiRest.Utils.models import TimeStamp
from ApiRest.Inscriptions.models import Eleve
from ApiRest.Ecole.models import Enseignant
from ApiRest.GRH.models import Personnel
CATEGORIE_ENSEIGNANT = (
    ('Primaire', 'Enseigne au Primaire'),
    ('College', 'Enseigne au College')
)

MOIS = (
    ('Octobre', 'Octobre'),
    ('Novembre', 'Novembre'),
    ('Décembre', 'Décembre'),
    ('Janvier', 'Janvier'),
    ('Février', 'Février'),
    ('Mars', 'Mars'),
    ('Avril', 'Avril'),
    ('Mai', 'Mai'),
    ('Juin', 'Juin'),
    ('Autres', (
        ('Juillet', 'Juillet'),
        ('Aout', 'Aout'),
        ('Septembre', 'Septembre'),
    )
    ),

)
TYPEFRAIS = (
    ('Frais Mensuel', 'Frais Mensuel'),
    ('Frais Trimesrtiel', 'Frais trimestriel'),
    ('Frais Annuel', 'Frais Annuel'),
    ('Assurance', 'Assurance'),
    ("Dossier d'examen", "Dossier d'examen"),
    ('Macaron', 'Macaron'),
    ("Tenu d'eps", "Tenu d'eps")
)
# Create your models here.


class ConfigurationFraisEleve(TimeStamp):
    paiement_frais_numero = models.AutoField(
        'Paiement frais n°:', primary_key=True)
    frais = models.CharField(
        'Intitulé du frais', choices=TYPEFRAIS, max_length=100, null=False)
    montant = models.FloatField(null=False)

    def __str__(self):
        return f'{self.frais} => {self.montant}'

    class Meta:
        db_table = 'Configuration_Frais_Eleve'


class ConfigurationSalaireEnseignant(TimeStamp):
    categorie_enseignant = models.CharField(
        "Catégorie d'employé :", max_length=30, choices=CATEGORIE_ENSEIGNANT, null=False)
    salaire_defini = models.FloatField('Salaire défini', null=False)

    def __str__(self):
        return f'{self.categorie_enseignant} => {self.salaire_defini}'

    class Meta:
        db_table = 'Configuration_Salaire_Enseignant'


class PaiementFrais(TimeStamp):
    eleve = models.ForeignKey(
        Eleve, on_delete=models.DO_NOTHING, related_name='eleve_payant')
    type_frais = models.ForeignKey(
        ConfigurationFraisEleve, on_delete=models.DO_NOTHING, verbose_name='Type de frais A payer', related_name='type_frais')
    montant_frais = models.ForeignKey(ConfigurationFraisEleve, on_delete=models.DO_NOTHING, editable=False,
                                      null=False)
    mois = models.CharField('Mois à payer', max_length=30,
                            choices=MOIS, null=True, blank=True)
    montant_a_payer = models.FloatField(null=False)
    montant_deja_paye = models.FloatField(
        default=0, null=False, editable=False)
    montant_restant = models.FloatField(null=False, editable=False)
    statut = models.BooleanField(
        blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")

    def __str__(self):
        return f'{self.type_frais} => {self.montant_frais}'

    class Meta:
        db_table = 'Paiement_frais'
        verbose_name_plural = 'frais'


class PaiementSalaireEnseignant(TimeStamp):
    paiement_numero = models.AutoField('Paiement numéro =>', primary_key=True)

    nom_enseignant = models.ForeignKey(
        Enseignant, on_delete=models.DO_NOTHING, related_name="enseignant_a_payer")
    mois_paiement = models.CharField(max_length=50, null=False, choices=MOIS)
    heures_effectuees = models.CharField(
        max_length=50, default='8h de cours enseignees', editable=False)
    montant_a_payer = models.FloatField(null=False)
    montant_deja_paye = models.FloatField(
        default=0, null=False, editable=False)
    montant_restant = models.FloatField(null=False, editable=False)
    statut = models.BooleanField(
        blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")

    def __str__(self):
        return f'Salaire enseignant => {self.type_de_paie} | Mois de: {self.mois_paiement}'

    class Meta:
        db_table = 'Paiement_Salaire_Enseignant'


class PaiementSalairePersonnel(TimeStamp):
    paiement_numero = models.AutoField('Paiement numéro =>', primary_key=True)
    nom_personnel = models.ForeignKey(
        Personnel, on_delete=models.DO_NOTHING, related_name="personnel_a_payer")
    mois_paiement = models.CharField(max_length=50, null=False, choices=MOIS)
    # heures_effectuees= models.ForeignKey(HeuresEnseignant, )
    montant_a_payer = models.FloatField(null=False)
    montant_deja_paye = models.FloatField(
        default=0, null=False, editable=False)
    montant_restant = models.FloatField(null=False, editable=False)
    statut = models.BooleanField(
        blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")

    def __str__(self):
        return f' Salaire de => {self.nom_personnel} | Mois de: {self.mois_paiement}'

    class Meta:
        db_table = 'Paiement_Salaire_Personnel'
