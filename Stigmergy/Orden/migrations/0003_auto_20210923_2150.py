# Generated by Django 2.2 on 2021-09-24 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0002_auto_20210923_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='hubRecepción',
            new_name='hubRecepcion',
        ),
    ]