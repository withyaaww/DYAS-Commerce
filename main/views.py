from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Widya Mutia Ichsan',
        'npm': '2306165912',
        'class': 'PBP E',
        'description': "Dya's Commerce adalah platform online inovatif yang dikhususkan untuk penjualan berbagai fitur game, termasuk avatar, pakaian karakter, aksesoris, dan item virtual lainnya yang dapat digunakan dalam berbagai permainan online. Kami menyediakan koleksi eksklusif yang dirancang khusus untuk memberikan pengalaman bermain game yang lebih personal dan menarik.",
        'additional_features': "Kami juga menawarkan berbagai fitur tambahan seperti paket peningkatan level, item langka, dan konten premium lainnya yang semuanya dapat diakses dengan mudah melalui platform kami. Tujuan kami adalah memberikan pengalaman belanja yang menyenangkan dan memuaskan bagi semua pengguna, sehingga mereka dapat menikmati permainan favorit mereka dengan lebih maksimal."
    }
    return render(request, "main.html", context)
