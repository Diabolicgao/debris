# Generated by Django 3.0.2 on 2020-04-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='/media/event.jpg', null=True, upload_to=''),
        ),
    ]