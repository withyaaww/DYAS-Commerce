from django.shortcuts import render, redirect, reverse
from main.forms import ProductForm
from main.models import Product

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products,
        'name': request.user.username,
        'price': 50000,
        'category': 'Handmade Crochet Flowers',
        'stock': 100,
        'description': 'DYA\'S Flowers adalah platform online yang menjual bunga rajut handmade yang indah dan unik. Setiap bunga dibuat dengan hati-hati dan penuh cinta, menjadikannya hadiah sempurna atau dekorasi cantik untuk rumah Anda.\n'
                       '\t Kami juga menawarkan berbagai varian bunga rajut dalam berbagai warna dan ukuran, sehingga pelanggan dapat memilih sesuai dengan keinginan mereka.',
        'additional_features': "Selain produk-produk unik, kami juga menyediakan paket custom untuk bunga rajut yang disesuaikan dengan permintaan Anda.",
        'last_login': request.COOKIES.get('last_login', ''),
    }
    return render(request, "main.html", context)

def create_flowers(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form = form.save(commit=False)
        form.user = request.user
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
    data = Product.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_pesanan(request, id):
    # Ambil data produk berdasarkan id yang diterima dari URL
    product = Product.objects.get(pk=id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman utama
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_pesanan.html", context)


def delete_pesanan(request, id):
    # Ambil produk berdasarkan id yang diterima dari URL
    pesanan = Product.objects.get(pk=id)

    # Hapus produk
    pesanan.delete()

    # Kembali ke halaman utama
    return HttpResponseRedirect(reverse('main:show_main'))
