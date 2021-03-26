from django.shortcuts import render
from .models import Eleve
from rest_framework import serializers, viewsets


# Create your views here.


class EleveSerializer(serializers.HyperlinkedModelSerializer):
    classeEleve= serializers.ReadOnlyField(source='classEleve')
    class Meta:
        model = Eleve
        fields = ['url', 'nom', 'sexe', 'naissance', 'age', 'lieuNaiss', 'classeEleve', 'dateInscrit']


class EleveViewset(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
