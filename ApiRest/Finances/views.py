from rest_framework import viewsets
from .models import *
from .serializer import *
# Create your views here. ConfigFraisEleve, ConfigSalaireEnseignant, ConfigSalairePersonnel, PaiementFrais,


class ConfigFraisEleveViewset(viewsets.ModelViewSet):
    queryset = ConfigFraisEleve.objects.all()
    serializer_class = ConfigFraisEleveSerializer


class ConfigSalaireEnseignantViewset(viewsets.ModelViewSet):
    queryset = ConfigSalaireEnseignant.objects.all()
    serializer_class = ConfigSalaireEnseignantSerializer
