# Generated by Django 3.0.2 on 2020-04-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20200406_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
