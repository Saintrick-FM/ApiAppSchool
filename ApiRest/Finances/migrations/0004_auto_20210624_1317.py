# Generated by Django 3.0.7 on 2021-06-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finances', '0003_auto_20210624_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiementfrais',
            name='montantDejaPaye',
            field=models.FloatField(default=0, verbose_name='Montant déjà payé'),
        ),
        migrations.AlterField(
            model_name='paiementfrais',
            name='montantRestant',
            field=models.FloatField(verbose_name='Montant restant'),
        ),
    ]
