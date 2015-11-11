# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import careapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0002_eating_sleeping'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='child_image',
            field=models.ImageField(null=True, upload_to=careapp.models.get_image_path, blank=True),
        ),
    ]
