# Generated by Django 3.0.2 on 2020-04-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_imageofpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageofpost',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
