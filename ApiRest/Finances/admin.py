from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ConfigurationSalaireEnseignant)
admin.site.register(ConfigurationFraisEleve)
admin.site.register(PaiementSalaireEnseignant)
admin.site.register(PaiementFraisMensuels)
admin.site.register(PaiementAutresFrais)
admin.site.register(PaiementSalairePersonnel)
admin.site.register(ConfigFraisInscriptionReinscription)
admin.site.register(PaiementInscriptionReinscription)
