# Generated by Django 3.0.7 on 2021-04-10 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inscriptions', '0001_initial'),
        ('Pedagogie', '0003_auto_20210410_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='note_eleve', to='Inscriptions.Eleve'),
        ),
    ]