# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0013_auto_20151207_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_extra',
            name='password',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
