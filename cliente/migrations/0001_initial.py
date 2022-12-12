# Generated by Django 4.1.4 on 2022-12-11 02:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('user_correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo Electrónico')),
                ('user_nombre', models.CharField(max_length=40)),
                ('user_apellidos', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('comuna_nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('dir_calle', models.CharField(max_length=50)),
                ('dir_nro', models.PositiveIntegerField()),
                ('dir_depto', models.BooleanField(default=False)),
                ('dir_depto_nro', models.PositiveIntegerField(blank=True, null=True)),
                ('dir_comuna', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoMesa',
            fields=[
                ('id_estado_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('estado_mesa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_evento', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.AutoField(primary_key=True, serialize=False)),
                ('local_hora_aper', models.TimeField()),
                ('local_hora_cierr', models.TimeField()),
                ('local_fono', models.IntegerField()),
                ('local_activo', models.BooleanField(default=True)),
                ('local_direccion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('mesa_nro', models.IntegerField()),
                ('mesa_sillas', models.IntegerField()),
                ('mesa_estado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.estadomesa')),
                ('mesa_local', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cliente.local')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id_reclamos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('apellido', models.CharField(max_length=40, null=True)),
                ('reclamo_fecha', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 23, 9, 6, 902204), null=True)),
                ('reclamo_descrip', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('region_nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id_tipo_usr', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_usr', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reserva', models.DateField(max_length=40)),
                ('hora_reserva', models.TimeField(blank=True, null=True)),
                ('reserva_evento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.evento')),
                ('reserva_mesa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.mesa')),
                ('reserva_usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='comuna_region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.region'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.direccion'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.tipo_usuario'),
        ),
    ]
