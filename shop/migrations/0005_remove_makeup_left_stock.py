# Generated by Django 4.1.7 on 2023-02-16 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_makeup_left_quantity_makeup_price_per_pack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makeup',
            name='left_stock',
        ),
    ]