# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0003_auto_20150612_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressId', models.AutoField(serialize=False, primary_key=True)),
                ('school', models.CharField(max_length=16)),
                ('building', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=64)),
                ('cellphone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.IntegerField(serialize=False, primary_key=True)),
                ('memo', models.CharField(max_length=200)),
                ('customerId', models.IntegerField()),
                ('state', models.IntegerField(default=0)),
                ('sumPrice', models.IntegerField()),
                ('addrId', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('bookTime', models.DateTimeField()),
                ('collectTime', models.DateTimeField(null=True)),
                ('finishTime', models.DateTimeField(null=True)),
                ('backTime', models.DateTimeField(null=True)),
            ],
        ),
    ]
