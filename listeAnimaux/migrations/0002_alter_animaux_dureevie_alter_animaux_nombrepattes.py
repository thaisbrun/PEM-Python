# Generated by Django 4.0.5 on 2022-06-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listeAnimaux', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaux',
            name='dureeVie',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='animaux',
            name='nombrePattes',
            field=models.IntegerField(),
        ),
    ]
