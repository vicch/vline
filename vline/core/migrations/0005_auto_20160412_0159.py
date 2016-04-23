# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160412_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='stories',
            field=models.ManyToManyField(blank=True, to='core.Story', null=True),
        ),
    ]
