# Generated by Django 3.0.2 on 2020-04-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20200406_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Star Wars', 'Star Wars'), ('Ninjago', 'Ninjago'), ('City', 'City'), ('Minecraft', 'Minecraft'), ('Series', 'Series'), ('Classic', 'Classic'), ('MOC', 'MOC'), ('Minifigures', 'Minifigures'), ('CyberPunk', 'CyberPunk'), ('Khác', 'Khác')], max_length=50),
        ),
    ]
