# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-18 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_auto_20180217_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.DetallePedido'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='detalle_venta',
            field=models.ManyToManyField(through='tienda.DetalleVenta', to='tienda.DetallePedido'),
        ),
    ]