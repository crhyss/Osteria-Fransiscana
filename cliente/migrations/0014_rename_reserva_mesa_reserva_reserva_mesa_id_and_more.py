# Generated by Django 4.0.6 on 2022-11-21 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0013_alter_reclamo_reclamo_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='reserva_mesa',
            new_name='reserva_mesa_id',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='reserva_usuario',
            new_name='reserva_usuario_id',
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='reclamo_fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 20, 21, 43, 35, 193250), null=True),
        ),
    ]