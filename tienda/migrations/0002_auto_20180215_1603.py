# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-15 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(blank=True, default='', max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='tienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda'),
        ),
        migrations.AddField(
            model_name='venta',
            name='tienda',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda'),
        ),
    ]