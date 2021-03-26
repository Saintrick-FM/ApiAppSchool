from rest_framework import serializers, viewsets
from .models import Classe

# Create your views here.
class ClasseSerializer(viewsets.HyperLinkedModelSerializer):
    eleve = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)