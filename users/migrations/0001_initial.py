# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('social_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('sex', models.IntegerField(max_length=10)),
                ('city_name', models.CharField(max_length=255)),
                ('city_id', models.IntegerField()),
                ('social_id', models.IntegerField()),
                ('country_name', models.CharField(max_length=255)),
                ('country_id', models.IntegerField()),
                ('social_groups', models.ManyToManyField(to='users.SocialGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
