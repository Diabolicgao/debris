# Generated by Django 3.0.2 on 2020-04-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_auto_20200419_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Ninjago', 'Ninjago'), ('City', 'City'), ('Động vật', 'Animal'), ('Fantasy', 'Fantasy'), ('Star Wars', 'Star Wars'), ('Minecraft', 'Minecraft'), ('Overwatch', 'Overwatch'), ('Vehicle', 'Vehicle'), ('Custom', 'Custom'), ('Technic', 'Technic'), ('Rồng', 'Dragon'), ('Lâu đài', 'Castle'), ('CyberPunk', 'CyberPunk'), ('DC', 'DC'), ('Marvel', 'Marvel'), ('Vòng tay', 'Bracelet'), ('Tủ đựng', 'Chest'), ('Hộp kính', 'Glass Box'), ('Móc chìa khóa', 'Key Chain'), ('Gạch', 'Brick')], max_length=50),
        ),
    ]
