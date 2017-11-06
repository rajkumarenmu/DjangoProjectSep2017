# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstName', models.CharField(null=True, max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
