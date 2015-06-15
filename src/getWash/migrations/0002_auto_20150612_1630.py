# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='clothId',
        ),
        migrations.RemoveField(
            model_name='clothdetail',
            name='clothId',
        ),
        migrations.AddField(
            model_name='cloth',
            name='clothType',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clothdetail',
            name='clothType',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
