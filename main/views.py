from django.shortcuts import render
from .models import Product

def show_main(request):
        context = {
            'name': 'dyas',
            'price': '50000',
            'description': 'Dyas Commerce adalah platform online inovatif yang dikhususkan untuk penjualan berbagai fitur game, termasuk avatar, pakaian karakter, aksesoris, dan item virtual lainnya yang dapat digunakan dalam berbagai permainan online. Kami menyediakan koleksi eksklusif yang dirancang khusus untuk memberikan pengalaman bermain game yang lebih personal dan menarik. Dengan pilihan yang beragam, para gamer dapat menyesuaikan tampilan karakter mereka sesuai dengan gaya dan kepribadian unik mereka, menjadikan setiap momen dalam permainan lebih hidup dan penuh warna.\n'
                            '\t Selain itu, Dyas Commerce juga menawarkan berbagai fitur tambahan seperti paket peningkatan level, item langka, dan konten premium lainnya yang semuanya dapat diakses dengan mudah melalui platform kami. Kami berkomitmen untuk menyediakan produk berkualitas tinggi dengan harga yang bersaing, serta didukung oleh layanan pelanggan yang responsif dan profesional. Tujuan kami adalah memberikan pengalaman belanja yang menyenangkan dan memuaskan bagi semua pengguna, sehingga mereka dapat menikmati permainan favorit mereka dengan lebih maksimal.',
            'category': 'Game',
            'additional_features': "Kami juga menawarkan berbagai fitur tambahan seperti paket peningkatan level, item langka, dan konten premium lainnya yang semuanya dapat diakses dengan mudah melalui platform kami."
        }
        return render(request, "main.html", context)
