# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cpuInfo', models.CharField(max_length=50)),
                ('macInfo', models.CharField(max_length=50)),
                ('memoryInfo', models.CharField(max_length=100)),
                ('gpuInfo', models.CharField(max_length=100)),
                ('keyInfo', models.CharField(max_length=200)),
                ('deviceInfo', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('userpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
