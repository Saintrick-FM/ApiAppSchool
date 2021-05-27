# Generated by Django 3.0.7 on 2021-05-26 18:41

import ApiRest.Ecole.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0007_auto_20210514_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enseignant',
            options={'ordering': ['-dateEmbauche']},
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='creeLe',
        ),
        migrations.AlterField(
            model_name='classe',
            name='anneeAcademique',
            field=models.CharField(default=ApiRest.Ecole.models.Classe.anneeAcademique, editable=False, max_length=50, verbose_name='Année académique :'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='dateEmbauche',
            field=models.DateTimeField(auto_now_add=True, verbose_name='créé_le'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='situationSociale',
            field=models.CharField(choices=[('Marié(e)', 'Marié(e)'), ('Divorcé(e)', 'Divorcé(e)'), ('Fiancé(e)', 'Fiancé(e)'), ('Veuf(ve)', 'Veuf(ve)'), ('Célibataire', 'Célibataire')], max_length=50, verbose_name='Situation sociale'),
        ),
    ]
