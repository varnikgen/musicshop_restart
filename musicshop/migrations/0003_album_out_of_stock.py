# Generated by Django 4.0 on 2022-01-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0002_alter_cart_final_price_alter_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='out_of_stock',
            field=models.BooleanField(default=False, verbose_name='Нет в наличии'),
        ),
    ]