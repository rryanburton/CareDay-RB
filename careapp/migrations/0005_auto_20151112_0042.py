# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0004_auto_20151112_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='child_image',
            new_name='image',
        ),
    ]
