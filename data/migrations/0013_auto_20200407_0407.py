# Generated by Django 3.0.2 on 2020-04-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20200406_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Ninjago', 'Ninjago'), ('City', 'City'), ('Star Wars', 'Star Wars'), ('Spider-Man', 'Spider-Man'), ('Bat-Man', 'Bat-Man'), ('Iron-Man', 'Iron-Man'), ('Harry-Potter', 'Harry-Potter'), ('Minecraft', 'Minecraft'), ('Overwatch', 'Overwatch'), ('Xe', 'Xe'), ('Custom', 'Custom'), ('Máy Bay', 'Máy Bay'), ('Rồng', 'Rồng'), ('Lâu Đài', 'Lâu Đài'), ('CyberPunk', 'CyberPunk'), ('Khác', 'Khác')], max_length=50),
        ),
    ]