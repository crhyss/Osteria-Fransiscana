# Generated by Django 4.0.6 on 2022-11-21 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0012_remove_reserva_reserva_estado_mesa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='reclamo_fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 20, 21, 42, 33, 340570), null=True),
        ),
    ]
