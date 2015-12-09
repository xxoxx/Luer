# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0015_auto_20151208_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee_extra',
            options={'permissions': (('department_manager', 'department_manager'), ('personnel_assistant', 'personnel_assistant'), ('personnel_manager', 'personnel_manager'), ('admin', 'admin'))},
        ),
    ]
