# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=100)),
                ('last', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('classification', models.CharField(blank=True, choices=[('fr', 'Freshman'), ('sp', 'Sophomore'), ('jn', 'Junior'), ('sn', 'Senior'), ('gd', 'Graduate Student'), ('ns', 'Not a Student')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]