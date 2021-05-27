# Generated by Django 3.0.7 on 2021-05-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0010_auto_20210527_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='intituleCompte',
            field=models.CharField(blank=True, help_text="Ecrire le nom du compte bancaire de l'enseignant", max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='numeroCnss',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Numéro CNSS'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='numeroCompteBancaire',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Numéro compte bancaire'),
        ),
    ]