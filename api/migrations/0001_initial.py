# Generated by Django 5.1.2 on 2024-10-21 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('genero_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_genero', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuarios_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=255)),
                ('fk_Generos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.generos')),
            ],
            options={
                'db_table': 'Uusuarios',
            },
        ),
    ]
