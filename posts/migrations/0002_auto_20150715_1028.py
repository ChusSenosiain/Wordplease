# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(default=b'PUB', max_length=3, choices=[(b'PUB', b'Public'), (b'PRI', b'Private')]),
        ),
    ]
