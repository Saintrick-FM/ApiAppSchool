from django.db import models

# Create your models here.


class TimeStamp(models.Model):

    cree_le = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name='créé_le')
    modifie_le = models.DateTimeField(
        'modifié_le', auto_now=True, editable=False)

    class Meta:
        abstract = True
