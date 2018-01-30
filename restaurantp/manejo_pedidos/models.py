

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', db_column='id_persona')
    tipo_cliente = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Consumo(models.Model):
    id_consumo = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey('Pedido', db_column='id_pedido', blank=True, null=True)
    plato = models.ForeignKey('Menu', db_column='plato', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    estado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'consumo'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    id_plato = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=3, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero = models.IntegerField(blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa'


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente', blank=True, null=True)
    mesa = models.ForeignKey(Mesa, db_column='mesa', blank=True, null=True)
    valor_total = models.DecimalField(max_digits=3, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=3, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_persona = models.TextField()
    identificacion = models.TextField(unique=True)
    telefono = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, db_column='id_persona')
    usuario = models.TextField(blank=True, null=True)
    contrasenia = models.TextField(blank=True, null=True)
    rol = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'

class Post(models.Model):
    id_personal = models.AutoField(primary_key=True)
    title= models.TextField(blank=True, null=True)
    text=models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'personal'
