from django.shortcuts import render,reverse, redirect
from shop.models import Makeup, Mobile_phones, Skincare, Perfume, HomeAppliances
# Create your views here.

def boulevard(request):
    return render(request, 'index.html')

def shoppingcart(request):
    return render(request, 'cart.html')

def shopproducts(request):
    return render(request,'shop.html')

def checkout(request):
    return render(request,'checkout.html')

def feature(request):
    return render(request, 'feature.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html') 