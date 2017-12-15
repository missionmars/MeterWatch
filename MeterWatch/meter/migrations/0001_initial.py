# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeterWater',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('meter_date', models.DateField(null=True, db_column=b'meter_date', blank=True)),
                ('meter_amount', models.IntegerField(default=0, db_column=b'meter_amount')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('property_name', models.CharField(max_length=100, verbose_name=b'Property Name', db_column=b'property_name')),
                ('property_address', models.CharField(max_length=100, verbose_name=b'Address', db_column=b'property_address')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='meterwater',
            name='meter_property',
            field=models.ForeignKey(to='meter.Property'),
        ),
    ]
