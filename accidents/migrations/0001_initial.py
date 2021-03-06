# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Malfunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('mf_desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SolvedMalfunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_rate', models.IntegerField()),
                ('repair_desc', models.TextField(max_length=200)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accidents.Application')),
            ],
        ),
    ]
