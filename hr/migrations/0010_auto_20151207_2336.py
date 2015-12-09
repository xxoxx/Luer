# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_employee_extra_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_extra',
            name='pic',
            field=models.ImageField(height_field=100, width_field=100, upload_to=b'upload'),
        ),
    ]
