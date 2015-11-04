# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0005_auto_20151103_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='departure_time',
            field=models.TimeField(null=True),
        ),
    ]
