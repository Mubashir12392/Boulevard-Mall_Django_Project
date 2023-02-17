from django.db import models

class Groceries(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)
    left_quantity_in_packets = models.SmallIntegerField(blank=True, null=True)
    left_quantity_in_weight = models.CharField(max_length=10, blank=True, null=True)
    left_quantity_in_volume = models.CharField(max_length=10, blank=True, null=True)
    price = models.CharField(max_length=10,default=0)
    monthly_sale = models.CharField(max_length=20)
    left_stock = models.CharField(max_length=30)
    ordered_new_stock = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.product_name
    
class Makeup(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)
    left_quantity = models.SmallIntegerField(blank= False, null=False)
    price = models.SmallIntegerField(blank= False, null=False)
    Monthly_sale = models.CharField(max_length=20)
    ordered_new_stock = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.product_name
    
class Mobile_phones(models.Model):
    model_name = models.CharField(max_length=20)
    description = models.CharField(max_length=30, blank=True, null=True)
    company_name = models.CharField(max_length=20)
    processor_name = models.CharField(max_length=20)
    storage_capacity = models.CharField(max_length=10)
    price = models.SmallIntegerField(default=0)
    monthly_sale = models.SmallIntegerField(default=0)
    left_stock = models.SmallIntegerField(default=0)
    ordered_new_stock = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.model_name

