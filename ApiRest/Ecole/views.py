import os

from ApiAppSchool.settings import BASE_DIR
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Ecole, Site, Classe, Matiere, Enseignant
from rest_framework import permissions


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


"""class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer
    # permission_classes = [permissions.IsAuthenticated]"""


@api_view(['GET'])
def PhotoView(request):
    photos = None
    if request.method == 'GET':
        path = os.path.join(BASE_DIR, 'photos.json')
        with open(path, 'r') as photo:
            photos = photo.read()

    return Response(photos, status=201)


class MatiereList(APIView):
    """
    List all matieres, or create a new matiere.
    """

    def get(self, request, format=None):
        matieres = Matiere.objects.all()
        serializer = MatiereSerializer(matieres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MatiereSerializer(data=request.data)
        print(f'contenu de la requete post => { request.data}')
        if serializer.is_valid():
            print('serializer is valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('serializer is not valid')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatiereDetail(APIView):
    """
    Retrieve, update or delete a matiere instance.
    """

    def get_object(self, pk):
        try:
            return Matiere.objects.get(pk=pk)

        except Matiere.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        matiere = self.get_object(pk)
        serializer = MatiereSerializer(matiere)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        matiere = self.get_object(pk)
        print(f'matière à updater => {matiere}')
        serializer = MatiereSerializer(matiere, data=request.data)
        print(f'contenu de la requete put =>{ request.data}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(f"pk sent => {pk}")
        matiere = self.get_object(pk)
        print(f'deleted {matiere} with id={pk} ')
        matiere.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
