# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('admintools', '0004_auto_20170609_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataqualityissue',
            name='jurisdiction',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='dataquality_issues', to='core.Jurisdiction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataqualityissue',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]