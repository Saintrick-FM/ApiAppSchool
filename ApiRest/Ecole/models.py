from django.db import models
from datetime import date

CYCLE = (
    ('Garderie', 'Garderie'),
    ('Prescolaire', 'Prescolaire'),
    ('Primaire', 'Primaire'),
    ('College', 'College')

)

PLURIPROF = (
    ('Non', 'Non'),
    ('Oui', 'Oui'),
)
IDENTIFIANT_CLASSE = (
    ('Crèche', 'Crèche'),
    ('P1', 'P1'),
    ('P2', 'P2'),
    ('P3', 'P3'),
    ('CP1', 'CP1'),
    ('CP2', 'CP2'),
    ('CE1', 'CE1'),
    ('CE2', 'CE2'),
    ('CM1', 'CM1'),
    ('CM2', 'CM2'),
    ('6e', '6e'),
    ('5e', '5e'),
    ('4e', '4e'),
    ('3e', '3e')

)

CIVILITE = (
    ('Masculin', 'Masculin'),
    ('Feminin', 'Feminin')
)


MODE_PAIEMENT = (
    ('Manuel', 'Manuel'),
    ('Virement', 'Virement Bancaire')
)

STATUT_SOCIAL = (
    ('Marié(e)', 'Marié(e)'),
    ('Divorcé(e)', 'Divorcé(e)'),
    ('Fiancé(e)', 'Fiancé(e)'),
    ('Veuf(ve)', 'Veuf(ve)'),
    ('Célibataire', 'Célibataire')

)

# LYCEE = '2nd,1ere,Terminale'
GROUPE_MATIERE = (
    ('MATIERE_LITTERAIRES', 'Matières litteraires'),
    ('MATIERE_SCIENTIFIQUES', 'Matières scientifiques'),
    ('AUTRES_MATIERES', 'Autres matières')
)
MATIERE_DE_BASE = (
    ('Non', 'Non'),
    ('Oui', 'Oui'),
)
MATIERE_LITTERAIRES = [
    ['Français, Histoire'],
    ['Français, Histoire, Géographie, Anglais']
    # {'Lycee': 'Espagnol,Français,Philosophie,Anglais'}
]
MATIERE_SCIENTIFIQUES = [
    [' Mathématiques, SVT, Mesures'],
    [' Mathématiques, SVT, Physique-Chimie']
    # {'Lycee': 'Mathématiques,SVT,Physique-Chimie,Informatique'}
]
AUTRES_MATIERES = [
    [' Education_culturelle, ...'],
    [' EPS, Informatique, Musique']
    # {'Lycee': 'EPS, Informatique'}
]

CATEGORIE_ENSEIGNANT = (
    ('Primaire', 'Primaire'),
    ('College', 'College'),
    ('Maternelle', 'Maternelle')
)

now = date.today()


def anneeAcademique(annee=now):
    return f'{annee.strftime("%Y")}-{(int(annee.strftime("%Y")) + 1)}'
# Create your models here.


class Ecole(models.Model):
    nom = models.CharField(max_length=200, null=False)
    nbreSites = models.IntegerField('Nbre de sites', null=False, default=2)
    pays = models.CharField(max_length=100, null=False)
    ville = models.CharField(max_length=200, null=False)
    adresse = models.CharField(max_length=200, null=False)
    telephone = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=True, blank=True)
    siteInternet = models.CharField('Site internet', null=True, max_length=200)
    prefixmatricule = models.CharField(
        'Préfix matricule', max_length=200, null=False)

    def __str__(self):
        return 'Ecole {}'.format(self.nom)


class Site(models.Model):
    numero = models.AutoField(primary_key=True)
    adresse_site = models.CharField('Adresse site', max_length=250, null=False)
    # cycles = models.CharField(max_length=250)
    nombreCycles = models.IntegerField('Nbre de salles au primaire,',
                                       'Nombre de cycles', default=2, null=False)
    nbreSalleGarderie = models.IntegerField('Nbre de salles en garderie',
                                            'Nbre de Salle en Garderie',  default=0, null=False)
    nbreSallePrimaire = models.IntegerField('Nbre de salles au primaire',
                                            'Nbre de Salle au Primaire', default=6, null=False)
    nbreSalleCollege = models.IntegerField('Nbre de salles au collège',
                                           'Nbre de Salle au Collège', default=4, null=False)

    def __str__(self):
        return "site {}".format(self.numero)


class Cycle(models.Model):
    nomCycle = models.CharField('Nom du cycle',
                                choices=CYCLE, default=CYCLE[0], primary_key=True, max_length=50)
    # numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
    # classes = models.ManyToManyField(Classe, related_name='classe_cycle')
    nbreSalles = models.IntegerField(
        'Total de salles', editable=False, null=True)

    def __str__(self):
        return self.nomCycle


