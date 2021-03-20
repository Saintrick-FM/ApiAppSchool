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
    ['Français,Histoire'],
    ['Français,Histoire,Géographie,Anglais']
    # {'Lycee': 'Espagnol,Français,Philosophie,Anglais'}
]
MATIERE_SCIENTIFIQUES = [
    ['Mathématiques,SVT,Mesures'],
    ['Mathématiques,SVT,Physique-Chimie']
    # {'Lycee': 'Mathématiques,SVT,Physique-Chimie,Informatique'}
]
AUTRES_MATIERES = [
    ['...,Education_culturelle'],
    ['EPS,Informatique,Musique']
    # {'Lycee': 'EPS, Informatique'}
]


# Create your models here.

class Site(models.Model):
    numero = models.IntegerField(default=1, null=False)
    adresseSite = models.CharField(max_length=250, null=False)
    cycles = models.CharField(max_length=250)
    nombreCycles = models.IntegerField(default=2, null=False)
    nbreSalleGarderie = models.IntegerField(default=0, null=False)
    nbreSallePrimaire = models.IntegerField(default=6, null=False)
    nbreSalleCollege = models.IntegerField(default=4, null=False)

#
# class Classe(models.Model):
#     referenceSite = models.ForeignKey(Site, on_delete=models.CASCADE())
#     identifiant = models.CharField(max_length=50)
#     heuresCours = models.CharField(default="7h30-13h", max_length=100)
#     nbreEleves = models.IntegerField(null=False)
#     nbreSalles = models.IntegerField(default=1, null=False)
#     contenance = models.IntegerField(null=False)
#     totalFilles = models.IntegerField(null=False)
#     totalGarcons = models.IntegerField(null=False)
#     matieresEnseigne = models.TextField(max_length=800)
#     redoublants = models.IntegerField(default=0, null=False)
#     nouveaux = models.IntegerField(default=0, null=False)
#     elevesVenuDailleurs = models.IntegerField(default=0, null=False)
#     inscrits = models.IntegerField(null=False)


class AffectationSite:
    def __init__(self, site, cycle=None):
        self.site = site
        self.cycle = cycle
        print("la valeur de l'attribut site => {}".format(self.site))

        if self.site == 'site1':

            if self.cycle == 'garderie':

                class GarderieSite1(models.Model):
                    self.numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
                    self.nbreSalles = models.IntegerField(default=2, null=False)
                    contenance = models.IntegerField(null=False)

            elif self.cycle == 'primaire':
                print("On est dans le if self.cycle='primaire' du Site 2")

                class PrimaireSite1(models.Model):
                    self.numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
                    self.nbreSalles = models.IntegerField(default=11, null=False)
                    self.sallesCP1 = models.IntegerField(default=2, null=False)
                    self.sallesCP2 = models.IntegerField(default=2, null=False)
                    self.sallesCE1 = models.IntegerField(default=2, null=False)
                    self.sallesCE2 = models.IntegerField(default=2, null=False)
                    self.sallesCM1 = models.IntegerField(default=2, null=False)
                    self.sallesCM2 = models.IntegerField(default=1, null=False)

                    self.contenanceCP1 = models.IntegerField(null=False)
                    self.contenanceCP2 = models.IntegerField(null=False)
                    self.contenanceCE1 = models.IntegerField(null=False)
                    self.contenanceCE2 = models.IntegerField(null=False)
                    self.contenanceCM1 = models.IntegerField(null=False)
                    self.contenanceCM2 = models.IntegerField(null=False)
                    self.matieres = models.CharField(
                        default='{},{},{}'.format(MATIERE_LITTERAIRES[0], MATIERE_SCIENTIFIQUES[0], AUTRES_MATIERES[0]))
            else:

                class CollegeSite1(models.Model):
                    self.numeroSite = models.ForeignKey(Site, on_delete=models.CASCADE)
                    self.nbreSalles = models.IntegerField(default=8, null=False)
                    self.salles6e = models.IntegerField(default=2, null=False)
                    self.salles5e = models.IntegerField(default=2, null=False)
                    self.salles4e = models.IntegerField(default=2, null=False)
                    self.salles3e = models.IntegerField(default=2, null=False)

                    self.contenance6e = models.IntegerField(null=False)
                    self.contenance5e = models.IntegerField(null=False)
                    self.contenance4e = models.IntegerField(null=False)
                    self.contenance3e = models.IntegerField(null=False)
                    self.matieres = models.CharField(

                        default='{},{},{}'.format(MATIERE_LITTERAIRES[1], MATIERE_SCIENTIFIQUES[1], AUTRES_MATIERES[1]))

        else:
            if self.cycle == 'primaire':

                class PrimaireSite2(models.Model):
                    print("On est dans le if self.cycle='primaire' du Site 2")
                    self.nbreSalles = models.IntegerField(default=6, null=False)
                    self.sallesCP1 = models.IntegerField(default=1, null=False)
                    self.sallesCP2 = models.IntegerField(default=1, null=False)
                    self.sallesCE1 = models.IntegerField(default=1, null=False)
                    self.sallesCE2 = models.IntegerField(default=1, null=False)
                    self.sallesCM1 = models.IntegerField(default=1, null=False)
                    self.sallesCM2 = models.IntegerField(default=1, null=False)

                    self.contenanceCP1 = models.IntegerField(null=False)
                    self.contenanceCP2 = models.IntegerField(null=False)
                    self.contenanceCE1 = models.IntegerField(default=1, null=False)
                    self.contenanceCE2 = models.IntegerField(default=1, null=False)
                    self.contenanceCM1 = models.IntegerField(default=1, null=False)
                    self.contenanceCM2 = models.IntegerField(default=1, null=False)
                    self.matieres = models.CharField(
                        default='{},{},{}'.format(MATIERE_LITTERAIRES[0], MATIERE_SCIENTIFIQUES[0], AUTRES_MATIERES[0]))
            elif cycle == 'collège':

                class CollegeSite2(models.Model):
                    self.nbreSalles = models.IntegerField(default=4, null=False)
                    self.salles6e = models.IntegerField(default=1, null=False)
                    self.salles5e = models.IntegerField(default=1, null=False)
                    self.salles4e = models.IntegerField(default=1, null=False)
                    self.salles3e = models.IntegerField(default=1, null=False)

                    self.contenance6e = models.IntegerField(null=False)
                    self.contenance5e = models.IntegerField(null=False)
                    self.contenance4e = models.IntegerField(null=False)
                    self.contenance3e = models.IntegerField(null=False)
                    self.matieres = models.CharField(
                        default='{},{},{}'.format(MATIERE_LITTERAIRES[1], MATIERE_SCIENTIFIQUES[1], AUTRES_MATIERES[1]))
            else:
                pass


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


class Cycle(models.Model):
    prescolaire = models.CharField(default=CYCLE[0], max_length=250, null=False)
    primaire = models.CharField(default=CYCLE[1], max_length=250, null=False)
    college = models.CharField(default=CYCLE[2], max_length=250, null=False)
    # lycee = models.CharField(default=COLLEGE, null=False)


siteA = AffectationSite(site='site1', cycle='garderie')
siteB = AffectationSite(site='site1', cycle='primaire')
siteC = AffectationSite(site='site1')

siteD = AffectationSite(site='site2', cycle='primaire')
siteE = AffectationSite(site='', cycle='collège')

