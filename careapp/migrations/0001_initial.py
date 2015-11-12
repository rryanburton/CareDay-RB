# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='B', choices=[('B', 'Boy'), ('G', 'Girl')], max_length=1)),
                ('first_name', models.CharField(max_length=20)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('parent_name', models.CharField(null=True, max_length=20, blank=True)),
                ('parent_email', models.EmailField(null=True, max_length=254, blank=True)),
                ('parent_phone', models.CharField(null=True, max_length=15, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('arrival_time', models.TimeField(null=True, blank=True)),
                ('departure_time', models.TimeField(null=True, blank=True)),
                ('mood_am', models.CharField(default='HA', choices=[('HA', 'Happy'), ('FI', 'Fine'), ('LF', 'A Little Fussy'), ('VF', 'Very Fussy'), ('NW', 'Not Well')], max_length=2)),
                ('mood_pm', models.CharField(default='HA', choices=[('HA', 'Happy'), ('FI', 'Fine'), ('LF', 'A Little Fussy'), ('VF', 'Very Fussy'), ('NW', 'Not Well')], max_length=2)),
                ('child', models.ForeignKey(to='careapp.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Diapering',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('time_diaper', models.TimeField()),
                ('num_one', models.BooleanField()),
                ('num_two', models.BooleanField()),
                ('comments', models.CharField(null=True, max_length=100, blank=True)),
                ('dailyreport', models.ForeignKey(to='careapp.DailyReport')),
            ],
        ),
    ]
