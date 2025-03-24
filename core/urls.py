"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
import django.views.static
from core.settings import DEBUG, STATIC_ROOT, MEDIA_ROOT
from ttw.views import index, MyDataClass

urlpatterns = [
        path('admin/', admin.site.urls),
        path("", index, name="index"),

        path("weather-data", MyDataClass.as_view(), name="weather-data"),
        path("exchange", ExchangeClass.as_view(), name="exchange-data"),

        re_path(r'^static/(?P<path>.*)', django.views.static.serve, {'document_root': STATIC_ROOT,
                                                                     'show_indexes': DEBUG}),
        re_path(r'^media/(?P<path>.*)', django.views.static.serve, {'document_root': MEDIA_ROOT,
                                                                    'show_indexes': DEBUG}),
]
