from django.contrib import admin
from shop.models import Groceries, Makeup, Mobile_phones, Skincare, Perfume, HomeAppliances

class ProductAdmin(admin.ModelAdmin):
    list_display= ['product_name', 'description', 'price']
    date_hierarchy= 'receive_at'
    actions_on_top= True
    list_filter= ['product_name', 'price', 'receive_at']
    search_fields= ['product_name', 'price']
    save_as= True
    save_as_top= True
admin.site.register(Groceries, ProductAdmin)
admin.site.register(Makeup, ProductAdmin)
@admin.register(Mobile_phones)
class Mobile_phonesAdmin(admin.ModelAdmin):
    list_display= ['model_name', 'description', 'price']
    date_hierarchy= 'receive_at'
    actions_on_top= True
    list_filter= ['model_name', 'price', 'receive_at']
    search_fields= ['model_name', 'price']
    save_as= True
    save_as_top= True

class SecondProductAdmin(admin.ModelAdmin):
    list_display= ['product_name', 'details', 'price']
    date_hierarchy= 'receive_at'
    actions_on_top= True
    list_filter= ['product_name', 'price', 'receive_at']
    search_fields= ['product_name', 'price']
    save_as= True
    save_as_top= True

admin.site.register(Skincare, SecondProductAdmin)
admin.site.register(Perfume, SecondProductAdmin)
admin.site.register(HomeAppliances, SecondProductAdmin)