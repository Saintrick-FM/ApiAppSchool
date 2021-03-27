from rest_framework import serializers, viewsets
from .models import Classe

# Create your views here.


class ClasseSerializer(serializers.ModelSerializer):
    # eleve = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = Classe
        fields = '__all__'


class ClassViewset(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer