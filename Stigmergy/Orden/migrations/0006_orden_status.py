# Generated by Django 2.2 on 2021-09-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0005_auto_20210924_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='status',
            field=models.CharField(choices=[('ok', 'Ok'), ('pending', 'Pending'), ('failed', 'Failed')], default='pending', max_length=255),
        ),
    ]
