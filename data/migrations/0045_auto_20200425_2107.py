# Generated by Django 3.0.2 on 2020-04-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0044_infouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='phonenumber',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
