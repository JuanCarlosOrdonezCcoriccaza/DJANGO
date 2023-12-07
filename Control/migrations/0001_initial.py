# Generated by Django 4.2.7 on 2023-11-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('idConductor', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=9)),
                ('Licencia', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=9)),
            ],
        ),
    ]