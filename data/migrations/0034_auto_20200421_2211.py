# Generated by Django 3.0.2 on 2020-04-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0033_auto_20200421_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=350, null=True),
        ),
    ]
