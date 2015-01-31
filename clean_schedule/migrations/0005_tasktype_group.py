# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clean_schedule', '0004_auto_20150131_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktype',
            name='group',
            field=models.ForeignKey(to='clean_schedule.Group', null=True),
            preserve_default=True,
        ),
    ]
