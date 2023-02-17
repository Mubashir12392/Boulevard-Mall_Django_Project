from django.shortcuts import render
from shop.models import Groceries
from shop.models import Makeup
from shop.models import Mobile_phones
# Create your views here.

def pakistan_store(request):
    return render(request, 'main_page.html')

def shop_categories(request):
    return render(request, 'shop_page.html')

def grocery(request):
    groceri = Groceries.objects.all()
    context = {
        'groceri' : groceri
    }
    return render(request, 'grocery.html', context=context)

def makeup(request):
    beauty = Makeup.objects.all()
    context = {
        'makeup' : beauty
    }
    return render(request, 'makeup.html', context=context )

def phone(request):
    phone = Mobile_phones.objects.all()
    context = {
        'phone' : phone
    }
    return render(request, 'phone.html', context=context)



