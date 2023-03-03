from django.db import models

STOCK_CHOICES = [
    ("N", "No"),
    ("Y", "Yes"),
]

    
class Makeup(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="shop_images/", null=True, blank=True)
    left_quantity = models.PositiveIntegerField(blank= False, null=False)
    price = models.PositiveIntegerField(blank= False, null=False)
    Monthly_sale = models.PositiveIntegerField()
    ordered_new_stock = models.CharField(max_length=10, choices=STOCK_CHOICES)
    receive_at = models.DateField(auto_now_add=True, null=True, blank=True)


class Mobile_phones(models.Model):
    model_name = models.CharField(max_length=20)
    description = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="shop_images/", null=True, blank=True)
    company_name = models.CharField(max_length=20)
    processor_name = models.CharField(max_length=20)
    storage_capacity = models.CharField(max_length=10)
    price = models.PositiveIntegerField(default=0)
    monthly_sale = models.PositiveIntegerField(default=0)
    left_stock = models.PositiveIntegerField(default=0)
    ordered_new_stock = models.CharField(max_length=10, choices=STOCK_CHOICES)
    receive_at = models.DateField(auto_now_add=True, null=True, blank=True)
    
class Skincare(models.Model):
    product_name = models.CharField(max_length= 30)
    details = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to="shop_images/", null=True, blank=True)
    company_name = models.CharField(max_length=20, blank=False, null=False)
    available_stock = models.PositiveIntegerField(null=True, blank=True,)
    price = models.PositiveIntegerField(null=True, blank=True)
    ordered_new_stock = models.CharField(max_length=10, choices=STOCK_CHOICES)
    monthly_sale = models.PositiveIntegerField(null=True, blank=True)
    receive_at = models.DateField(auto_now_add=True, null=True, blank=True)

class Perfume(models.Model):
    product_name = models.CharField(max_length= 30)
    details = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to="shop_images/", null=True, blank=True)
    company_name = models.CharField(max_length=20, blank=False, null=False)
    available_stock = models.PositiveIntegerField(null=True, blank=True,)
    price = models.PositiveIntegerField(null=True, blank=True)
    ordered_new_stock = models.CharField(max_length=10, choices=STOCK_CHOICES)
    monthly_sale = models.PositiveIntegerField(null=True, blank=True)
    receive_at = models.DateField(auto_now_add=True, null=True, blank=True)

class HomeAppliances(models.Model):
    product_name = models.CharField(max_length= 30)
    details = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to="shop_images/", null=True, blank=True)
    company_name = models.CharField(max_length=20, blank=False, null=False)
    available_stock = models.PositiveIntegerField(null=True, blank=True,)
    price = models.PositiveIntegerField(null=True, blank=True)
    ordered_new_stock = models.CharField(max_length=10, choices=STOCK_CHOICES)
    monthly_sale = models.PositiveIntegerField(null=True, blank=True)
    receive_at = models.DateField(auto_now_add=True, null=True, blank=True)


