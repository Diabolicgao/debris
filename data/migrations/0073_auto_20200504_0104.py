# Generated by Django 3.0.2 on 2020-05-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0072_auto_20200504_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancel',
            field=models.BooleanField(default=False, verbose_name='Hủy'),
        ),
        migrations.AddField(
            model_name='order',
            name='exchange_scf',
            field=models.BooleanField(default=False, verbose_name='Giao dịch thành công'),
        ),
    ]
