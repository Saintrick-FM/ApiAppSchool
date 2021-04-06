# Generated by Django 3.0.7 on 2021-04-03 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ecole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('eleveNumber', models.AutoField(auto_created=True, db_column='n°', primary_key=True, serialize=False, verbose_name='n°:')),
                ('nom', models.CharField(help_text='Tapez tous les noms et prénoms', max_length=255, unique=True)),
                ('sexe', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], default='', max_length=255)),
                ('naissance', models.CharField(help_text='Tappez juste la date de Naissance Eg: 11-Mai-1995', max_length=50)),
                ('lieuNaiss', models.CharField(db_column='lieuDeNaissance', default='Brazzaville', max_length=50)),
                ('nationalite', models.CharField(default='Congolaise', max_length=255)),
                ('etat_sanitaire', models.CharField(choices=[('Apte', 'Apte'), ('Inapte', 'Inapte')], default=('Apte', 'Apte'), max_length=20)),
                ('ecole_d_origine', models.CharField(default='Saint Martin', max_length=255)),
                ('nom_de_maman', models.CharField(help_text='Tapez tous les noms et prénoms', max_length=255)),
                ('tel_maman', models.CharField(blank=True, max_length=15, null=True)),
                ('nom_de_papa', models.CharField(help_text='Tapez tous les noms et prénoms', max_length=255)),
                ('tel_papa', models.CharField(blank=True, max_length=15, null=True)),
                ('tuteur', models.CharField(max_length=255)),
                ('tel_tuteur', models.CharField(max_length=15)),
                ('email_tuteur', models.EmailField(max_length=255, null=True)),
                ('date_inscription', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('redoublant', models.CharField(choices=[('Nouveau', 'Nouveau'), ('Redoublant', 'Redoublant')], default=('Nouveau', 'Nouveau'), max_length=25)),
                ('scolarite', models.CharField(default='', editable=False, max_length=50)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eleve', to='Ecole.Classe')),
            ],
        ),
    ]
