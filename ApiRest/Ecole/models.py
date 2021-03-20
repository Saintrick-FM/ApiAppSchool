from django.db import models

CYCLE = {
    {'0': 'Garderie'},
    {'1': 'Prescolaire'},
    {'2': 'Primaire'},
    {'3': 'College'},
    # {'4': 'Lycée'},
}
PRESCOLAIRE = 'CP,P1,P2'
PRIMAIRE = 'CP,CE1,CE2,CM1,CM2'

COLLEGE = '6e,5e,4e,3e'
# LYCEE = '2nd,1ere,Terminale'
MATIERE_LITTERAIRES = [
    {'Primaire': 'Français,Histoire'},
    {'Collège': 'Français,Histoire,Géographie,Anglais'},
    # {'Lycee': 'Espagnol,Français,Philosophie,Anglais'}
]
MATIERE_SCIENTIFIQUES = [
    {'Primaire': 'Mathématiques,SVT,Mesures'},
    {'Collège': 'Mathématiques,SVT,Physique-Chimie'}
    # {'Lycee': 'Mathématiques,SVT,Physique-Chimie,Informatique'}
]
AUTRES_MATIERES = [
    {'Primaire': '...,Education_culturelle'},
    {'Collège': 'EPS,Informatique,Musique'}
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


class Site(models.Model):

    def affecteSite(self, site, cycle=None):
        if site == 'site1':
            if cycle == 'garderie':
                nbreSalles = models.IntegerField(default=2, null=False)
                contenance = models.IntegerField(null=False, max_length=5)

            elif cycle == 'primaire':
                nbreSalles = models.IntegerField(default=11, null=False)
                sallesCP1 = models.IntegerField(default=2, null=False, max_length=4)
                sallesCP2 = models.IntegerField(default=2, null=False, max_length=4)
                sallesCE1 = models.IntegerField(default=2, null=False, max_length=4)
                sallesCE2 = models.IntegerField(default=2, null=False, max_length=4)
                sallesCM1 = models.IntegerField(default=2, null=False, max_length=4)
                sallesCM2 = models.IntegerField(default=1, null=False, max_length=4)

                contenanceCP1 = models.IntegerField(null=False, max_length=4)
                contenanceCP2 = models.IntegerField(null=False, max_length=4)
                contenanceCE1 = models.IntegerField(null=False, max_length=4)
                contenanceCE2 = models.IntegerField(null=False, max_length=4)
                contenanceCM1 = models.IntegerField(null=False, max_length=4)
                contenanceCM2 = models.IntegerField(null=False, max_length=4)
                matieres = models.CharField(
                    default=MATIERE_LITTERAIRES[0] + MATIERE_SCIENTIFIQUES[0] + AUTRES_MATIERES[0])
            else:
                nbreSalles = models.IntegerField(default=8, null=False)
                salles6e = models.IntegerField(default=2, null=False, max_length=4)
                salles5e = models.IntegerField(default=2, null=False, max_length=4)
                salles4e = models.IntegerField(default=2, null=False, max_length=4)
                salles3e = models.IntegerField(default=2, null=False, max_length=4)

                contenance6e = models.IntegerField(null=False, max_length=4)
                contenance5e = models.IntegerField(null=False, max_length=4)
                contenance4e = models.IntegerField(null=False, max_length=4)
                contenance3e = models.IntegerField(null=False, max_length=4)
                matieres = models.CharField(
                    default=MATIERE_LITTERAIRES[1] + MATIERE_SCIENTIFIQUES[1] + AUTRES_MATIERES[1])


        else:
            if cycle == 'primaire':
                nbreSalles = models.IntegerField(default=6, null=False)
                sallesCP1 = models.IntegerField(default=1, null=False, max_length=4)
                sallesCP2 = models.IntegerField(default=1, null=False, max_length=4)
                sallesCE1 = models.IntegerField(default=1, null=False, max_length=4)
                sallesCE2 = models.IntegerField(default=1, null=False, max_length=4)
                sallesCM1 = models.IntegerField(default=1, null=False, max_length=4)
                sallesCM2 = models.IntegerField(default=1, null=False, max_length=4)

                contenanceCP1 = models.IntegerField(null=False, max_length=4)
                contenanceCP2 = models.IntegerField(null=False, max_length=4)
                contenanceCE1 = models.IntegerField(default=1, null=False, max_length=4)
                contenanceCE2 = models.IntegerField(default=1, null=False, max_length=4)
                contenanceCM1 = models.IntegerField(default=1, null=False, max_length=4)
                contenanceCM2 = models.IntegerField(default=1, null=False, max_length=4)
                matieres = models.CharField(
                    default=MATIERE_LITTERAIRES[0] + MATIERE_SCIENTIFIQUES[0] + AUTRES_MATIERES[0])
            elif cycle == 'collège':
                nbreSalles = models.IntegerField(default=4, null=False)
                salles6e = models.IntegerField(default=1, null=False, max_length=4)
                salles5e = models.IntegerField(default=1, null=False, max_length=4)
                salles4e = models.IntegerField(default=1, null=False, max_length=4)
                salles3e = models.IntegerField(default=1, null=False, max_length=4)

                contenance6e = models.IntegerField(null=False, max_length=4)
                contenance5e = models.IntegerField(null=False, max_length=4)
                contenance4e = models.IntegerField(null=False, max_length=4)
                contenance3e = models.IntegerField(null=False, max_length=4)
                matieres = models.CharField(
                    default=MATIERE_LITTERAIRES[1] + MATIERE_SCIENTIFIQUES[1] + AUTRES_MATIERES[1])
            else:
                pass


class Cycle(models.Model):
    prescolaire = models.CharField(default=PRESCOLAIRE, null=False)
    primaire = models.CharField(default=PRIMAIRE, null=False)
    college = models.CharField(default=COLLEGE, null=False)
    # lycee = models.CharField(default=COLLEGE, null=False)


class Site1(Site):
    Site.affecteSite(site='site1', cycle='garderie')
    Site.affecteSite(site='site1', cycle='primaire')
    Site.affecteSite(site='site1')


class Site2(Site):
    Site.affecteSite(site='...', cycle='primaire')
    Site.affecteSite(site='...', cycle='collège')