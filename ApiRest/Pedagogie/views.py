from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializer import NoteSerializer


class NoteViewsets(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

     def create(self, request, *arg, **kwargs):
        moyene_devoir = (int(request.note_premier_devoir) +
                        int(request.note_deuxieme_devoir))/2
        point_total_compo = int(request.note_compo) * \
            int(request.coefficient_matiere)
        # pour une matiere de coefficient 4 80pts=20 de moyenne
        moyenne_compo = (point_total_compo*20)/80
        moyenne_generale_matiere = (moyenne_compo+moyene_devoir)/2

        valide_dataPlusMG = validated_data.pop('moyenne_generale_matiere': moyenne_generale_matiere))
        note=Note.objects.create(**validated_data)
        note.moyenne_generale_matiere=valide_dataPlusMG
        note.save()
        return user
