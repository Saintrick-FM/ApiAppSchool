from django.db import models
from ApiRest.Utils.models import TimeStamp
from ApiRest.Inscriptions.models import Eleve
from ApiRest.Ecole.models import Enseignant, Classe, AnneeScolaire
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
InscReinsc = (
    ('Frais Inscription', 'Frais Inscription'),
    ('Frais Reinscription', 'Frais Reinscription')
)
# Create your models here.


class ConfigurationFraisEleve(TimeStamp):
    frais = models.CharField(
        'Intitulé du frais', max_length=100, null=False, primary_key=True)
    periodePaiement = models.CharField(
        'Période de paiement', max_length=100, null=True)
    # obligatoire= models.BooleanField(verbose_name="Frais Obligatoire ?",default=True, null=False)
    montant = models.FloatField(null=True)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='config_frais_annee', null=True)

    def __str__(self):
        return f'{self.frais}'

    class Meta:
        db_table = 'Configuration_Frais_Eleve'


class ConfigEcolage(TimeStamp):
    identifiant = models.CharField(
        'Intitulé du frais', max_length=100, default="Frais mensuels")
    periodePaiement = models.CharField(
        'Période de paiement', max_length=100, null=False)
    obligatoire = models.BooleanField(
        verbose_name="Frais Obligatoire ?", default=True, null=False)
    montant = models.FloatField(null=False)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='ecolage_annnee')
    classe = models.OneToOneField(
        Classe, related_name='ecolage_classe', unique=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.typeFrais} => {self.montant}'

    class Meta:
        db_table = 'Ecolage'


class ConfigAutresFrais(TimeStamp):
    identifiant = models.CharField(
        max_length=100, null=False, primary_key=True)
    periodePaiement = models.CharField(
        'Période de paiement', max_length=100, null=False)
    obligatoire = models.BooleanField(
        verbose_name="Frais Obligatoire ?", default=True, null=False)
    montant = models.FloatField(null=False)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='autresFrais_annnee')
    classesSpeciales = models.ManyToManyField(
        Classe, related_name='autreFrais_classe')

    def __str__(self):
        return f'{self.identifiant} => {self.montant}'

    class Meta:
        db_table = 'Configuration_Autres_Frais'
        verbose_name_plural = 'Configuration_Autres_Frais'


class ConfigFraisInscriptionReinscription(TimeStamp):
    classe = models.OneToOneField(
        Classe, related_name='inscr_reinsc_classe', unique=True, default='', on_delete=models.DO_NOTHING)
    periodePaiement = models.CharField(
        'Période de paiement', max_length=100, default="", null=False)
    fraisInscription = models.IntegerField(null=False)
    fraisReinscription = models.IntegerField(null=False)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='config_inscReinsc_annee')

    def __str__(self):
        return f'{self.classe} => {self.fraisInscription}'

    class Meta:
        db_table = 'Config_Frais_Insc_Reinsc'


class ConfigDepenses(TimeStamp):
    identifiant = models.CharField(
        'Intitulé du frais', max_length=100, primary_key=True)
    periodePaiement = models.CharField(
        'Période de paiement', max_length=100, null=False)
    obligatoire = models.BooleanField(
        verbose_name="Frais Obligatoire ?", default=True, null=False)
    montant = models.FloatField(null=True)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='config_depense_annnee')
    caisseDeRetrait = models.CharField(
        'Caisse de retrait', max_length=100, null=True)

    def __str__(self):
        return f'{self.identifiant}'

    class Meta:
        db_table = 'Config_Depenses'


class ConfigurationSalaireEnseignant(TimeStamp):
    categorieEnseignant = models.CharField(
        "Catégorie d'employé :", max_length=30, choices=CATEGORIE_ENSEIGNANT, null=False)
    salaireDefini = models.FloatField('Salaire défini', null=False)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='config_salaireTeacher_annee')

    def __str__(self):
        return f'{self.categorie_enseignant} => {self.salaire_defini}'

    class Meta:
        db_table = 'Configuration_Salaire_Enseignant'


class PaiementInscriptionReinscription(TimeStamp):
    eleve = models.ForeignKey(
        Eleve, on_delete=models.DO_NOTHING, related_name='eleve_payant_insc_reinsc')
    classe = models.ForeignKey(
        Classe, related_name='classe_eleve_insc_reinsc', default='', on_delete=models.DO_NOTHING)
    typeFrais = models.ForeignKey(
        ConfigurationFraisEleve, on_delete=models.DO_NOTHING, default="", verbose_name='Type de frais à payer',
        related_name='InscReinsc_type_frais')

    montantFrais = models.FloatField(
        null=False, verbose_name='Montant Frais à payer')
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='annee_scolaire_insc_reinsc')

    def __str__(self):
        return f'{self.typeFrais} === {self.eleve}'

    class Meta:
        db_table = 'Paiement_Inscription_Reinscription'
        ordering = ['-cree_le']


