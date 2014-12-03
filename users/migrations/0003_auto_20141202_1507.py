# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141202_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='city_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='country_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='sex',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='social_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
