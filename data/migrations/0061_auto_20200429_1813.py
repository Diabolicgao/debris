# Generated by Django 3.0.2 on 2020-04-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0060_auto_20200429_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payments',
            field=models.BooleanField(db_column='Thanh toán khi nhận hàng', verbose_name='Thanh toán khi nhận hàng'),
        ),
    ]
