# Generated by Django 4.0.6 on 2022-11-21 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0016_reserva_hora_reserva_alter_reclamo_reclamo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='reclamo_fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 20, 22, 3, 35, 355378), null=True),
        ),
    ]
