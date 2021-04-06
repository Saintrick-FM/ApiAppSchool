from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ConfigurationSalaireEnseignant)
admin.site.register(ConfigurationFraisEleve)
admin.site.register(PaiementFrais)
admin.site.register(PaiementSalaireEnseignant)
admin.site.register(PaiementSalairePersonnel)
