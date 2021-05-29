from datetime import date
from ApiRest.Ecole.models import Classe
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Eleve
from rest_framework import serializers, viewsets, status
from rest_framework import permissions


# Create your views here.

class EleveSerializer(serializers.ModelSerializer):
    # classe = serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())

    class Meta:
        model = Eleve
        fields = '__all__'
        # read_only_fields = ['sexe', 'age']


class EleveViewset(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
    #permission_classes = [permissions.IsAuthenticated]


"""
    now = date.today()
    anneeActuelle = int(now.strftime("%Y"))

    ageCount = lambda today, yearBirth: f'{today - yearBirth} ans'
    extractYear = lambda naissance="11-05-1995": int(naissance[-4] + naissance[-3] + naissance[-2] + naissance[-1])

    def verifyNaissance(self, naissance) :
        annee= naissance[-4] + naissance[-3] + naissance[-2] + naissance[-1]
        if annee.isnumeric():
            print(f"l'année de naissance tapée est {annee}")
            return True
        else:
            print(f"l'année de naissance tapée est {annee}")
            return False

"""
