# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0008_auto_20151207_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_extra',
            name='pic',
            field=models.ImageField(default=datetime.datetime(2015, 12, 7, 14, 33, 28, 149258, tzinfo=utc), upload_to=b'upload'),
            preserve_default=False,
        ),
    ]
