# Generated by Django 3.0.2 on 2020-04-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0061_auto_20200429_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payments',
            field=models.BooleanField(verbose_name='Thanh toán khi nhận hàng'),
        ),
    ]
