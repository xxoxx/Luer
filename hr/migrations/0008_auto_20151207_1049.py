# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_auto_20151206_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee_extra',
            options={'permissions': (('search_info_all', 'search_info_all'), ('attendence_manage', 'attendence_manage'))},
        ),
    ]
