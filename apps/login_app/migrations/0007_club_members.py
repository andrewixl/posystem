# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-07 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_user_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(related_name='members', to='login_app.User'),
        ),
    ]
