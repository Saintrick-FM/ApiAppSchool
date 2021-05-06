import os

from ApiAppSchool.settings import BASE_DIR
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import api_view

from .models import Ecole, Site, Classe, Matiere, Enseignant
from rest_framework import permissions
from rest_framework.response import Response


class EcoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ecole
        fields = '__all__'


class EcoleViewSet(viewsets.ModelViewSet):
    queryset = Ecole.objects.all()
    serializer_class = EcoleSerializer


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'


class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'


class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer


class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'


class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer
    # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def PhotoView(request):
    photos = None
    if request.method == 'GET':
        path = os.path.join(BASE_DIR, 'photos.json')
        with open(path, 'r') as photo:
            photos = photo.read()

    return Response(photos, status=201)
