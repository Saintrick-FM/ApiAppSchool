# Generated by Django 3.0.7 on 2021-10-01 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0005_auto_20210828_0607'),
        ('Inscriptions', '0002_auto_20210914_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='eleve', to='Ecole.Classe'),
        ),
    ]