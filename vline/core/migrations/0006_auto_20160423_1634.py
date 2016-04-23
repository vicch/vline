# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160412_0159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_time']},
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(null=True, verbose_name='End', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(verbose_name='Start'),
        ),
    ]
