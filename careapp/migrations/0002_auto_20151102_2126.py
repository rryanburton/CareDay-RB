# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(default='B', max_length=1, choices=[('B', 'B'), ('G', 'G')]),
        ),
    ]
