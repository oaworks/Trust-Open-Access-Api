# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('Title', models.CharField(default=b'', max_length=100, blank=True)),
                ('URL', models.CharField(max_length=300, serialize=False, primary_key=True)),
                ('DOAJurl', models.CharField(max_length=300, blank=True)),
                ('DOAJapproved', models.BooleanField(default=False)),
                ('Predatory', models.BooleanField(default=False)),
                ('Hybrid', models.BooleanField(default=False)),
                ('OpenAccess', models.BooleanField(default=False)),
                ('OASPAapproved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('URL',),
            },
        ),
    ]
