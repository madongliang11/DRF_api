# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-12 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('shoe_id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('shoe_brand', models.CharField(max_length=100, verbose_name='鞋子品牌')),
                ('shoe_color', models.CharField(max_length=50, verbose_name='鞋子颜色')),
                ('shoe_size', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='鞋子尺寸')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(verbose_name='用户编号')),
            ],
            options={
                'verbose_name': '鞋',
                'verbose_name_plural': '鞋',
                'db_table': 'shoes',
                'ordering': ('create_date',),
            },
        ),
    ]
