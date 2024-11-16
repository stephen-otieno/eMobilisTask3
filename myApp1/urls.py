from project1 import urls
from django.urls import path
from. import views

urlpatterns =[

    path('', views.home, name='home'),
    path('brand/', views.brand, name='brand_page'),
    path('insert/', views.insert_data, name='insert'),





]