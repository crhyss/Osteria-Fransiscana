# Generated by Django 4.0.2 on 2022-09-28 23:14

from django.db import migrations, models


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
    ]
