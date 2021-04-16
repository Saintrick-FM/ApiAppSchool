from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializer import NoteSerializer


class NoteViewsets(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

