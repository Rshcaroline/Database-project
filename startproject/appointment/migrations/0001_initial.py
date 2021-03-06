# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0005_auto_20170516_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=32, verbose_name='成员')),
                ('gender', models.CharField(max_length=16, verbose_name='性别')),
                ('major', models.CharField(max_length=16, verbose_name='专业')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('awards', models.TextField(verbose_name='获奖')),
                ('introduction', models.TextField(verbose_name='介绍')),
            ],
        ),
        migrations.CreateModel(
            name='appoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xid', models.CharField(max_length=9, verbose_name='预约对象的id')),
                ('xtype', models.CharField(max_length=9, verbose_name='预约对象的类型')),
                ('starttime', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('people', models.CharField(max_length=10, verbose_name='预约人数')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=140, verbose_name='讲座主题')),
                ('professor', models.CharField(max_length=32, verbose_name='教授')),
                ('introduction', models.TextField(verbose_name='介绍')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=32, verbose_name='应用名称')),
                ('introduction', models.TextField(verbose_name='介绍')),
            ],
        ),
    ]
