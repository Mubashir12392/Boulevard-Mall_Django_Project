# Generated by Django 4.1.7 on 2023-02-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_name_groceries_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makeup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('Monthly_sale', models.CharField(max_length=20)),
                ('left_stock', models.CharField(max_length=20)),
                ('ordered_new_stock', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='groceries',
            old_name='quantity_in_packets',
            new_name='left_quantity_in_packets',
        ),
        migrations.RenameField(
            model_name='groceries',
            old_name='quantity_in_volume',
            new_name='left_quantity_in_volume',
        ),
        migrations.RenameField(
            model_name='groceries',
            old_name='quantity_in_weight',
            new_name='left_quantity_in_weight',
        ),
        migrations.RemoveField(
            model_name='groceries',
            name='total_sale_in_stock',
        ),
        migrations.AddField(
            model_name='groceries',
            name='left_stock',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groceries',
            name='monthly_sale',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groceries',
            name='ordered_new_stock',
            field=models.CharField(default='yes', max_length=10),
            preserve_default=False,
        ),
    ]