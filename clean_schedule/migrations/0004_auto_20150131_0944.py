# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean_schedule', '0003_auto_20150131_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='owner',
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(to='clean_schedule.CleanUser'),
            preserve_default=True,
        ),
    ]
