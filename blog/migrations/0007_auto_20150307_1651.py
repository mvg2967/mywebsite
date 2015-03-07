# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20141226_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/products/', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, unique=True, max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, unique=True, max_length=100, null=True),
            preserve_default=True,
        ),
    ]
