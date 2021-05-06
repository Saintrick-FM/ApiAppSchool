# Generated by Django 3.0.7 on 2021-05-06 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ecole', '0001_initial'),
        ('GRH', '0001_initial'),
        ('Inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigurationFraisEleve',
            fields=[
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('paiementFraisNumero', models.AutoField(primary_key=True, serialize=False, verbose_name='Paiement frais n°:')),
                ('frais', models.CharField(choices=[('Frais Mensuel', 'Frais Mensuel'), ('Frais Trimesrtiel', 'Frais trimestriel'), ('Frais Annuel', 'Frais Annuel'), ('Assurance', 'Assurance'), ("Dossier d'examen", "Dossier d'examen"), ('Macaron', 'Macaron'), ("Tenu d'eps", "Tenu d'eps")], max_length=100, verbose_name='Intitulé du frais')),
                ('montant', models.FloatField()),
            ],
            options={
                'db_table': 'Configuration_Frais_Eleve',
            },
        ),
        migrations.CreateModel(
            name='ConfigurationSalaireEnseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('categorieEnseignant', models.CharField(choices=[('Primaire', 'Enseigne au Primaire'), ('College', 'Enseigne au College')], max_length=30, verbose_name="Catégorie d'employé :")),
                ('salaireDefini', models.FloatField(verbose_name='Salaire défini')),
            ],
            options={
                'db_table': 'Configuration_Salaire_Enseignant',
            },
        ),
        migrations.CreateModel(
            name='PaiementSalairePersonnel',
            fields=[
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('paiementNumero', models.AutoField(primary_key=True, serialize=False, verbose_name='Paiement numéro =>')),
                ('moisPaiement', models.CharField(choices=[('Octobre', 'Octobre'), ('Novembre', 'Novembre'), ('Décembre', 'Décembre'), ('Janvier', 'Janvier'), ('Février', 'Février'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Autres', (('Juillet', 'Juillet'), ('Aout', 'Aout'), ('Septembre', 'Septembre')))], max_length=50, verbose_name='Mois à payer')),
                ('montantApayer', models.FloatField(verbose_name='Montant à payer')),
                ('montantDejaPaye', models.FloatField(default=0, editable=False, verbose_name='Montant déjà payé')),
                ('montantRestant', models.FloatField(editable=False, verbose_name='Montant Restant à payer')),
                ('statut', models.BooleanField(blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")),
                ('nomPersonnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='personnel_a_payer', to='GRH.Personnel', verbose_name='Nom du personnel')),
            ],
            options={
                'db_table': 'Paiement_Salaire_Personnel',
            },
        ),
        migrations.CreateModel(
            name='PaiementSalaireEnseignant',
            fields=[
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('paiementNumero', models.AutoField(primary_key=True, serialize=False, verbose_name='Paiement numéro =>')),
                ('moisPaiement', models.CharField(choices=[('Octobre', 'Octobre'), ('Novembre', 'Novembre'), ('Décembre', 'Décembre'), ('Janvier', 'Janvier'), ('Février', 'Février'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Autres', (('Juillet', 'Juillet'), ('Aout', 'Aout'), ('Septembre', 'Septembre')))], max_length=50, verbose_name='Mois à payer')),
                ('heuresEffectue', models.CharField(default='8h de cours enseignees', editable=False, max_length=50, verbose_name='Heures effectuées')),
                ('montantApayer', models.FloatField()),
                ('montantDejaPaye', models.FloatField(default=0, editable=False, verbose_name='Montant Déjà payé')),
                ('montantRestant', models.FloatField(editable=False, verbose_name='Montant Restant à payer')),
                ('statut', models.BooleanField(blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")),
                ('nomEnseignant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enseignant_a_payer', to='Ecole.Enseignant', verbose_name="Nom de l'enseignant")),
            ],
            options={
                'db_table': 'Paiement_Salaire_Enseignant',
            },
        ),
        migrations.CreateModel(
            name='PaiementFrais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='créé_le')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='modifié_le')),
                ('mois', models.CharField(blank=True, choices=[('Octobre', 'Octobre'), ('Novembre', 'Novembre'), ('Décembre', 'Décembre'), ('Janvier', 'Janvier'), ('Février', 'Février'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Autres', (('Juillet', 'Juillet'), ('Aout', 'Aout'), ('Septembre', 'Septembre')))], max_length=30, null=True, verbose_name='Mois à payer')),
                ('montantApayer', models.FloatField(verbose_name='Montant à payer')),
                ('montantDejaPaye', models.FloatField(default=0, editable=False, verbose_name='Montant déjà payé')),
                ('montantRestant', models.FloatField(editable=False, verbose_name='Montant restant')),
                ('statut', models.BooleanField(blank=True, editable=False, help_text="Est coché lorsque l'élève a réglé totalement")),
                ('classe', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='classe_eleve', to='Ecole.Classe')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='eleve_payant', to='Inscriptions.Eleve')),
                ('montantFrais', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to='Finances.ConfigurationFraisEleve', verbose_name='Montant Frais à payer')),
                ('typeFrais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='type_frais', to='Finances.ConfigurationFraisEleve', verbose_name='Type de frais à payer')),
            ],
            options={
                'verbose_name_plural': 'frais',
                'db_table': 'Paiement_frais',
            },
        ),
    ]
