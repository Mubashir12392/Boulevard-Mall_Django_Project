"""boulevard_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import pakistan_store
from shop.views import shop_categories
from shop.views import grocery
from shop.views import makeup
from shop.views import phone
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', pakistan_store, name='homepage'),
    path('home/shop/', shop_categories, name='shop_page'),
    path('home/shop/grocery/', grocery, name='grocery_shop'),
    path('home/shop/makeup/', makeup, name='makeup_shop'),
    path('home/shop/mobilephone/', phone, name='phone_shop')

]
