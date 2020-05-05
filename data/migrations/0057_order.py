# Generated by Django 3.0.2 on 2020-04-28 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0056_auto_20200428_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('payments', models.CharField(choices=[('COD', 'Thanh toán khi nhận hàng'), ('ATM/Internet Banking', 'ATM/Internet Banking'), ('Chuyển khoản', 'Chuyển khoản')], max_length=30)),
                ('sum_money', models.IntegerField()),
                ('tran_cost', models.IntegerField()),
                ('infouser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='data.InfoUser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]