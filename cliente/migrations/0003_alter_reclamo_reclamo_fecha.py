# Generated by Django 4.1.4 on 2022-12-11 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_reclamo_reclamo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='reclamo_fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 23, 9, 29, 419101), null=True),
        ),
    ]
