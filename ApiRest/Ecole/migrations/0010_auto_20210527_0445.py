# Generated by Django 3.0.7 on 2021-05-27 04:45

import ApiRest.Ecole.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecole', '0009_auto_20210527_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='anneeAcademique',
            field=models.CharField(default=ApiRest.Ecole.models.anneeAcademique, editable=False, max_length=50, verbose_name='Année académique :'),
        ),
    ]