# Generated by Django 3.2.9 on 2021-12-13 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('numeroDeDocumento', models.IntegerField()),
                ('numeroDeLicencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('numeroDeDocumento', models.IntegerField()),
                ('vacunado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ubicacion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40)),
                ('empresa', models.CharField(max_length=40)),
                ('capacidad', models.IntegerField()),
                ('patente', models.IntegerField()),
            ],
        ),
    ]
