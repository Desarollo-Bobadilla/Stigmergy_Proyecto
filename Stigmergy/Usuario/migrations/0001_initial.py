# Generated by Django 2.2 on 2021-09-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('preferencias', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]