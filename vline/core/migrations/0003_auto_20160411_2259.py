# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160411_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entityevent',
            name='entity',
        ),
        migrations.RemoveField(
            model_name='entityevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='storyevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='storyevent',
            name='story',
        ),
        migrations.AddField(
            model_name='event',
            name='entities',
            field=models.ManyToManyField(to='core.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='stories',
            field=models.ManyToManyField(to='core.Story'),
        ),
        migrations.DeleteModel(
            name='EntityEvent',
        ),
        migrations.DeleteModel(
            name='StoryEvent',
        ),
    ]
