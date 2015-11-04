# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0004_auto_20151102_2257'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(max_length=1, default='B', choices=[('B', 'Boy'), ('G', 'Girl')]),
        ),
    ]
