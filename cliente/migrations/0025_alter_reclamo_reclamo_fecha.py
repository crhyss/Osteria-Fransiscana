# Generated by Django 4.0.6 on 2022-11-21 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0024_alter_reclamo_reclamo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='reclamo_fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 20, 23, 38, 1, 683751), null=True),
        ),
    ]