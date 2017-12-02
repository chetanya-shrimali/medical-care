# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-02 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register_hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(default='Text Here')),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('type', models.CharField(choices=[('GOV', 'Government'), ('PR', 'Private')], max_length=10)),
                ('speciality', models.CharField(max_length=50)),
                ('working_days', models.CharField(max_length=10)),
                ('working_hours', models.CharField(max_length=10)),
                ('blood_bank_availability', models.BooleanField(default=False)),
                ('avg_cost', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default=0, max_length=10)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register_hospital.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('timing_from', models.TimeField()),
                ('timing_to', models.TimeField()),
                ('availability_now', models.BooleanField(default=False)),
                ('experience', models.CharField(max_length=50)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_detail.Detail')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('comment', models.TextField()),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_detail.Detail')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_detail.Detail')),
            ],
        ),
    ]
