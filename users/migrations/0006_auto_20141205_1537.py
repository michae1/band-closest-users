# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20141205_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='social_id',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
