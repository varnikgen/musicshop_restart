# Generated by Django 4.0 on 2022-01-21 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0003_album_out_of_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicshop.cart', verbose_name='Корзина'),
        ),
    ]