class PaiementFraisMensuels(TimeStamp):
    eleve = models.ForeignKey(
        Eleve, on_delete=models.DO_NOTHING, related_name='eleve_payant_FM')
    classe = models.ForeignKey(
        Classe, related_name='classeEleve_payant_FM', default='', on_delete=models.DO_NOTHING)

    montantFrais = models.CharField(
        max_length=50, null=False, verbose_name='Montant Frais à payer')
    mois = models.CharField('Mois à payer', max_length=50,
                            null=True, blank=True)
    moisAsolver = models.CharField('Mois à solver', max_length=50,
                                   null=True, blank=True)
    montantApayer = models.FloatField('Montant à payer', null=False)
    montantDejaPaye = models.FloatField('Montant déjà payé',
                                        default=0, null=False)
    montantRestant = models.FloatField(
        'Montant restant', null=False)
    statut = models.CharField(max_length=250, blank=True)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='frais_mensuel_annee')

    def __str__(self):
        return f'{self.type_frais} => {self.montant_frais}'

    class Meta:
        db_table = 'Paiement_frais_Mensuels'
        ordering = ['-cree_le']


class PaiementAutresFrais(TimeStamp):
    eleve = models.ForeignKey(
        Eleve, on_delete=models.DO_NOTHING, related_name='eleve_payant_autreFrais')
    classe = models.ForeignKey(
        Classe, related_name='classeEleve_payant_autreFrais', default='', on_delete=models.DO_NOTHING)
    typeFrais = models.ForeignKey(
        ConfigurationFraisEleve, on_delete=models.DO_NOTHING, verbose_name='Type de frais à payer', related_name='type_frais')
    montantFrais = models.CharField(
        max_length=50, null=False, verbose_name='Montant Frais à payer')
    montantApayer = models.FloatField('Montant à payer', null=False)
    montantRestant = models.FloatField(
        'Montant restant', null=False)
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='autre_frais_annee')

    def __str__(self):
        return f'{self.type_frais} => {self.montant_frais}'

    class Meta:
        db_table = 'Paiement_Autres_frais'
        verbose_name_plural = 'frais'
        ordering = ['-cree_le']


class PaiementEveryFrais(TimeStamp):
    eleve = models.ForeignKey(
        Eleve, on_delete=models.DO_NOTHING, related_name='eleve_payant')
    classe = models.ForeignKey(
        Classe, related_name='classe_eleve', default='', on_delete=models.DO_NOTHING)
    typeFrais = models.ForeignKey(
        ConfigurationFraisEleve, on_delete=models.DO_NOTHING, verbose_name='Type de frais à payer', related_name='typeFrais')
    montantFrais = models.CharField(
        max_length=50, null=False, verbose_name='Montant Frais à payer')
    mois = models.CharField('Mois à payer', max_length=30,
                            null=True, blank=True)
    moisAsolver = models.CharField('Mois à solver', max_length=50,
                                   null=True, blank=True, default="")

    montantApayer = models.FloatField('Montant à payer', null=False)
    montantDejaPaye = models.FloatField('Montant déjà payé',
                                        default=0, null=False)
    montantRestant = models.FloatField(
        'Montant restant', null=False)
    statut = models.CharField(max_length=250, blank=True)

    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, default="", related_name='everyfrais_annee')

    def __str__(self):
        return f'{self.typeFrais} => {self.montantFrais}'

    class Meta:
        db_table = 'Paiement_Every_Frais'
        verbose_name_plural = 'Paiement_Every_Frais'


class PaiementSalaireEnseignant(TimeStamp):
    paiementNumero = models.AutoField('Paiement numéro =>', primary_key=True)

    nomEnseignant = models.ForeignKey(
        Enseignant, on_delete=models.DO_NOTHING, related_name="enseignant_a_payer", verbose_name="Nom de l'enseignant")
    moisPaiement = models.CharField(
        'Mois à payer', max_length=50, null=False, choices=MOIS)
    heuresEffectue = models.CharField('Heures effectuées',
                                      max_length=50, default='8h de cours enseignees', editable=False)
    montantApayer = models.FloatField(null=False)
    montantDejaPaye = models.FloatField('Montant Déjà payé',
                                        default=0, null=False, editable=False)
    montantRestant = models.FloatField(
        'Montant Restant à payer', null=False, editable=False)
    statut = models.BooleanField(
        blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='salaire_teacher_annee')

    def __str__(self):
        return f'Salaire enseignant => {self.type_de_paie} | Mois de: {self.mois_paiement}'

    class Meta:
        db_table = 'Paiement_Salaire_Enseignant'


class PaiementSalairePersonnel(TimeStamp):
    paiementNumero = models.AutoField('Paiement numéro =>', primary_key=True)
    nomPersonnel = models.ForeignKey(
        Personnel, on_delete=models.DO_NOTHING, verbose_name='Nom du personnel', related_name="personnel_a_payer")
    moisPaiement = models.CharField(
        'Mois à payer', max_length=50, null=False, choices=MOIS)
    # heures_effectuees= models.ForeignKey(HeuresEnseignant, )
    montantApayer = models.FloatField('Montant à payer', null=False)
    montantDejaPaye = models.FloatField('Montant déjà payé',
                                        default=0, null=False, editable=False)
    montantRestant = models.FloatField(
        'Montant Restant à payer', null=False, editable=False)
    statut = models.BooleanField(
        blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")
    AnneeScolaire = models.ForeignKey(
        AnneeScolaire, on_delete=models.DO_NOTHING, related_name='salaire_personnel_annee')

    def __str__(self):
        return f' Salaire de => {self.nom_personnel} | Mois de: {self.mois_paiement}'

    class Meta:
        db_table = 'Paiement_Salaire_Personnel'
