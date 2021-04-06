# Generated by Django 3.0.7 on 2021-04-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigSalairePersonnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie_personnel', models.CharField(choices=[('Surveillant', 'Surveillant'), ('Caissier', 'Caissier'), ('Directeurs', (('PDG', 'Promoteur'), ('DG', 'Directeur Général'), ('DE', 'Directeur des Etudes'))), ('Agent De propreté', 'Agent de propreté'), ('Agent de sécurité', 'Agent de sécurité')], max_length=50, verbose_name="Catégorie d'employé :")),
                ('salaire_defini', models.FloatField(verbose_name='Salaire défini')),
            ],
            options={
                'db_table': 'Configuration_Salaire_Personnel',
            },
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('personnel_numero', models.AutoField(auto_created=True, db_column='n°', primary_key=True, serialize=False, verbose_name='N°:')),
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('nom', models.CharField(help_text='Tapez tous les noms et prénoms', max_length=255, unique=True)),
                ('civilite', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], default='', max_length=255)),
                ('date_naissance', models.CharField(help_text='Tappez juste la date de Naissance Eg: 11-Mai-1995', max_length=50)),
                ('lieu_naissance', models.CharField(blank=True, db_column='lieuDeNaissance', default='Brazzaville', max_length=50)),
                ('situation_sociale', models.CharField(choices=[('Marie', 'Marié(e)'), ('Divorce', 'Divorcé(e)'), ('Fiance', 'Fiancé(e)'), ('Veuf', 'Veuf(ve)'), ('Celibataire', 'Célibataire')], max_length=50)),
                ('nationalite', models.CharField(default='Congolaise', max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('date_d_embauche', models.DateField()),
                ('poste_occupe', models.CharField(choices=[('Surveillant', 'Surveillant'), ('Caissier', 'Caissier'), ('Directeurs', (('PDG', 'Promoteur'), ('DG', 'Directeur Général'), ('DE', 'Directeur des Etudes'))), ('Agent De propreté', 'Agent de propreté'), ('Agent de sécurité', 'Agent de sécurité')], max_length=50, verbose_name='Embauché en qualité de :')),
                ('mode_paiement', models.CharField(choices=[('Manuel', 'Manuel'), ('Virement', 'Virement Bancaire')], default=('Manuel', 'Manuel'), max_length=100, verbose_name='Mode de paiement')),
                ('intitule_du_compte', models.CharField(blank=True, help_text="Ecrire le nom du compte bancaire de l'enseignant", max_length=250, null=True, unique=True)),
                ('numero_du_compte_bancaire', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('numero_cnss', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='mode de paiement')),
            ],
            options={
                'ordering': ['-cree_le'],
            },
        ),
    ]
