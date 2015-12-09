# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='year',
            field=models.CharField(default=1997, max_length=100),
            preserve_default=False,
        ),
    ]
