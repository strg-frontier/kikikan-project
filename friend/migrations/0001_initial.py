# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_user', models.IntegerField()),
                ('follow_user', models.IntegerField()),
                ('request_state', models.IntegerField(default=0)),
            ],
        ),
    ]
