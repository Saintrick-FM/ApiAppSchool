# Generated by Django 3.0.7 on 2021-03-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inscriptions', '0002_auto_20210326_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='id',
        ),
        migrations.AddField(
            model_name='eleve',
            name='eleveNumber',
            field=models.IntegerField(auto_created=True, db_column='n°', default=1, verbose_name='n°:'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='nom',
            field=models.CharField(help_text='Tapez tous les noms et prénoms', max_length=255, primary_key=True, serialize=False),
        ),
    ]
