# Generated by Django 3.0.2 on 2020-04-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20200407_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]