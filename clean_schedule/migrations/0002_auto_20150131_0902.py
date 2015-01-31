# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clean_schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleanUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('group', models.ForeignKey(to='clean_schedule.Group')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=True,
        ),
    ]
