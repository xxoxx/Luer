# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0010_auto_20151207_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_extra',
            name='pic',
            field=models.ImageField(height_field=b'100', width_field=b'100', upload_to=b'upload'),
        ),
    ]
