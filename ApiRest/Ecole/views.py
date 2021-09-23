import os

from ApiAppSchool.settings import BASE_DIR
from rest_framework import viewsets, permissions
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Ecole, Site, Classe, Matiere, Enseignant, AnneeScolaire,Cycle
from ApiRest.Finances.models import ConfigEcolage
from rest_framework.permissions import DjangoModelPermissions

class AnneeScolaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeScolaire
        fields = '__all__'

class AnneeScolaireViewSet(viewsets.ModelViewSet):
    queryset = AnneeScolaire.objects.all()
    serializer_class = AnneeScolaireSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class EcoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecole
        fields = '__all__'


class EcoleViewSet(viewsets.ModelViewSet):
    queryset = Ecole.objects.all()
    serializer_class = EcoleSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]



class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ClasseSerializer(serializers.ModelSerializer):
    # scolarite= serializers.CharField(read_only=True, source='ConfigEcolage.montant')
    class Meta:
        model = Classe
        fields = '__all__'


class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

"""
    frais_ecolages = ConfigEcolage.objects.all()
    for ecolage in frais_ecolages:
        result= list(Classe.objects.filter(identifiant= ecolage.montant))
        for x in result:
            setattr(x,'ecolage',ecolage)

"""

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = ['enseignant_numero','nom','civilite','date_naissance','lieu_naissance',
                  'situationSociale','nationalite','adresse','telephone','email','matiereEnseigne',
                  'classesOccupees','modePaiement', 'intituleCompte', 'numeroCompteBancaire', 'numeroCnss', 'enseigneAu',
                  'dateEmbauche', 'modifieLe', 'get_asbolute_url']


class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer


class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields= '__all__'

        # fields = ['id','nomMatiere', 'codeMatiere','pluriProf', 'matiereDeBase',
        #           'seanceParSemaine', 'coefficient', 'groupeMatiere', 'classAssocie']
        # extra_kwargs = {
        #     'url': {'view_name':'matiere-detail','lookup_field': 'nomMatiere'},
        #     # 'lookup_field': 'nomMatiere'
        # }


class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer
    #permission_classes = [permissions.DjangoModelPermissions]

"""

@api_view(['GET'])
def PhotoView(request):
    photos = None
    if request.method == 'GET':
        path = os.path.join(BASE_DIR, 'photos.json')
        with open(path, 'r') as photo:
            photos = photo.read()

    return Response(photos, status=201)


class MatiereList(APIView):
    
    List all matieres, or create a new matiere.
    
    def get(self, request, format=None):
        matieres = Matiere.objects.all()
        serializer = MatiereSerializer(matieres, many=True)
        return Response(serializer.data)

    @permission_classes([DjangoModelPermissions])
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
    
    Retrieve, update or delete a matiere instance.
    

    def get_object(self, pk):
        try:
            return Matiere.objects.get(pk=pk)

        except Matiere.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        matiere = self.get_object(pk)
        serializer = MatiereSerializer(matiere)
        return Response(serializer.data)

    @permission_classes([DjangoModelPermissions])
    def put(self, request, pk, format=None):
        matiere = self.get_object(pk)
        print(f'matière à updater => {matiere}')
        serializer = MatiereSerializer(matiere, data=request.data)
        print(f'contenu de la requete put =>{ request.data}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([DjangoModelPermissions])
    def delete(self, request, pk, format=None):
        print(f"pk sent => {pk}")
        matiere = self.get_object(pk)
        print(f'deleted {matiere} with id={pk} ')
        matiere.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""