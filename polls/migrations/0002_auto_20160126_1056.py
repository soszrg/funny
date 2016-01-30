# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='choice',
        ),
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]
