from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import ConfigSalairePersonnel, Personnel

# Create your views here.


class ConfigSalairePersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigSalairePersonnel
        fields = '__all__'


class PersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'


class ConfigSalairePersonnelViewset(viewsets.ModelViewset):
    queryset = ConfigSalairePersonnel.objects.all()
    serializer_class = ConfigSalairePersonnelSerializer


class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
