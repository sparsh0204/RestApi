# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 10:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_datatable_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatable',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
