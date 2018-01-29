# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manejo_pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_personal', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'personal',
                'managed': False,
            },
        ),
    ]
