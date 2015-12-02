# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0041_itematributo_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itematributo',
            unique_together=set([('atributo', 'slug')]),
        ),
    ]
