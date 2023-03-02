from django.shortcuts import render,reverse, redirect
from shop.models import Groceries, Makeup, Mobile_phones, Skincare, Perfume, HomeAppliances
# Create your views here.

def pakistan_store(request):
    return render(request, 'main_page.html')

def shop_categories(request):
    return render(request, 'shop_page.html')

def grocery(request):
    groceries = Groceries.objects.all()
    context = {
        'groceries' : groceries
    }
    return render(request, 'grocery.html', context=context)

def makeup(request):
    makeup = Makeup.objects.all()
    context = {
        'makeup' : makeup
    }
    return render(request, 'makeup.html', context=context )

def phone(request):
    phone = Mobile_phones.objects.all()
    context = {
        'phone' : phone
    }
    return render(request, 'phone.html', context=context)


def skin_care(request):
    product = Skincare.objects.all()
    context = {
        'product' : product
    }
    return render(request, 'skin_care.html', context=context)

def perfume(request):
    if request.method == "GET":
        product = Perfume.objects.all()
        context = {
            'product' : product
        }
        return render(request, 'perfume.html', context=context)
    return redirect(reverse('shop_page'))

def home_appliances(request):
    if request.method == "GET":
        product = HomeAppliances.objects.all() 
        context = {
            'product' :  product
        }
        return render(request, 'home_appliances.html', context=context)
    return redirect(reverse('shop_page'))