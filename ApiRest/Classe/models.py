from django.db import models
from ApiRest.Ecole import models as modelEcole


# Create your models here.


class AbstractClasse(models.Model):
    referenceSite = models.ForeignKey(modelEcole.Site, on_delete=models.CASCADE)
    heuresCours = models.CharField(default="7h30-13h", max_length=100)
    nbreEleves = models.IntegerField(null=False)
    nbreSalles = models.IntegerField(default=1, null=False)
    contenance = models.IntegerField(null=False)
    totalFilles = models.IntegerField(null=False)
    totalGarcons = models.IntegerField(null=False)
    matieresEnseigne = models.TextField(max_length=800)
    redoublants = models.IntegerField(default=0, null=False)
    nouveaux = models.IntegerField(default=0, null=False)
    elevesVenuDailleurs = models.IntegerField(default=0, null=False)
    inscrits = models.IntegerField(null=False)

    class Meta:
        abstract = True


class Classe(AbstractClasse, models.Model):
    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class Creche(models.Model):
    identifiant = models.CharField(default='Crèche', max_length=50)
    nbreEleves = models.IntegerField(null=False)
    nbreSalles = models.IntegerField(default=1, null=False)
    contenance = models.IntegerField(null=False)
    totalFilles = models.IntegerField(null=False)
    totalGarcons = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Crèche'

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class CP1(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CP1', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class CP2(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CP2', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class CE1(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CE1', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class CE2(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CE2', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class CM1(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CM1', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class CM2(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CM2', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class Sixieme(AbstractClasse, models.Model):
    identifiant = models.CharField(default='6e', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)

    class Meta:
        verbose_name = '6e'


class Cinquieme(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CP2', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class Quatrieme(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CP2', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)


class Troisieme(AbstractClasse, models.Model):
    identifiant = models.CharField(default='CP2', max_length=50)

    def __str__(self):
        return 'Classe {}'.format(self.identifiant)

