from django.db import models

CYCLE = (
    ('Garderie', 'Garderie'),
    ('Prescolaire', 'Prescolaire'),
    ('Primaire', 'Primaire'),
    ('College', 'College')

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
    ('Marie', 'Marié(e)'),
    ('Divorce', 'Divorcé(e)'),
    ('Fiance', 'Fiancé(e)'),
    ('Veuf', 'Veuf(ve)'),
    ('Celibataire', 'Célibataire')

)

# LYCEE = '2nd,1ere,Terminale'
GROUPE_MATIERE = (
    ('MATIERE_LITTERAIRES', 'Matières litteraires'),
    ('MATIERE_SCIENTIFIQUES', 'Matières scientifiques'),
    ('AUTRES_MATIERES', 'Autres matières')
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

# Create your models here.


class Ecole(models.Model):
    nom = models.CharField(max_length=200, null=False)
    nbreSites = models.IntegerField(null=False, default=2)
    pays = models.CharField(max_length=100, null=False)
    ville = models.CharField(max_length=200, null=False)
    adresse = models.CharField(max_length=200, null=False)
    telephone = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=True, blank=True)
    siteInternet = models.CharField(null=True, max_length=200)
    prefixmatricule = models.CharField(max_length=200, null=False)

    def __str__(self):
        return 'Ecole {}'.format(self.nom)


class Site(models.Model):
    numero = models.AutoField(primary_key=True)
    adresse_site = models.CharField('Adresse site', max_length=250, null=False)
    # cycles = models.CharField(max_length=250)
    nombre_cycles = models.IntegerField(
        'Nombre de cycles', default=2, null=False)
    nbre_salle_garderie = models.IntegerField(
        'Nbre de Salle en Garderie',  default=0, null=False)
    nbre_salle_primaire = models.IntegerField(
        'Nbre de Salle au Primaire', default=6, null=False)
    nbre_salle_college = models.IntegerField(
        'Nbre de Salle au Collège', default=4, null=False)

    def __str__(self):
        return "site {}".format(self.numero)


class Cycle(models.Model):
    nom_cycle = models.CharField(
        choices=CYCLE, default=CYCLE[0], primary_key=True, max_length=50)
    # numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
    # classes = models.ManyToManyField(Classe, related_name='classe_cycle')
    nbreSalles = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return self.nom_cycle


class Classe(models.Model):
    identifiant = models.CharField(
        primary_key=True, choices=IDENTIFIANT_CLASSE, max_length=50)
    reference_site = models.ManyToManyField(
        Site, related_name='classe_site', default='', verbose_name='Site n°:')
    heures_cours = models.CharField(default="7h30-13h", max_length=100)
    # nbreEleves = models.IntegerField(null=False)
    nbre_salles = models.IntegerField(default=1, null=False)
    contenance = models.IntegerField(null=False)
    total_filles = models.IntegerField(null=True, editable=False)
    total_garcons = models.IntegerField(null=True, editable=False)
    # matieresEnseigne = models.ManyToManyField(
    #     Matiere, related_name='classe_matiere')
    redoublants = models.IntegerField(default=0, null=True, editable=False)
    nouveaux = models.IntegerField(default=0, null=True, editable=False)
    elevesVenuDailleurs = models.IntegerField(
        default=0, null=True, editable=False)
    inscrits = models.IntegerField(null=True, editable=False)
    # enseignants_affecte = models.ManyToManyField(
    #     Enseignant, related_name='classe_enseignant')
    scolarite = models.CharField(
        help_text="Frais à payer mensuellement Eg: 8000F", null=False, max_length=50)
    cycle = models.ForeignKey(
        Cycle, on_delete=models.CASCADE, related_name='classe_cycle')

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class Matiere(models.Model):
    # attention francy il faut que tu assignes la clé primaire à ce champ.
    nom_matiere = models.CharField(
        max_length=200, primary_key=True, verbose_name='nom de la matière')
    code_matiere = models.CharField(max_length=200, null=False, unique=True)
    enseigne_en_groupe = models.BooleanField(default=False, null=False)
    matiere_de_base = models.BooleanField(default=False, null=False)
    seance_par_semaine = models.IntegerField(null=False)
    coefficient = models.IntegerField(null=False)
    groupe_matiere = models.CharField(
        max_length=100, choices=GROUPE_MATIERE, default='')
    classe_associe = models.ManyToManyField(
        Classe, related_name='matiere_de_la_classe', default='')

    def __str__(self):
        return self.nom_matiere

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
    situation_sociale = models.CharField(max_length=50, choices=STATUT_SOCIAL)
    nationalite = models.CharField(
        max_length=255, default='Congolaise', null=False)
    adresse = models.CharField(max_length=255, null=False)
    telephone = models.CharField(max_length=15, null=False, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    date_d_embauche = models.DateField(null=False)
    matiere_enseigne = models.ManyToManyField(
        Matiere, default='', related_name='enseignant_matieres', verbose_name='matière(s) enseignée(s)')
    classes_occupees = models.ManyToManyField(
        Classe, related_name='enseignant_classes', verbose_name="classe(s) d'enseignement")

    mode_paiement = models.CharField(
        'Mode de paiement', max_length=100, choices=MODE_PAIEMENT, null=False, default=MODE_PAIEMENT[0])
    intitule_du_compte = models.CharField(
        max_length=250, unique=True, blank=True, help_text="Ecrire le nom du compte bancaire de l'enseignant", null=True)
    numero_du_compte_bancaire = models.CharField(
        max_length=250, unique=True, blank=True, null=True)
    numero_cnss = models.CharField('mode de paiement',
                                   max_length=100, unique=True, blank=True, null=True)
    cree_le = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='créé_le')
    modifie_at = models.DateTimeField(
        'modifié_le', auto_now=True, editable=False)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-cree_le']
