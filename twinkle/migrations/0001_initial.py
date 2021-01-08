# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-11-10 01:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('classlevel', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=2)),
                ('time_of_study', models.CharField(max_length=100)),
                ('campus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_firstname', models.CharField(max_length=100)),
                ('father_lastname', models.CharField(max_length=100)),
                ('father_phonenumber_one', models.IntegerField(default=0)),
                ('father_phonenumber_two', models.IntegerField(default=0)),
                ('mother_firstname', models.CharField(max_length=100)),
                ('mother_lastname', models.CharField(max_length=100)),
                ('mother_phonenumber_one', models.IntegerField(default=0)),
                ('mother_phonenumber_two', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('time', models.DateField(default=datetime.date.today)),
                ('bank', models.CharField(max_length=100)),
                ('term', models.IntegerField(default=1)),
                ('year', models.IntegerField(default=0)),
                ('installment', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='children',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='twinkle.parents', verbose_name='parent'),
        ),
    ]
