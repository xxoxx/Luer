# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'hr', '0001_initial')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendence_name', models.CharField(max_length=100)),
                ('is_early_or_late', models.BooleanField(default=None)),
                ('attendence_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_name', models.CharField(max_length=100)),
                ('department_manager', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=100)),
                ('base_salary', models.FloatField()),
                ('hiredate', models.DateField()),
                ('department', models.ForeignKey(to='hr.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salary_extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salary', models.FloatField()),
                ('name', models.ForeignKey(to='hr.Employee_extra')),
            ],
        ),
    ]
