# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0006_person_photo_consent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo_consent',
            field=models.BooleanField(),
        ),
    ]
