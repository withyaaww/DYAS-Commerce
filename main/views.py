from django.shortcuts import render, redirect
from main.forms import MoodEntryForm
from main.models import MoodEntry
from .models import Product

from django.http import HttpResponse
from django.core import serializers


def show_main(request):
        mood_entries = MoodEntry.objects.all()

        context = {
            'name': 'dyas',
            'price': 50000,
            'category': 'Game',
            'stock':100,
            'description': 'Dyas Commerce adalah platform online inovatif yang dikhususkan untuk penjualan berbagai fitur game, termasuk avatar, pakaian karakter, aksesoris, dan item virtual lainnya yang dapat digunakan dalam berbagai permainan online. Kami menyediakan koleksi eksklusif yang dirancang khusus untuk memberikan pengalaman bermain game yang lebih personal dan menarik. Dengan pilihan yang beragam, para gamer dapat menyesuaikan tampilan karakter mereka sesuai dengan gaya dan kepribadian unik mereka, menjadikan setiap momen dalam permainan lebih hidup dan penuh warna.\n'
                            '\t Selain itu, Dyas Commerce juga menawarkan berbagai fitur tambahan seperti paket peningkatan level, item langka, dan konten premium lainnya yang semuanya dapat diakses dengan mudah melalui platform kami. Kami berkomitmen untuk menyediakan produk berkualitas tinggi dengan harga yang bersaing, serta didukung oleh layanan pelanggan yang responsif dan profesional. Tujuan kami adalah memberikan pengalaman belanja yang menyenangkan dan memuaskan bagi semua pengguna, sehingga mereka dapat menikmati permainan favorit mereka dengan lebih maksimal.',
            'mood_entries': mood_entries,
            'additional_features': "Kami juga menawarkan berbagai fitur tambahan seperti paket peningkatan level, item langka, dan konten premium lainnya yang semuanya dapat diakses dengan mudah melalui platform kami."
        }
        return render(request, "main.html", context)

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")