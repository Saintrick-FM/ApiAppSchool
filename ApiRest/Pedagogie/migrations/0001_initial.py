# Generated by Django 3.0.7 on 2021-05-29 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ecole', '0001_initial'),
        ('Inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('periode', models.CharField(choices=[('Octobre', 'Octobre'), ('Novembre', 'Novembre'), ('Décembre', 'Décembre'), ('Janvier', 'Janvier'), ('Février', 'Février'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Trimestre', (('1er Trimestre', '1er Trimestre'), ('2e Trimestre', '2e Trimestre'), ('3e Trimestre', '3e Trimestre')))], max_length=50, verbose_name='Mois ou Trimestre :')),
                ('notePremierDevoir', models.FloatField(help_text='Note du 1er devoir de classe')),
                ('noteDeuxiemeDevoir', models.FloatField(help_text='Note du 2e devoir de classe', null=True)),
                ('moyenneDevoir', models.FloatField(editable=False, null=True, verbose_name='Moyenne devoir de classe')),
                ('noteCompo', models.FloatField(help_text='Note du premier devoir de classe')),
                ('coefficient_matiere', models.PositiveIntegerField(default=4, editable=False)),
                ('absenceJustifiee', models.BooleanField(blank=True, help_text="cochez si l'absence de l'élève a été justifiée", null=True, verbose_name='Absence justifiée')),
                ('observations', models.CharField(max_length=150, verbose_name='Observations')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_classe', to='Ecole.Classe')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_eleve', to='Inscriptions.Eleve', to_field='nom')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_matiere', to='Ecole.Matiere')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
