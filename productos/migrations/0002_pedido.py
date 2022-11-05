# Generated by Django 4.0.6 on 2022-11-05 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('pedido_modif', models.CharField(max_length=200)),
                ('pedido_listo', models.BooleanField(default=False)),
                ('pedido_producto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]
