# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0003_child_child_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_image',
            field=models.ImageField(upload_to='static/img/', null=True, blank=True),
        ),
    ]
