# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0002_auto_20150612_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='id',
        ),
        migrations.RemoveField(
            model_name='clothdetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='cloth',
            name='clothType',
            field=models.CharField(default=datetime.datetime(2015, 6, 12, 15, 53, 3, 785204, tzinfo=utc), max_length=50, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clothdetail',
            name='clothType',
            field=models.CharField(default=datetime.datetime(2015, 6, 12, 15, 53, 17, 806005, tzinfo=utc), max_length=50, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clothdetail',
            name='orderId',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
