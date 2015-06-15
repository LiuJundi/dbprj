# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0003_auto_20150614_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothdetail',
            old_name='orderId',
            new_name='order',
        ),
        migrations.AlterUniqueTogether(
            name='clothdetail',
            unique_together=set([('clothType', 'order')]),
        ),
    ]
