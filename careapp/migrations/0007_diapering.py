# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0006_auto_20151103_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diapering',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('time_diaper', models.TimeField()),
                ('num_one', models.BooleanField()),
                ('num_two', models.BooleanField()),
                ('comments', models.CharField(max_length=100)),
                ('dailyreport_id', models.ForeignKey(to='careapp.DailyReport')),
            ],
        ),
    ]
