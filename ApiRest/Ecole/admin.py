from django.contrib import admin
from .models import Cycle, Ecole, Site, Classe, Matiere, Enseignant, AnneeScolaire

admin.site.register(Ecole)
admin.site.register(Cycle)
admin.site.register(Site)
admin.site.register(Matiere)
admin.site.register(Classe)
admin.site.register(AnneeScolaire)
admin.site.register(Enseignant)
