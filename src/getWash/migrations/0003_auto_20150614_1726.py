# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0002_auto_20150614_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='addrId',
            new_name='addr',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerId',
            new_name='customer',
        ),
    ]
