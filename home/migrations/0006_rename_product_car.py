# Generated by Django 4.2.4 on 2023-08-31 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_car_name_product_speed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Car',
        ),
    ]
