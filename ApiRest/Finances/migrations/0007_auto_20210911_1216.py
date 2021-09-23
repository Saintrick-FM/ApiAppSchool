# Generated by Django 3.0.7 on 2021-09-11 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0005_auto_20210828_0607'),
        ('Finances', '0006_configfraisinscriptionreinscription_periodepaiement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigAutresFrais',
            fields=[
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('identifiant', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('periodePaiement', models.CharField(max_length=100, verbose_name='Période de paiement')),
                ('obligatoire', models.BooleanField(default=True, verbose_name='Frais Obligatoire ?')),
                ('montant', models.FloatField()),
                ('AnneeScolaire', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='autresFrais_annnee', to='Ecole.AnneeScolaire')),
                ('classe', models.ManyToManyField(related_name='autreFrais_classe', to='Ecole.Classe')),
            ],
            options={
                'db_table': 'Configuration_Autres_Frais',
            },
        ),
        migrations.CreateModel(
            name='ConfigEcolage',
            fields=[
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('identifiant', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Intitulé du frais')),
                ('periodePaiement', models.CharField(max_length=100, verbose_name='Période de paiement')),
                ('obligatoire', models.BooleanField(default=True, verbose_name='Frais Obligatoire ?')),
                ('montant', models.FloatField()),
                ('AnneeScolaire', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecolage_annnee', to='Ecole.AnneeScolaire')),
                ('classe', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ecolage_classe', to='Ecole.Classe')),
            ],
            options={
                'db_table': 'Ecolage',
            },
        ),
        migrations.DeleteModel(
            name='EcolageEtAutresFrais',
        ),
    ]