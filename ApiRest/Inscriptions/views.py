from ApiRest.Classe.models import Classe
from .models import Eleve
from rest_framework import serializers, viewsets


# Create your views here.

class EleveSerializer(serializers.HyperlinkedModelSerializer):
    classe= serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())

    class Meta:
        model = Eleve
        fields = ['url', 'eleveNumber', 'nom', 'sexe', 'naissance', 'age', 'lieuNaiss', 'classe', 'dateInscrit']
        read_only_fields= ['classe']


class EleveViewset(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
