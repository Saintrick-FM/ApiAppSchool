# Generated by Django 3.0.7 on 2021-09-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finances', '0002_configurationfraiseleve_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationfraiseleve',
            name='obligatoire',
            field=models.BooleanField(default=True, verbose_name='Frais Obligatoire ?'),
        ),
    ]
