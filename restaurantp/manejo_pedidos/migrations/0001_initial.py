# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(serialize=False, primary_key=True)),
                ('tipo_cliente', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id_consumo', models.AutoField(serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'consumo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.AutoField(serialize=False, primary_key=True)),
                ('id_plato', models.TextField(null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('precio', models.DecimalField(null=True, max_digits=3, decimal_places=3, blank=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id_mesa', models.AutoField(serialize=False, primary_key=True)),
                ('numero', models.IntegerField(null=True, blank=True)),
                ('capacidad', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'mesa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(serialize=False, primary_key=True)),
                ('valor_total', models.DecimalField(null=True, max_digits=3, decimal_places=3, blank=True)),
                ('subtotal', models.DecimalField(null=True, max_digits=3, decimal_places=3, blank=True)),
            ],
            options={
                'db_table': 'pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_persona', models.TextField()),
                ('identificacion', models.TextField(unique=True)),
                ('telefono', models.TextField(null=True, blank=True)),
                ('direccion', models.TextField(null=True, blank=True)),
                ('mail', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_personal', models.AutoField(serialize=False, primary_key=True)),
                ('usuario', models.TextField(null=True, blank=True)),
                ('contrasenia', models.TextField(null=True, blank=True)),
                ('rol', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'personal',
                'managed': False,
            },
        ),
    ]
