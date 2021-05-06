from django.db import models
from ..Ecole.models import Matiere, Enseignant, Classe
from ..Inscriptions.models import Eleve
from ApiRest.Utils.models import TimeStamp


PERIODE = (
    ('Octobre', 'Octobre'),
    ('Novembre', 'Novembre'),
    ('Décembre', 'Décembre'),
    ('Janvier', 'Janvier'),
    ('Février', 'Février'),
    ('Mars', 'Mars'),
    ('Avril', 'Avril'),
    ('Mai', 'Mai'),
    ('Juin', 'Juin'),
    ('Trimestre', (
        ('1er Trimestre', '1er Trimestre'),
        ('2e Trimestre', '2e Trimestre'),
        ('3e Trimestre', '3e Trimestre'),
    )
    ),

)


class Note(TimeStamp):

    eleve = models.ForeignKey(Eleve, on_delete=models.DO_NOTHING,
                              related_name='note_eleve', to_field='nom')
    classe = models.ForeignKey(
        Classe, on_delete=models.DO_NOTHING, related_name='note_classe')
    matiere = models.ForeignKey(
        Matiere, on_delete=models.DO_NOTHING, related_name='note_matiere')
    periode = models.CharField(
        'Mois ou Trimestre :', max_length=50, choices=PERIODE, null=False,)
    notePremierDevoir = models.FloatField(
        help_text='Note du 1er devoir de classe', null=False)
    noteDeuxiemeDevoir = models.FloatField(
        help_text='Note du 2e devoir de classe', null=True)
    moyenneDevoir = models.FloatField(
        'Moyenne devoir de classe', null=True, editable=False)
    noteCompo = models.FloatField(
        help_text='Note du premier devoir de classe', null=False)
    coefficient_matiere = models.PositiveIntegerField(
        default=4, editable=False)
    absenceJustifiee = models.BooleanField('Absence justifiée',
                                           blank=True, null=True,
                                           help_text="cochez si l'absence de l'élève a été justifiée")
    moyenneGeneraleMatiere = models.FloatField(
        null=True, editable=False)
    observations = models.CharField('Observations', max_length=150, null=False)

    def __str__(self):
        return f'Notes {self.periode}, {self.classe}'

    def moyenneGeneraleMatiere(self):
        output = ''

        try:
            eleve_sans_moyenne = Note.objects.get(
                moyenne_generale_matiere=None)
            print('Juste avant le if valeur de l Eleve sans moyenne =' +
                  bool(eleve_sans_moyenne))
            if bool(eleve_sans_moyenne):
                print("A l'interieur du bloc if")
                eleve_sans_moyenne = Note.objects.get(
                    moyenne_generale_matiere=None)
                note_premier_devoir = eleve_sans_moyenne.note_premier_devoir
                note_deuxieme_devoir = eleve_sans_moyenne.note_deuxieme_devoir
                note_compo = eleve_sans_moyenne.note_compo
                coefficient = eleve_sans_moyenne.coefficient_matiere

                moyene_devoir = (int(note_premier_devoir) +
                                 int(note_deuxieme_devoir))/2
                point_total_compo = int(note_compo) * int(coefficient)
                # pour une matiere de coefficient 4 80pts=20 de moyenne
                moyenne_compo = (point_total_compo*20)/80
                moyenne_generale = (moyenne_compo+moyene_devoir)/2

                eleve_sans_moyenne.moyenne_generale_matiere = moyenne_generale
                eleve_sans_moyenne.save()
                output = "😃  Moyenne Générale de l'élève ajouté avec succès"
            else:
                output = '😢 elève non trouvé'
        except:
            output = "😠😠😠 le programme a levé l'exception = >\
                Note matching query does not exist"
        return output


# note = Note()
# print(note.moyenneGeneraleMatiere())
