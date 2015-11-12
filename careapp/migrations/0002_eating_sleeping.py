# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time_eat', models.TimeField(blank=True, null=True)),
                ('food', models.CharField(blank=True, null=True, max_length=6, choices=[('BOTTLE', 'Bottle'), ('NURSED', 'Nursed'), ('FOOD', 'Food')])),
                ('leftover', models.CharField(blank=True, null=True, max_length=9, choices=[('NONE', 'None leftover'), ('1_QUARTER', '1/4 leftover'), ('1_HALF', '1/2 leftover'), ('3_QUARTER', '3/4 leftover'), ('ALL', 'All leftover')])),
                ('dailyreport', models.ForeignKey(to='careapp.DailyReport')),
            ],
        ),
        migrations.CreateModel(
            name='Sleeping',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('time_slp_start', models.TimeField(blank=True, null=True)),
                ('time_slp_end', models.TimeField(blank=True, null=True)),
                ('dailyreport', models.ForeignKey(to='careapp.DailyReport')),
            ],
        ),
    ]
