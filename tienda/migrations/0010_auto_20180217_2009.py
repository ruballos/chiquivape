# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-18 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_auto_20180215_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleventa',
            old_name='detalle_venta',
            new_name='venta',
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalle_producto', to='tienda.Producto'),
        ),
    ]
