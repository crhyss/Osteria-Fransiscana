# Generated by Django 4.1.3 on 2022-12-03 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0010_alter_boleta_bta_fecha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Boleta',
        ),
        migrations.DeleteModel(
            name='Estado_venta',
        ),
        migrations.DeleteModel(
            name='Tipo_venta',
        ),
    ]