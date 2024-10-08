<div align="center">
  <h2>𓍢ִ໋🌷͙֒₊˚*ੈ♡ Welcome to DYA'S ⸝⸝𓍢ִ໋ 🌷͙֒₊˚⋆</h2>
</div>     

![alt text](image-3.png)

***
**Nama**: Widya Mutia Ichsan  
**NPM**: 2306165912  
**Kelas**: PBP E  
--- 

Aplikasi PWS yang sudah di-deploy dapat diakses melalui tautan berikut:  
[http://pbp.cs.ui.ac.id/widya.mutia/dyascommerce](http://pbp.cs.ui.ac.id/widya.mutia/dyascommerce)

---
#                   Table of Contents
- [TUGAS INDIVIDU 2](#tugas-individu-2)
- [TUGAS INDIVIDU 3](#tugas-individu-3)
- [TUGAS INDIVIDU 4](#tugas-individu-4)
- [TUGAS INDIVIDU 5](#tugas-individu-5)
- [TUGAS INDIVIDU 6](#tugas-individu-6)


***
#                  TUGAS INDIVIDU 2

### Penjelasan Implementasi Tugas *Step-by-Step* (Bukan Hanya Sekadar Mengikuti Tutorial)

**1. Membuat sebuah proyek Django baru.**  
Untuk langkah pertama saya membuat sebuah proyek Django bernama *dyascommerce* menggunakan command:  
`django-admin startproject dyascommerce`

**2. Membuat aplikasi dengan nama main pada proyek tersebut.**  
Langkah kedua yaitu membuat aplikasi baru bernama **main** di dalam proyek menggunakan perintah:  
`python manage.py startapp main`

**3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**  
Langkah ke-3 yaitu menambahkan 'main' dan 'dyascommerce' ke dalam daftar aplikasi:  
```python
INSTALLED_APPS = [
    ...,
    'main',
    'dyas_commerce'
]
```

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**  
`name : CharField`  
`price : IntegerField`  
`description : TextField`  

Akan tetapi saya juga menambahkan 2 atribut yaitu:  
`stock : IntegerField`  
`category : CharField`  
<!-- `image : ImageField` -->

**5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**<br>
Pada langkah ke-5, saya membuka berkas views.py yang terletak pada direktori main, kemudian mendeklarasikan sebuah fungsi bernama *show_main*, yang akan menerima parameter *request*. Fungsi yang saya buat ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai sehingga akan mengembalikan ke dalam direktori template berisi file html yang akan menampilkan nama
    

**6. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.**

Pada langkah ini, saya perlu membuat routing di berkas `urls.py` pada aplikasi *main* untuk menghubungkan fungsi yang sudah dibuat di `views.py`.

Langkah yang dilakukan adalah dengan menambahkan kode berikut di `urls.py` aplikasi *main*:

```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Setelah itu, saya akan menambahkan rute URL di `urls.py` proyek untuk menghubungkan aplikasi *main* dengan proyek secara keseluruhan. Pastikan membuka berkas `urls.py` di direktori proyek utama, bukan di direktori aplikasi *main*.

Impor fungsi `include` dari `django.urls`:

```python
from django.urls import path, include
```

Kemudian, saya menambahkan rute URL berikut untuk mengarahkan ke tampilan dari aplikasi *main*:

```python
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```

**7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**<br>
Pada tahap ini, saya melakukan deploy ke PWS dengan menambahkan alamat PWS ke dalam repository menggunakan perintah:<br> 
    `git remote add pws https://pbp.cs.ui.ac.id/widya.mutia/dyascommerce.`

Selanjutnya, saya mengubah nama branch dari "master" ke "main" menggunakan perintah:<br>
    `git branch -M master.`

Setelah itu, saya melakukan push ke PWS dengan perintah 
    `git push pws master`
sehingga aplikasi saya dapat diakses oleh teman-teman melalui internet.

***

### Bagan yang Berisi Request Client ke Web Aplikasi Berbasis Django Beserta Responnya

Buat bagan yang menunjukkan alur dari request client ke web aplikasi Django dan respons yang dikembalikan. Jelaskan bagaimana `urls.py`, `views.py`, `models.py`, dan berkas `html` saling terkait dalam proses ini.

![alt text](image-1.png)

***

### Penjelasan Fungsi Git dalam Pengembangan Perangkat Lunak

Fungsi git dalam pengembangan perangkat lunak yaitu sebagai sistem kontrol yang esensial yang digunakan untuk mengelola perubahan kode secara efektif, selain itu juga memungkinkan pengembang untuk mencatat dan melacak setiap perubahan yang dilakukan pada kode sumber. Dengan Git, pengembang dapat mengatur berbagai versi aplikasi, yang sangat berguna untuk memantau perkembangan proyek dari waktu ke waktu.

Selain itu juga, dengan menggunakan Git dapat mengurangi risiko kehilangan data. Karena Git menyimpan riwayat lengkap dari setiap perubahan yang dilakukan, sehingga pengembang dapat dengan mudah kembali ke versi sebelumnya jika diperlukan. Hal ini membantu dalam memulihkan data yang mungkin hilang atau terhapus secara tidak sengaja. Dengan Git, proses pemulihan data menjadi lebih mudah dan aman, memberikan rasa percaya diri kepada pengembang bahwa kode mereka tetap terlindungi dan dapat dipulihkan jika terjadi masalah.

### Dari Semua Framework yang Ada, Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Karena Django adalah framework yang populer dan banyak digunakan dalam pengembangan web. Selain itu Django memiliki fitur-fitur yang memudahkan pengembangan aplikasi web, seperti ORM dan template engine.

### Mengapa Model pada Django Disebut sebagai ORM?

Karena berfungsi sebagai jembatan antara objek-objek dalam kode Python dan tabel-tabel dalam database relasional.

---
#         TUGAS INDIVIDU 3

 ### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?<br>
    
karena untuk mengumpulkan, mengolah, dan menganalisis data pelanggan secara efektif, sehingga membantu perusahaan membuat keputusan bisnis yang lebih cerdas dan meningkatkan efisiensi operasional.

 ### 2. mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

 Keduanya sama-sama bagus, akan tetapi jika dibandingkan JSON lebih populer karena kemudahannya, kinerjanya yang lebih cepat, dan kompatibilitasnya yang baik dengan JS, membuatnya ideal untuk pengembangan web modern. Namun, XML masih memiliki kelebihan dalam struktur data yang lebih kompleks dan interoperabilitas antar platform, sehingga masih digunakan dalam beberapa konteks tertentu.

 ### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

 fungsi dari `is_valid()` yaitu untuk memvalidasi data input dari user, kita memerlukan method tersebut karena untuk memastikan data yang diterima aman, sesuai, dan sia diproses atau disimpan.<br> 
 
 Selain itu method ini juga membantu dalam pengelolaan kesalahan input yang bisa ditampilkan kembali kepada pengguna

 ### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita memerlukan `csrf_token` karena alasan keamanan. Token ini secara otomatis di-*generate* oleh Django untuk mencegah serangan **Cross-Site Request Forgery (CSRF)**, di mana penyerang dapat memanfaatkan sesi pengguna yang valid untuk mengirim permintaan tanpa izin pengguna.

 Jika kita **tidak menambahkan** `csrf_token`, maka penyerang dapat memalsukan permintaan atas nama pengguna tanpa sepengetahuan mereka.<br>
 
Selain itu permintaan berbahaya seperti perubahan data, penghapusan informasi penting, atau bahkan transaksi dapat dilakukan tanpa otorisasi pengguna.

### Cara penyerang memanfaatkannya yaitu dengan
membuat halaman atau skrip berbahaya yang ketika pengguna mengunjungi halaman tersebut, hal tersebut dapat mengirimkan permintaan tanpa otorisasi ke aplikasi Django yang sedang digunakan oleh pengguna yang telah login, sehingga terjadi manipulasi data atau tindakan lain yang tidak diinginkan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 ---

### **Step 1: Membuat Input Form**
1. **Buat Form**: Buat form dengan menggunakan `ModelForm` di `forms.py` 

2. **Buat Template**: Di `templates/create_flowers.html`, buat form dengan memasukkan `csrf_token`.
   

### **Step 2: Menambahkan Fungsi Views**
1. masuk ke views.py dan buat function baru untuk nampilin data dalam format XML, JSON, XML by ID dan JSON by ID(jangan lupa buat import `HttpResponse` dan `serializers`).

**XML View**:
   ```python
   from django.http import HttpResponse
   from django.core import serializers
   from .models import MoodEntry

   def show_xml(request):
       data = MoodEntry.objects.all()
       return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
   ```

**JSON View**
   ```python
   from django.http import JsonResponse

   def show_json(request):
       data = list(MoodEntry.objects.values())
       return JsonResponse(data, safe=False)
   ```

**XML by ID View**
   ```python
   def show_xml_by_id(request, id):
       try:
           mood_entry = MoodEntry.objects.get(pk=id)
           data = serializers.serialize('xml', [mood_entry])
           return HttpResponse(data, content_type='application/xml')
       except MoodEntry.DoesNotExist:
           return HttpResponse(status=404)
   ```

**JSON by ID View**
   ```python
   def show_json_by_id(request, id):
       try:
           mood_entry = MoodEntry.objects.get(pk=id)
           data = {
               'id': str(mood_entry.id),
               'nama_lengkap': mood_entry.nama_lengkap,
               'time': mood_entry.time,
               'deskripsi': mood_entry.deskripsi,
               'jumlah_character': mood_entry.jumlah_character
           }
           return JsonResponse(data)
       except MoodEntry.DoesNotExist:
           return JsonResponse({'error': 'Not found'}, status=404)
   ```

### **Step 3: Membuat Routing URL**
**Update `urls.py`**: nambahin path untuk views yang udah dibuat di `urls.py`.
  
   

---
### POSTMAN 

#### XML
![alt text](image-6.png)

#### JSON 
![alt text](image-7.png)

### XML by ID
![alt text](image-8.png)

### JSON by ID 
![alt text](image-9.png)

---
##      TUGAS INDIVIDU 4
---
### 1. **Perbedaan HttpResponseRedirect() dan redirect()**
`HttpResponseRedirect`: Hanya menerima URL langsung dan tidak memproses penamaan URL atau objek view.
`redirect`: Lebih fleksibel karena bisa menerima URL string, nama view, atau model instance.

### 2. **Cara menghubungkan model Product dengan User**
   Model Product dan User bisa dihubungkan dengan relasi `ForeignKey`. Dengan menggunakan `ForeignKey`, sebuah model Product bisa dikaitkan dengan banyak instance dari model User, sehingga hubungan antar kedua model ini dapat terhubung dengan baik. 

```python
...
from django.contrib.auth.models import User #pastikan sudah mengimpor ni terlebih dahulu
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```
### 3. Perbedaan antara Autentikasi dan Otorisasi saat Pengguna Login

**Autentikasi** adalah proses yang digunakan untuk memverifikasi identitas pengguna. Tujuannya adalah memastikan bahwa pengguna yang mencoba mengakses sistem atau aplikasi adalah orang yang benar-benar mereka klaim.

#### Contoh:
Saat pengguna login ke **Dyas Flowers**, mereka diminta untuk memasukkan username dan password. Django akan memeriksa username dan password yang dimasukkan terhadap database untuk memastikan apakah kredensial tersebut valid. Jika valid, Django akan mengizinkan pengguna untuk mengakses fitur dan halaman yang dilindungi.

Setelah pengguna berhasil melakukan autentikasi, **otorisasi** berfungsi untuk menentukan hak akses mereka dalam aplikasi. Django mengatur apa yang diizinkan dan tidak diizinkan bagi pengguna untuk dilakukan. Django menyediakan decorators seperti `@login_required`, yang memastikan hanya pengguna yang terautentikasi yang dapat mengakses halaman tertentu.


### 4. Bagaimana Django Mengingat Pengguna yang Telah Login dan Keamanan Cookies

Django mengingat pengguna yang telah login melalui sistem **session**, di mana ID pengguna disimpan dalam database dan dikirim ke browser sebagai **cookie**. Saat pengguna kembali, Django membaca cookie sesi untuk memverifikasi apakah pengguna masih terautentikasi. Untuk keamanan, Django menerapkan beberapa langkah, seperti menggunakan **secure cookies**, mengatur cookie agar tidak dapat diakses melalui JavaScript, dan menggunakan beberapa atribut untuk melindungi dari serangan CSRF.


### 5. **Langkah-langkah Implementasi Checklist**

1. **Step 1:**<br> Mengimplementasikan Fungsi Registrasi, Login, dan Logout dengan menggunakan **Django auth views** untuk membuat fitur registrasi, login dan logout, serta memastikan untuk menambahkan URL routing yang sesuai dalam `urls.py`.

2. **Step 2**<br> Membuat Dua Akun Pengguna. Setelah mengimplementasikan fungsi registrasi, buat dua akun pengguna secara manual, kemudian membuat tiga dummy data untuk masing-masing akun.


3. **Step 3: Menghubungkan Model Product dengan User** <br> Untuk menghubungkan model **Product** dengan model **User**, perlu menambahkan field `ForeignKey` dalam file model **Product**. Contoh implementasi dapat dilihat pada langkah [nomor 2](###2.-**Cara-menghubungkan-model-Product-dengan-User**).


4. **Step 4**<br> Menampilkan Informasi Pengguna yang Sedang Login, Untuk menampilkan informasi pengguna yang sedang login, dapat menggunakan cookie untuk menyimpan dan menampilkan waktu login terakhir, dengan cara menambahkan kode berikut dalam fungsi `show_main` yang ada di dalam view :

```python
def show_main(request):
    ...
    last_login = request.COOKIES.get('last_login')
    ...
```

pastikan bahwa sudah memperbarui isi dari file html

---
#           TUGAS INDIVIDU 5
---
## Urutan Prioritas CSS Selector

Dalam CSS, urutan prioritas pengambilan selector ditentukan oleh spesifisitas dan urutan penulisan. Berikut adalah urutan prioritas yang umum:

1. *Inline Styles*
2. *ID Selector*
3. *Class Selector*
4. *Element Selector*
5. *Universal Selector* <br>

kalo misal ada beberapa selector dengan spesifisitas yang sama, maka selector yang ditulis terakhir dalam CSS bakal diterapin.

## Pentingnya Responsive Design

Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena:

- *Aksesibilitas*
- *SEO yang Lebih Baik*
- *Pengalaman Pengguna*

### Contoh Aplikasi
- *Aplikasi Responsif*<br>
misal situs web seperti Amazon dan Facebook menerapkan desain responsif dengan baik.
- *Aplikasi Tidak Responsif*<br>
 misalnya ada beberapa situs berita lama tidak mendukung desain responsif, membuatnya sulit diakses melalui perangkat mobile.

## Perbedaan Margin, Border, dan Padding

- **Margin**: Ruang di luar batas elemen. Margin memisahkan elemen dari elemen lain.
- **Border**: Garis yang mengelilingi elemen. Border dapat memiliki warna dan ketebalan.
- **Padding**: Ruang di dalam batas elemen, antara konten dan border.

### Implementasi
contoh implementasi ketiga properti di atas dalam CSS yaitu:
```css
.element {
    margin: 20px; /* untuk mengatur margin */
    border: 1px solid black; /* untuk mengatur border */
    padding: 10px; /* untuk mengatur padding */
}
```

## Konsep Flexbox dan Grid Layout

### Flexbox
Flexbox adalah model layout CSS yang memungkinkan elemen dalam kontainer fleksibel untuk disusun secara efisien dalam satu dimensi (baris atau kolom). <br>

Fungsinya biasanya termasuk:
- Untuk menyusun elemen secara responsif.
- Untuk mengatur ruang antara elemen dengan mudah.

### Grid Layout
Grid Layout adalah model layout dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom.<br>

Fungsinya biasanya termasuk:
- Untuk membuat tata letak kompleks dengan lebih mudah.
- Untuk mengontrol ukuran dan posisi elemen secara lebih presisi.

## Implementasi Checklist

Untuk mengimplementasikan checklist di atas secara step-by-step:

---
1. Implementasikan fungsi untuk menghapus dan mengedit product.
ngebuat dua function di `views.py`:<br>

```python

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
```

Jangan lupa mastiin buat import `reserve` dan hubungin urlnya di `urls.py`

---

# Kustomisasi Desain pada Template HTML

Proyek ini bertujuan untuk menerapkan kustomisasi desain pada template HTML menggunakan Tailwind CSS dan JavaScript, khususnya pada halaman login, register, dan halaman daftar produk. Selain itu, navbar yang responsif juga telah diterapkan untuk meningkatkan pengalaman pengguna.

## Kustomisasi Halaman Login dan Register

Saya telah memodifikasi file `login.py` dan `register.py` dengan menambahkan animasi menggunakan Tailwind CSS dan JavaScript. Berikut adalah contoh penerapannya:

### Contoh Kode Animasi dengan Tailwind CSS

```html
<!-- Animasi dengan Tailwind CSS -->
<style>
  .animate-slide-down {
    animation: slideDown 1s ease-out forwards;
  }

  @keyframes slideDown {
    from {
      transform: translateY(-100%);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
</style>
```

### Contoh Kode untuk Animasi Teks dengan JavaScript

```javascript
<!-- JavaScript for Typing Animation -->
<script>
  const text = "Login to your account";
  let index = 0;
  
  function typeText() {
    if (index < text.length) {
      document.getElementById('typing-text').innerHTML += text.charAt(index);
      index++;
      setTimeout(typeText, 100);
    }
  }
</script>
```

## Kustomisasi Halaman Daftar Produk

Pada halaman `Add New Flower`, saya menerapkan logika untuk menangani dua kondisi berbeda:

- **Jika aplikasi belum memiliki produk yang tersimpan**: Tampilkan pesan atau elemen yang menginformasikan pengguna bahwa tidak ada produk.
- **Jika sudah ada produk yang tersimpan**: Tampilkan daftar produk yang ada.

### Contoh Pseudocode

```python
 {% if not products %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/dyasxoxo.jpeg' %}" alt="ayoo beli:P" class="w-96 h-96 mb-4"/>
        <p class="text-center text-gray-600">Belum ada pesanan untuk saat ini, ayo beli :((</p>
    </div>
    {% else %}
    <div class="flex flex-wrap justify-center">
        {% for product in products %}
        <div class="relative break-inside-avoid mb-4 mx-4 mt-4">
            <!-- Pin di atas card -->
            <div class="absolute -top-6 left-[-10px] transform -translate-x-0 w-12 h-12 bg-[#FDE6CA] rounded-md shadow-md mb-4"></div>

            <!-- Card dengan warna latar belakang gradien -->
            <div class="bg-gradient-to-b from-[#312E81] to-[#5954DC] shadow-lg rounded-lg break-inside-avoid flex flex-col border-2 border-blue-400 transform rotate-2 hover:rotate-1 transition-transform duration-300 animate-wiggle">
                <div class="p-4">
                    <h3 class="text-4xl font-bold bg-gray-100 text-white bg-clip-text mt-4">
                        𓍢ִ໋🌷 {{ product.name }} 𓍢ִ໋🌷
                    </h3>
                </div>
                <div class="p-5 text-gray-700">
                    <p class="font-semibold text-lg text-white mb-2">Description:</p>
                    <p class="font-medium text-white">{{ product.description }}</p>
                    <p class="font-medium text-white">Rp. {{ product.price }}</p>
                    <p class="font-medium text-white">Stock: {{ product.stock }}</p>
                    <p class="font-medium text-white">Category: {{ product.category }}</p>
                </div>
                <div class="flex justify-between p-4 border-t border-gray-300">
                    <a href="{% url 'main:edit_pesanan' product.id %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full px-4 py-2 transition duration-300 shadow-lg">
                        Edit
                    </a>
                    <a href="{% url 'main:delete_pesanan' product.id %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full px-4 py-2 transition duration-300 shadow-lg">
                        Delete
                    </a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    {% endif %}
```

## Styling untuk Setiap Kartu Produk

Untuk setiap kartu produk, saya menggunakan styling dari Tailwind CSS, termasuk:

- **Background Color**: Warna latar belakang menggunakan kelas Tailwind.
- **Padding dan Margin**: Menggunakan kelas padding dan margin untuk mengatur jarak.
- **Border dan Shadow**: Menambahkan border dan efek bayangan untuk membuat kartu lebih menarik.

### Contoh Kode untuk Kartu Produk

```html
<div class="bg-white shadow-lg rounded-lg p-4">
  <h2 class="text-lg font-bold">Nama Produk</h2>
  <p class="text-gray-700">Deskripsi Produk</p>
  <span class="text-green-500">Harga: Rp 100.000</span>
</div>
```

selain itu saya juga menambahkan `delete` dan `edit`
## Navigasi Bar (Navbar) yang Responsif

Navbar yang digunakan telah dioptimalkan untuk tampil dengan baik di berbagai ukuran layar. Menggunakan Tailwind CSS, navbar ini menyesuaikan tampilan dan fungsionalitasnya pada perangkat mobile dan desktop.

### Contoh Struktur Navbar

```html
<nav class="bg-gradient-to-b from-[#312E81] to-[#5954DC] shadow-lg fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-5xl mx-auto px-3 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <h1 class="text-2xl font-bold text-white">🌷DYAS FLOWERS🌷</h1>
      <div class="hidden md:flex items-center space-x-4">
        <a href="#home" class="text-white hover:bg-blue-500 px-3 py-2 rounded transition duration-300">Home</a>
        <a href="#category" class="text-white hover:bg-blue-500 px-3 py-2 rounded transition duration-300">Category</a>
        <a href="#cart" class="text-white hover:bg-blue-500 px-3 py-2 rounded transition duration-300">Cart</a>
      </div>
    </div>
  </div>
</nav>
```
---
#           TUGAS INDIVIDU 6
---

## Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web

JavaScript adalah bahasa pemrograman yang sangat penting dalam pengembangan aplikasi web modern. Berikut adalah beberapa manfaat utamanya:

- **Interaktivitas**: JavaScript memungkinkan pengembang untuk membuat halaman web yang interaktif dan responsif, meningkatkan pengalaman pengguna dengan elemen dinamis seperti formulir, animasi, dan konten yang dapat diperbarui tanpa memuat ulang halaman.
- **Pengolahan Data di Klien**: Dengan JavaScript, data dapat diproses langsung di sisi klien, mengurangi beban server dan mempercepat waktu respons aplikasi.
- **Kompatibilitas**: JavaScript didukung oleh semua browser modern, menjadikannya pilihan yang universal untuk pengembangan web.
- **Ekosistem yang Luas**: Terdapat banyak pustaka dan framework (seperti React, Angular, dan Vue.js) yang memudahkan pengembangan aplikasi kompleks.

## Fungsi Penggunaan `await` dalam `fetch()`

Keyword `await` digunakan untuk menunggu hasil dari promise yang dikembalikan oleh fungsi `fetch()`. Berikut adalah penjelasan lebih lanjut:

- **Menunggu Respons**: Dengan menggunakan `await`, eksekusi kode akan ditunda hingga promise selesai, sehingga kita bisa mendapatkan hasilnya secara langsung. Hal ini membuat kode lebih mudah dibaca dan ditulis dibandingkan dengan menggunakan metode `.then()`.
- **Tanpa `await`**: Jika kita tidak menggunakan `await`, kode akan melanjutkan eksekusi tanpa menunggu hasil dari `fetch()`, yang dapat menyebabkan kesalahan jika kita mencoba mengakses data sebelum tersedia. Ini bisa mengakibatkan error atau data yang tidak terdefinisi ketika mencoba memproses hasilnya.

### Contoh Penggunaan `await`

```javascript
 async function refreshFlowers() {
    document.getElementById("product").innerHTML = "";
    document.getElementById("product").className = "";
    const flowers = await getFlowers();
    let htmlString = "";
    let classNameString = "";
    ....
```

## Pentingnya Menggunakan Decorator `csrf_exempt` pada View untuk AJAX POST

Decorator `csrf_exempt` digunakan untuk menghindari pemeriksaan CSRF (Cross-Site Request Forgery) pada view tertentu yang digunakan untuk menerima permintaan AJAX POST. Alasan penggunaannya meliputi:

- **Permintaan AJAX**: Permintaan AJAX sering kali tidak menyertakan token CSRF secara otomatis. Dengan menggunakan `csrf_exempt`, kita memastikan bahwa view dapat diakses tanpa token tersebut, sehingga permintaan dari klien tetap dapat diproses.
- **Keamanan**: Meskipun menggunakan `csrf_exempt`, penting untuk memastikan bahwa view tersebut aman dari serangan lain, seperti validasi input dan otentikasi pengguna.

### Contoh Penggunaan `csrf_exempt`

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def add_flowers_ajax(request):
    name = strip_tags(request.POST.get("name"))  # strip HTML tags!
    description = strip_tags(request.POST.get("description"))  # strip HTML tags!
    price = strip_tags(request.POST.get("price"))  # strip HTML tags!
    stock = strip_tags(request.POST.get("stock"))  # strip HTML tags!
    category = strip_tags(request.POST.get("category", "General"))  # Default category
    
    # Mendapatkan user yang login
    user = request.user

    # Membuat objek Product baru
    new_product = Product(
        user=user,
        name=name, description=description,
        price=price, stock=stock,
        category=category
    )
    
    new_product.save()  
```

## Pembersihan Data Input Pengguna di Backend

Pembersihan data input pengguna di backend adalah langkah penting meskipun sudah ada validasi di frontend. Berikut alasannya:

- **Keamanan Tambahan**: Validasi di frontend dapat dengan mudah dihindari oleh pengguna jahat. Dengan melakukan pembersihan di backend, kita menambah lapisan keamanan tambahan untuk memastikan bahwa data yang diterima aman dan sesuai.
- **Konsistensi Data**: Pembersihan di backend membantu menjaga konsistensi data dalam aplikasi, terlepas dari bagaimana data dikirimkan dari klien. Ini penting untuk integritas database dan logika aplikasi secara keseluruhan.

### Contoh Pembersihan Data

```python
 def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
```

## Implementasi Checklist Secara Step-by-Step

Berikut adalah langkah-langkah implementasi checklist dalam pengembangan aplikasi:

