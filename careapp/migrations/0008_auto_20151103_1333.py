# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0007_remove_child_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='departure_time',
            field=models.TimeField(null=True),
        ),
    ]
