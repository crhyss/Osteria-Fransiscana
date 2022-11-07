# Generated by Django 4.1.2 on 2022-11-03 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_prod',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_prod', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('prod_nombre', models.CharField(max_length=100)),
                ('prod_descri', models.CharField(max_length=200)),
                ('prod_precio_ba', models.IntegerField()),
                ('prod_precio_of', models.IntegerField()),
                ('prod_imagen', models.FileField(default=None, upload_to='productos/')),
                ('prod_categoria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='productos.categoria_prod')),
            ],
        ),
    ]
