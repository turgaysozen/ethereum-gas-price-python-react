from django.http.response import HttpResponse, JsonResponse
from .gas_price_estimation import GasPrice


class GasPriceView:
    def get_gas_price(request):
        gas_price = GasPrice()
        gas_price = gas_price.estimate_gas_price()
        if gas_price:
            return JsonResponse(gas_price, status=200)
        else:
            return JsonResponse(status=500)