from rest_framework import viewsets
from rest_framework import serializers
from .models import *


class ConfigFraisEleveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationFraisEleve
        fields = '__all__'


class ConfigSalaireEnseignantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfigurationSalaireEnseignant
        fields = ['categorie_enseignant', 'salaire_defini']


# class ConfigSalairePersonnelSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ConfigurationSalairePersonnel
#         fields = '__all__'


class PaiementFraisSerializer(serializers.ModelSerializer):
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


class ConfigFraisEleveViewset(viewsets.ModelViewSet):
    queryset = ConfigurationFraisEleve.objects.all()
    serializer_class = ConfigFraisEleveSerializer


class ConfigSalaireEnseignantViewset(viewsets.ModelViewSet):
    queryset = ConfigurationSalaireEnseignant.objects.all()
    serializer_class = ConfigSalaireEnseignantSerializer


class PaiementFraisViewset(viewsets.ModelViewSet):
    serializer_class = PaiementFraisSerializer

    def get_queryset(self):
        queryset = PaiementFrais.objects.all()
        eleveId = self.request.query_params.get("id", None)
        if eleveId is not None:
            queryset = queryset.filter(eleve__eleveNumber=eleveId)
        return queryset

