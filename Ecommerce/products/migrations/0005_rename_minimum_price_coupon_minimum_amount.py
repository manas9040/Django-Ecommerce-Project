# Generated by Django 4.1.2 on 2023-01-16 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='minimum_price',
            new_name='minimum_amount',
        ),
    ]
