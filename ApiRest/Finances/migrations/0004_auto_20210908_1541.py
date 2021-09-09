# Generated by Django 3.0.7 on 2021-09-08 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0005_auto_20210828_0607'),
        ('Finances', '0003_configurationfraiseleve_obligatoire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configfraisinscriptionreinscription',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='config_inscReinsc_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='configurationfraiseleve',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='config_frais_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='configurationsalaireenseignant',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='config_salaireTeacher_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='paiementautresfrais',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='autre_frais_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='paiementfraismensuels',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='frais_mensuel_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='paiementinscriptionreinscription',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='annee_scolaire_insc_reinsc', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='paiementsalaireenseignant',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salaire_teacher_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='paiementsalairepersonnel',
            name='AnneeScolaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salaire_personnel_annee', to='Ecole.AnneeScolaire'),
        ),
    ]
