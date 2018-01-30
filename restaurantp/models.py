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

from django.forms import ModelForm


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
