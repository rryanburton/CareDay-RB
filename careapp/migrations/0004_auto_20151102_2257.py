# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0003_dailyreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 2, 22, 57, 50, 379529)),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
