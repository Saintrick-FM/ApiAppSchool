# Generated by Django 3.0.7 on 2021-09-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0005_auto_20210828_0607'),
        ('Finances', '0004_auto_20210908_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configurationfraiseleve',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='configurationfraiseleve',
            name='obligatoire',
        ),
        migrations.CreateModel(
            name='EcolageEtAutresFrais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('periodePaiement', models.CharField(max_length=100, verbose_name='Période de paiement')),
                ('obligatoire', models.BooleanField(default=True, verbose_name='Frais Obligatoire ?')),
                ('montant', models.FloatField()),
                ('AnneeScolaire', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecolage_AutresFrais_annnee', to='Ecole.AnneeScolaire')),
                ('classe', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecolage_classe', to='Ecole.Classe')),
                ('typeFrais', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.DO_NOTHING, to='Finances.ConfigurationFraisEleve', verbose_name='Intitulé du frais')),
            ],
            options={
                'db_table': 'Ecolage_Et_Autres_Frais',
            },
        ),
    ]