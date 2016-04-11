# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EntityEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField()),
                ('cause', models.TextField()),
                ('effect', models.TextField()),
                ('entity', models.ForeignKey(to='core.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name='Date/Time')),
                ('end_time', models.DateTimeField(verbose_name='Date/Time')),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cause', models.TextField()),
                ('effect', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EventRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField()),
                ('from_event', models.ForeignKey(to='core.Event', related_name='from_event')),
                ('to_event', models.ForeignKey(to='core.Event', related_name='to_event')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StoryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('event', models.ForeignKey(to='core.Event')),
                ('story', models.ForeignKey(to='core.Story')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='core.EventType'),
        ),
        migrations.AddField(
            model_name='entityevent',
            name='event',
            field=models.ForeignKey(to='core.Event'),
        ),
        migrations.AddField(
            model_name='entity',
            name='type',
            field=models.ForeignKey(to='core.EntityType'),
        ),
    ]
