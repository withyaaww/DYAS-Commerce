from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()

    context = {
        'products': products,
        'name': 'DYA\'S Flowers',
        'price': 50000,
        'category': 'Handmade Crochet Flowers',
        'stock': 100,
        'description': 'DYA\'S Crochet Flowers adalah platform online yang menjual bunga rajut handmade yang indah dan unik. Setiap bunga dibuat dengan hati-hati dan penuh cinta, menjadikannya hadiah sempurna atau dekorasi cantik untuk rumah Anda.\n'
                       '\t Kami juga menawarkan berbagai varian bunga rajut dalam berbagai warna dan ukuran, sehingga pelanggan dapat memilih sesuai dengan keinginan mereka.',
        'additional_features': "Selain produk-produk unik, kami juga menyediakan paket custom untuk bunga rajut yang disesuaikan dengan permintaan Anda."
    }
    return render(request, "main.html", context)

def create_flowers(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_flowers.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk="2365d94e-8370-4bf3-aba3-a12e2ad76e62")
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk="2365d94e-8370-4bf3-aba3-a12e2ad76e62")
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
