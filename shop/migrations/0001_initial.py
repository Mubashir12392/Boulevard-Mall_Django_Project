# Generated by Django 4.1.7 on 2023-03-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAppliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images/')),
                ('company_name', models.CharField(max_length=20)),
                ('available_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('ordered_new_stock', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], max_length=10)),
                ('monthly_sale', models.PositiveIntegerField(blank=True, null=True)),
                ('receive_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Makeup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images/')),
                ('left_quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('Monthly_sale', models.PositiveIntegerField()),
                ('ordered_new_stock', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], max_length=10)),
                ('receive_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile_phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images/')),
                ('company_name', models.CharField(max_length=20)),
                ('processor_name', models.CharField(max_length=20)),
                ('storage_capacity', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField(default=0)),
                ('monthly_sale', models.PositiveIntegerField(default=0)),
                ('left_stock', models.PositiveIntegerField(default=0)),
                ('ordered_new_stock', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], max_length=10)),
                ('receive_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images/')),
                ('company_name', models.CharField(max_length=20)),
                ('available_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('ordered_new_stock', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], max_length=10)),
                ('monthly_sale', models.PositiveIntegerField(blank=True, null=True)),
                ('receive_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skincare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images/')),
                ('company_name', models.CharField(max_length=20)),
                ('available_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('ordered_new_stock', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], max_length=10)),
                ('monthly_sale', models.PositiveIntegerField(blank=True, null=True)),
                ('receive_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]