# Generated by Django 3.0.2 on 2020-04-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0047_auto_20200425_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]