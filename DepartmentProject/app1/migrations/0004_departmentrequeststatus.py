# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20170819_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartMentRequestStatus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('departmentName', models.CharField(max_length=100)),
            ],
        ),
    ]
