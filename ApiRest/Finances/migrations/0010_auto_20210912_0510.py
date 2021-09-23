# Generated by Django 3.0.7 on 2021-09-12 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0005_auto_20210828_0607'),
        ('Finances', '0009_configdepenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationfraiseleve',
            name='AnneeScolaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='config_frais_annee', to='Ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='configurationfraiseleve',
            name='montant',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='configurationfraiseleve',
            name='periodePaiement',
            field=models.CharField(max_length=100, null=True, verbose_name='Période de paiement'),
        ),
    ]
