from django.contrib import admin
from django.urls import path, include
from .views import GasPriceView


urlpatterns = [
    path('gas_price', GasPriceView.get_gas_price, name='gas_price'),
]
