# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clothId', models.IntegerField()),
                ('unitPrice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('sales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClothDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderId', models.IntegerField()),
                ('clothId', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
