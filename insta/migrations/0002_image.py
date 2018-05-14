# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=20)),
                ('image_description', models.CharField(max_length=30)),
                ('image', models.ImageField(blank='True', null='True', upload_to='photos/')),
            ],
        ),
    ]