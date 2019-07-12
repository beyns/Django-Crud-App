from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
# Create your views here.


def product_detail_view(request):
    products = Product.objects.all()[:10]
    context = {
        'product': products
    }
    return render(request, "product/details.html", context)
