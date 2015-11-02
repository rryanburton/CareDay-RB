# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0002_auto_20151102_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 11, 2, 23, 0, 59, 910734, tzinfo=utc))),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('mood_am', models.CharField(default='HA', choices=[('HA', 'Happy'), ('FI', 'Fine'), ('LF', 'A Little Fussy'), ('VF', 'Very Fussy'), ('NW', 'Not Well')], max_length=2)),
                ('mood_pm', models.CharField(default='HA', choices=[('HA', 'Happy'), ('FI', 'Fine'), ('LF', 'A Little Fussy'), ('VF', 'Very Fussy'), ('NW', 'Not Well')], max_length=2)),
                ('child', models.ForeignKey(to='careapp.Child')),
            ],
        ),
    ]
