from django.shortcuts import render

from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]
    context = {
        'title': 'Главная',
        'products': products
    }

    return render(request, "geekshop/index.html", context)


def contacts(request):
    return render(request, 'geekshop/contact.html')
