from rest_framework import viewsets
from rest_framework import serializers
from .models import Ecole, Site


class EcoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ecole
        fields = '__all__'


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    classe
    class Meta:
        model = Site
        fields = '__all__'


class EcoleViewSet(viewsets.ModelViewSet):
    queryset = Ecole.objects.all()
    serializer_class = EcoleSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
