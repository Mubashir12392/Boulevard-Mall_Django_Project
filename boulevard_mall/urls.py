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
from django.conf import settings
from django.conf.urls.static import static
from shop.views import pakistan_store, shop_categories, grocery, makeup, phone, skin_care, perfume, home_appliances
from core.views import  home_core
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', pakistan_store, name='homepage'),
    path('home/shop/', shop_categories, name='shop_page'),
    path('home/shop/grocery/', grocery, name='grocery_shop'),
    path('home/shop/makeup/', makeup, name='makeup_shop'),
    path('home/shop/mobilephone/', phone, name='phone_shop'),
    path('home/shop/skincare/', skin_care, name='skin-care'),
    path('home/shop/perfume/', perfume, name='perfume'),
    path('home/shop/home/appliances', home_appliances, name='home-appliances'),
    path('', home_core, name='home-core'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_URL)
 
