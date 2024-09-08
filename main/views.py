from django.shortcuts import render
from .models import Product

def show_product(request):
    product = Product.objects.first()
    if product:
        context = {
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'stock': product.stock,
            'category': product.category,
            'additional_features': "Kami juga menawarkan berbagai fitur tambahan seperti paket peningkatan level, item langka, dan konten premium lainnya yang semuanya dapat diakses dengan mudah melalui platform kami."
        }
    else:
        context = {
            'error': "Product not found.",
        }
    return render(request, "product.html", context)
