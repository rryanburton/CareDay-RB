# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('birthday', models.DateField()),
                ('parent_name', models.CharField(max_length=10)),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_phone', models.CharField(max_length=12)),
            ],
        ),
    ]
