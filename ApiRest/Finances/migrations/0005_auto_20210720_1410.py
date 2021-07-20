# Generated by Django 3.0.7 on 2021-07-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finances', '0004_auto_20210624_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiementfrais',
            name='moisSolves',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mois à solver'),
        ),
        migrations.AlterField(
            model_name='paiementfrais',
            name='mois',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mois à payer'),
        ),
    ]
