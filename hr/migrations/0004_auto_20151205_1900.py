# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20151205_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary_extra',
            name='name',
        ),
        migrations.AddField(
            model_name='employee_extra',
            name='extra_salary',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Salary_extra',
        ),
    ]
