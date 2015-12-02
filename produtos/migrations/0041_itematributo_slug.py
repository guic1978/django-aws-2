# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0040_auto_20151201_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='itematributo',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
