# Generated by Django 3.0.2 on 2020-05-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0070_auto_20200501_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('ninjago', 'ninjago'), ('city', 'city'), ('animal', 'animal'), ('fantasy', 'fantasy'), ('star_wars', 'star_wars'), ('overwatch', 'overwatch'), ('item', 'item'), ('vehicle', 'vehicle'), ('custom', 'custom'), ('technic', 'technic'), ('dragon', 'dragon'), ('castle', 'castle'), ('cyberpunk', 'cyberpunk'), ('dc', 'dc'), ('marvel', 'marvel'), ('brick', 'brick')], max_length=50),
        ),
    ]
