# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20151202_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary_extra',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]
