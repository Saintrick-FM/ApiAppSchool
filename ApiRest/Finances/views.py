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


class PaiementFraisMensuelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementFraisMensuels
        fields = '__all__'


class PaiementSalaireEnseignantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaiementSalaireEnseignant
        fields = '__all__'


class PaiementSalairePersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaiementSalairePersonnel
        fields = '__all__'


class PaiementAutresFraisSerializer(serializers.ModelSerializer):
    class Meta:
        model= PaiementAutresFrais
        fields= "__all__"


class ConfigFraisEleveViewset(viewsets.ModelViewSet):
    queryset = ConfigurationFraisEleve.objects.all()
    serializer_class = ConfigFraisEleveSerializer


class ConfigFraisInscriptionReinscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigFraisInscriptionReinscription
        fields = '__all__'


class ConfigFraisInscriptionReinscriptionViewset(viewsets.ModelViewSet):
    queryset = ConfigFraisInscriptionReinscription.objects.all()
    serializer_class = ConfigFraisInscriptionReinscriptionSerializer


class ConfigSalaireEnseignantViewset(viewsets.ModelViewSet):
    queryset = ConfigurationSalaireEnseignant.objects.all()
    serializer_class = ConfigSalaireEnseignantSerializer


class PaiementFraisMensuelsViewset(viewsets.ModelViewSet):
    serializer_class = PaiementFraisMensuelsSerializer

    def get_queryset(self):
        queryset = PaiementFraisMensuels.objects.all()
        eleveId = self.request.query_params.get("id", None)
        annee_scolaire = self.request.query_params.get("annee_scolaire", None)
        classe = self.request.query_params.get("classe", None)
        if annee_scolaire is not None and eleveId is not None:
            queryset = queryset.filter(anneeAcademique=annee_scolaire, eleve__eleveNumber=eleveId)
        if annee_scolaire is not None and classe is not None:
            queryset = queryset.filter(anneeAcademique=annee_scolaire, classe__identifiant=classe)

        # return queryset.filter(anneeAcademique=annee_scolaire)
        return queryset


class PaiementAutresFraisViewset(viewsets.ModelViewSet):
    serializer_class = PaiementAutresFraisSerializer

    def get_queryset(self):
        queryset = PaiementAutresFrais.objects.all()
        eleveId = self.request.query_params.get("id", None)
        annee_scolaire = self.request.query_params.get("annee_scolaire", None)
        type_frais = self.request.query_params.get("type_frais", None)
        if annee_scolaire is not None and eleveId is not None:
            queryset = queryset.filter(anneeAcademique=annee_scolaire, eleve__eleveNumber=eleveId)
        if annee_scolaire is not None and type_frais is not None:
            queryset = queryset.filter(anneeAcademique=annee_scolaire, typeFrais__frais=type_frais)

        # return queryset.filter(anneeAcademique=annee_scolaire)
        return queryset

class PaiementInscriptionReinscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= PaiementInscriptionReinscription
        fields= "__all__"


class PaiementInscriptionReinscriptionViewset(viewsets.ModelViewSet):
    serializer_class = PaiementInscriptionReinscriptionSerializer

    def get_queryset(self):
        queryset = PaiementInscriptionReinscription.objects.all()
        anneeScolaire = self.request.query_params.get("annee_scolaire" ,None)
        classe = self.request.query_params.get("classe", None)
        if anneeScolaire is not None:
            queryset = queryset.filter(anneeAcademique=anneeScolaire)
            if classe is not None:
                queryset = queryset.filter(classe=classe)
        return queryset
