from project1 import urls
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('brands/', views.brands, name='brand_page'),
    path('insert/', views.insert_data, name='insert'),





]