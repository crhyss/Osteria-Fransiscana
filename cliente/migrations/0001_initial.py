# Generated by Django 4.1.2 on 2022-10-21 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('comuna_nombre', models.CharField(max_length=40)),
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
            name='Direccion',
            fields=[
                ('comuna_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='cliente.comuna')),
                ('codigo_postal', models.IntegerField(primary_key=True, serialize=False)),
                ('dir_calle', models.CharField(blank=True, max_length=50)),
                ('dir_nro', models.IntegerField(blank=True)),
                ('dir_depto', models.BooleanField(blank=True)),
                ('dir_depto_nro', models.IntegerField(blank=True, default=None, null=True)),
            ],
            bases=('cliente.comuna',),
        ),
        migrations.AddField(
            model_name='comuna',
            name='comuna_region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.region'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usr_nombre', models.CharField(max_length=40)),
                ('usr_apellido_pat', models.CharField(max_length=40)),
                ('usr_apellido_mat', models.CharField(max_length=40)),
                ('usr_pass', models.CharField(max_length=40)),
                ('usr_correo', models.EmailField(max_length=100)),
                ('usr_activo', models.BooleanField(default=True)),
                ('usr_tipo', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='cliente.tipo_usuario')),
                ('usr_direccion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.AutoField(primary_key=True, serialize=False)),
                ('local_activo', models.BooleanField(default=True)),
                ('local_hora_aper', models.DateTimeField()),
                ('local_hora_cierr', models.DateTimeField()),
                ('local_fono', models.IntegerField()),
                ('locar_direccion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.direccion')),
            ],
        ),
    ]
