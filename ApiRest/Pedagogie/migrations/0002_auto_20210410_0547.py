# Generated by Django 3.0.7 on 2021-04-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedagogie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='moyenne_generale',
        ),
        migrations.AddField(
            model_name='note',
            name='moyenne_generale_matiere',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='coefficient_matiere',
            field=models.PositiveIntegerField(default=4, editable=False),
        ),
    ]