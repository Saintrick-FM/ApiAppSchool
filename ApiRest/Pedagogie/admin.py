from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    exclude = ('coefficient',)
    list_display = ('eleve', 'classe', 'periode', 'moyenne_generale_matiere')


admin.site.register(Note, NoteAdmin)
