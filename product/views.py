from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product
# Create your views here.


def create_product(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "product/details.html", context)


def product_detail_view(request):
    products = Product.objects.all()[:10]
    context = {
        'product': products
    }
    return render(request, "product/details.html", context)
