# Generated by Django 3.0.2 on 2020-04-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0039_cart_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]