from django.db import models

CYCLE = [
    {'0': 'Garderie'},
    {'1': 'Prescolaire'},
    {'2': 'Primaire'},
    {'3': 'College'}
    # {'4': 'Lycée'},
]
PRESCOLAIRE = 'CP,P1,P2'
PRIMAIRE = 'CP,CE1,CE2,CM1,CM2'

COLLEGE = '6e,5e,4e,3e'
# LYCEE = '2nd,1ere,Terminale'
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


class Cycle(models.Model):
    prescolaire = models.CharField(default=CYCLE[0]["0"], max_length=250, null=False)
    primaire = models.CharField(default=CYCLE[1]["1"], max_length=250, null=False)
    college = models.CharField(default=CYCLE[2]["2"], max_length=250, null=False)
    # lycee = models.CharField(default=COLLEGE, null=False)


class Site(models.Model):
    numero = models.IntegerField(default=1, null=False)
    adresseSite = models.CharField(max_length=250, null=False)
    cycles = models.CharField(max_length=250)
    nombreCycles = models.IntegerField(default=2, null=False)
    nbreSalleGarderie = models.IntegerField(default=0, null=False)
    nbreSallePrimaire = models.IntegerField(default=6, null=False)
    nbreSalleCollege = models.IntegerField(default=4, null=False)

    def __str__(self):
        return "site {}".format(self.numero)


class GarderieSite1(models.Model):
    numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
    nbreSalles = models.IntegerField(default=2, null=False)
    contenance = models.IntegerField(null=False)


class CollegeSite1(models.Model):
    numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
    nbreSalles = models.IntegerField(default=8, null=False)
    salles6e = models.IntegerField(default=2, null=False)
    salles5e = models.IntegerField(default=2, null=False)
    salles4e = models.IntegerField(default=2, null=False)
    salles3e = models.IntegerField(default=2, null=False)

    contenance6e = models.IntegerField(null=False)
    contenance5e = models.IntegerField(null=False)
    contenance4e = models.IntegerField(null=False)
    contenance3e = models.IntegerField(null=False)
    matieres = models.TextField(default='{},{},{}'.format(MATIERE_LITTERAIRES[1][0], MATIERE_SCIENTIFIQUES[1][0],
                                                          AUTRES_MATIERES[1][0]))


class CollegeSite2(models.Model):
    nbreSalles = models.IntegerField(default=4, null=False)
    salles6e = models.IntegerField(default=1, null=False)
    salles5e = models.IntegerField(default=1, null=False)
    salles4e = models.IntegerField(default=1, null=False)
    salles3e = models.IntegerField(default=1, null=False)

    contenance6e = models.IntegerField(null=False)
    contenance5e = models.IntegerField(null=False)
    contenance4e = models.IntegerField(null=False)
    contenance3e = models.IntegerField(null=False)
    matieres = models.TextField(
        default='{},{},{}'.format(MATIERE_LITTERAIRES[1][0], MATIERE_SCIENTIFIQUES[1][0], AUTRES_MATIERES[1][0]))


class PrimaireSite1(models.Model):
    numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
    nbreSalles = models.IntegerField(default=11, null=False)
    sallesCP1 = models.IntegerField(default=2, null=False)
    sallesCP2 = models.IntegerField(default=2, null=False)
    sallesCE1 = models.IntegerField(default=2, null=False)
    sallesCE2 = models.IntegerField(default=2, null=False)
    sallesCM1 = models.IntegerField(default=2, null=False)
    sallesCM2 = models.IntegerField(default=1, null=False)

    contenanceCP1 = models.IntegerField(null=False)
    contenanceCP2 = models.IntegerField(null=False)
    contenanceCE1 = models.IntegerField(null=False)
    contenanceCE2 = models.IntegerField(null=False)
    contenanceCM1 = models.IntegerField(null=False)
    contenanceCM2 = models.IntegerField(null=False)
    matieres = models.TextField(
        default='{},{},{}'.format(MATIERE_LITTERAIRES[0][0], MATIERE_SCIENTIFIQUES[0][0], AUTRES_MATIERES[0][0]))


class PrimaireSite2(models.Model):
    nbreSalles = models.IntegerField(default=6, null=False)
    sallesCP1 = models.IntegerField(default=1, null=False)
    sallesCP2 = models.IntegerField(default=1, null=False)
    sallesCE1 = models.IntegerField(default=1, null=False)
    sallesCE2 = models.IntegerField(default=1, null=False)
    sallesCM1 = models.IntegerField(default=1, null=False)
    sallesCM2 = models.IntegerField(default=1, null=False)

    contenanceCP1 = models.IntegerField(null=False)
    contenanceCP2 = models.IntegerField(null=False)
    contenanceCE1 = models.IntegerField(default=1, null=False)
    contenanceCE2 = models.IntegerField(default=1, null=False)
    contenanceCM1 = models.IntegerField(default=1, null=False)
    contenanceCM2 = models.IntegerField(default=1, null=False)
    matieres = models.TextField(
        default='{}  --  {}  --  {}'.format(MATIERE_LITTERAIRES[0][0], MATIERE_SCIENTIFIQUES[0][0],
                                            AUTRES_MATIERES[0][0]))
