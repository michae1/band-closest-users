# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20141202_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialgroup',
            name='processed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
