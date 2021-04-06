from rest_framework import serializers
from .models import *


class ConfigFraisEleveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigFraisEleve
        fields = '__all__'


class ConfigSalaireEnseignantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigSalaireEnseignant
        fields = ['categorie_enseignant', 'salaire_defini']


class ConfigSalairePersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigSalairePersonnel
        fields = '__all__'


class PaiementFraisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaiementFrais
        fields = '__all__'


class PaiementSalaireEnseignantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaiementSalaireEnseignant
        fields = '__all__'


class PaiementSalairePersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaiementSalairePersonnel
        fields = '__all__'


class
