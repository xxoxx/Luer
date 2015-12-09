# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_salary_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee_extra',
            options={'permissions': (('search_info_all', 'search_info_all'),)},
        ),
    ]
