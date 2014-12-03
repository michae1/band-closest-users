# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialgroup',
            name='social_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
