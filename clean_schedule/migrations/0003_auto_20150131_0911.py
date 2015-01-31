# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean_schedule', '0002_auto_20150131_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanuser',
            name='group',
            field=models.ForeignKey(to='clean_schedule.Group', null=True),
            preserve_default=True,
        ),
    ]
