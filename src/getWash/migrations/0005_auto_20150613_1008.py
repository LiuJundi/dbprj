# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0004_address_customer_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='firstName',
            field=models.CharField(default=datetime.datetime(2015, 6, 13, 2, 8, 23, 757855, tzinfo=utc), max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='lastName',
            field=models.CharField(default=datetime.datetime(2015, 6, 13, 2, 8, 28, 881016, tzinfo=utc), max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='cellphone',
            field=models.CharField(unique=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerId',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
