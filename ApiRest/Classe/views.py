from rest_framework import serializers, viewsets
from .models import Classe
from ApiRest.Inscriptions.models import Eleve

# Create your views here.


class ClasseSerializer(serializers.ModelSerializer):
    # => marche avec le model serializer
    eleve = serializers.StringRelatedField(many=True)
    #referenceSite= serializers.HyperlinkedRelatedField(view_name='')

    class Meta:
        model = Classe
        fields = ['url', 'identifiant', 'totalFilles', 'totalGarcons', 'referenceSite', 'heuresCours', 'contenance',
                  'matieresEnseigne', 'inscrits', 'scolarite', 'eleve']


class ClassViewset(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
