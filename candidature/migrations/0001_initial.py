# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-19 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prenom', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('nb_annee_experience_data', models.IntegerField()),
            ],
        ),
    ]