class Classe(models.Model):

    identifiant = models.CharField(
        primary_key=True, choices=IDENTIFIANT_CLASSE, max_length=50)
    referenceSite = models.ManyToManyField(
        Site, related_name='classe_site', default='', verbose_name='Site n°:')
    heuresCours = models.CharField(
        'Heures de cours', default="7h30-13h", max_length=100)
    # nbreEleves = models.IntegerField(null=False)
    nbreSalles = models.IntegerField('Nbre de salles', default=1, null=False)
    contenance = models.IntegerField(null=False)
    totalFilles = models.IntegerField(
        'Total des filles', null=True, editable=False)
    totalGarcons = models.IntegerField(
        'Total des garçons', null=True, editable=False)
    # matieresEnseigne = models.ManyToManyField(
    #     Matiere, related_name='classe_matiere')
    redoublants = models.IntegerField(default=0, null=True, editable=False)
    nouveaux = models.IntegerField(default=0, null=True, editable=False)
    elevesVenuDailleurs = models.IntegerField("Eleves venus d'ailleurs",
                                              default=0, null=True, editable=False)
    inscrits = models.IntegerField(null=True, editable=False)
    # enseignants_affecte = models.ManyToManyField(
    #     Enseignant, related_name='classe_enseignant')
    scolarite = models.CharField(
        help_text="Frais à payer mensuellement Eg: 8000F", null=False, max_length=50)
    cycle = models.ForeignKey(
        Cycle, on_delete=models.CASCADE, related_name='classe_cycle')
    anneeAcademique = models.CharField(
        'Année académique :', max_length=50, default=anneeAcademique, editable=False)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class Matiere(models.Model):
    # attention francy il faut que tu assignes la clé primaire à ce champ.
    nomMatiere = models.CharField('nom de la matière',  primary_key=True,
                                  max_length=200)
    codeMatiere = models.CharField('Code de la matière',
                                   max_length=200, blank=True, null=True, default='')
    pluriProf = models.CharField('Enseignée par plusieurs ?', max_length=20,
                                 choices=PLURIPROF, default=PLURIPROF[0], null=False)
    matiereDeBase = models.CharField('Matiere de Base ?', max_length=50, choices=MATIERE_DE_BASE,
                                     null=True)
    seanceParSemaine = models.IntegerField('Nbre de Séances/semaine', default=0,
                                           null=False)
    coefficient = models.IntegerField(null=False, default=0)
    groupeMatiere = models.CharField('Groupe Matière',
                                     max_length=100, choices=GROUPE_MATIERE, blank=True, default='')
    classAssocie = models.ManyToManyField(
        Classe, related_name='matiere_de_la_classe')

    def __str__(self):
        return self.nomMatiere

    def get_asbolute_url(self):
        return f'/{self.nomMatiere}/'

    class Meta:
        db_table = 'Matière'


class Enseignant(models.Model):
    enseignant_numero = models.AutoField('N°:',
                                         primary_key=True, auto_created=True, db_column='n°')
    nom = models.CharField(unique=True, max_length=255,
                           help_text="Tapez tous les noms et prénoms", null=False)
    civilite = models.CharField(
        choices=CIVILITE, max_length=255, default='', null=False)
    date_naissance = models.CharField(max_length=50, help_text='Tappez juste la date de Naissance Eg: 11-Mai-1995',
                                      null=False)
    lieu_naissance = models.CharField(
                    max_length=50, default='Brazzaville', db_column="lieuDeNaissance", blank=True)
    situationSociale = models.CharField('Situation sociale',max_length=50, choices=STATUT_SOCIAL)
    nationalite = models.CharField(
                    max_length=255, default='Congolaise', null=False)
    adresse = models.CharField(max_length=255, null=False)
    telephone = models.CharField(max_length=15, null=False, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    matiereEnseigne = models.ManyToManyField(
                    Matiere, default='', related_name='enseignant_matieres', verbose_name='Matière(s) enseignée(s)')
    classesOccupees = models.ManyToManyField(
                    Classe, related_name='enseignant_classes', verbose_name="Classe(s) à enseigner")
    modePaiement = models.CharField(
                    'Mode de paiement', max_length=100, choices=MODE_PAIEMENT, null=False, default=MODE_PAIEMENT[0])
    intituleCompte = models.CharField(
                    max_length=250,  blank=True, help_text="Ecrire le nom du compte bancaire de l'enseignant", null=True)
    numeroCompteBancaire = models.CharField("Numéro compte bancaire",
                    max_length=250,  blank=True, null=True)
    numeroCnss = models.CharField('Numéro CNSS',
                                   max_length=100,  blank=True, null=True)
    enseigneAu = models.CharField(
        "Enseigne au cycle :", max_length=30, default=CATEGORIE_ENSEIGNANT[1], choices=CATEGORIE_ENSEIGNANT, null=False)
    dateEmbauche = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='créé_le')
    modifieLe = models.DateTimeField(
        'modifié_le', auto_now=True, editable=False)

    def __str__(self):
        return self.nom

    def get_asbolute_url(self):
        return str(self.nom)

    class Meta:
        ordering = ['-dateEmbauche']
