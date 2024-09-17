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

