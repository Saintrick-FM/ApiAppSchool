# Generated by Django 3.0.7 on 2021-08-27 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0002_auto_20210827_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='anneeScolaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='classe_annee_scolaire', to='Ecole.AnneeScolaire', verbose_name='Année Scolaire'),
        ),
        migrations.AlterField(
            model_name='classe',
            name='scolarite',
            field=models.CharField(help_text='Frais à payer mensuellement Eg: 8000F', max_length=50, null=True),
        ),
    ]