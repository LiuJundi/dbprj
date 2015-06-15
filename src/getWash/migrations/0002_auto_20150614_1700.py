# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getWash', '0001_initial'),
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
                ('customerId', models.AutoField(serialize=False, primary_key=True)),
                ('cellphone', models.CharField(unique=True, max_length=15)),
                ('firstName', models.CharField(max_length=16)),
                ('lastName', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('memo', models.CharField(max_length=200, null=True)),
                ('state', models.IntegerField(default=0)),
                ('sumPrice', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('bookTime', models.DateTimeField(auto_now_add=True)),
                ('collectTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('finishTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('backTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('addrId', models.ForeignKey(to='getWash.Address')),
                ('customerId', models.ForeignKey(to='getWash.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='clothId',
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='id',
        ),
        migrations.AddField(
            model_name='cloth',
            name='clothType',
            field=models.CharField(default=0, max_length=50, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothdetail',
            name='clothType',
            field=models.ForeignKey(default=0, to='getWash.Cloth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clothdetail',
            name='orderId',
            field=models.ForeignKey(to='getWash.Order'),
        ),
        migrations.AlterUniqueTogether(
            name='clothdetail',
            unique_together=set([('clothType', 'orderId')]),
        ),
        migrations.RemoveField(
            model_name='clothdetail',
            name='clothId',
        ),
    ]
