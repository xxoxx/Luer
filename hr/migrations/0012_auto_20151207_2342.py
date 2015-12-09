# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0011_auto_20151207_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_extra',
            name='pic',
            field=models.ImageField(height_field=b'100px', width_field=b'100px', upload_to=b'upload'),
        ),
    ]
