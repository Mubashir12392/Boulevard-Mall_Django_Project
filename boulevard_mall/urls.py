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
from shop.views import boulevard,shoppingcart,shopproducts,checkout,feature,contact,login,register


urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/',boulevard, name='homepage'),
    path('home/cart/',shoppingcart, name='cart'),
    path('home/shop/',shopproducts,name='shop'),
    path('home/cart/checkout/',checkout, name='checkout'),
    path('home/feature_products/',feature, name='feature'),
    path('home/contact/',contact, name='contact'),
    path('home/login/',login,name='login'),
    path('home/register/', register,name='register')

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_URL)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
