# Generated by Django 2.2 on 2021-09-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0004_auto_20210924_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='hubEntrega',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='hubRecepcion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='identificate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
