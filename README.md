**Nama**: Widya Mutia Ichsan  
**NPM**: 2306165912  
**Kelas**: PBP E  

Aplikasi PWS yang sudah di-deploy dapat diakses melalui tautan berikut:  
[http://pbp.cs.ui.ac.id/widya.mutia/dyascommerce](http://pbp.cs.ui.ac.id/widya.mutia/dyascommerce)

***

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
    'dyascommerce'
]
```

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**  
`name : CharField`  
`price : IntegerField`  
`description : TextField`  

Akan tetapi saya juga menambahkan beberapa atribut seperti:  
`stock : IntegerField`  
`category : CharField`  
`image : ImageField`

**5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**

**6. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.**

**7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

***

### Bagan yang Berisi Request Client ke Web Aplikasi Berbasis Django Beserta Responnya

Buat bagan yang menunjukkan alur dari request client ke web aplikasi Django dan respons yang dikembalikan. Jelaskan bagaimana `urls.py`, `views.py`, `models.py`, dan berkas `html` saling terkait dalam proses ini.

***

### Penjelasan Fungsi Git dalam Pengembangan Perangkat Lunak

Fungsi git dalam pengembangan perangkat lunak yaitu sebagai sistem kontrol yang esensial yang digunakan untuk mengelola perubahan kode secara efektif, selain itu juga memungkinkan pengembang untuk mencatat dan melacak setiap perubahan yang dilakukan pada kode sumber. Dengan Git, pengembang dapat mengatur berbagai versi aplikasi, yang sangat berguna untuk memantau perkembangan proyek dari waktu ke waktu.

Selain itu juga, dengan menggunakan Git dapat mengurangi risiko kehilangan data. Karena Git menyimpan riwayat lengkap dari setiap perubahan yang dilakukan, sehingga pengembang dapat dengan mudah kembali ke versi sebelumnya jika diperlukan. Hal ini membantu dalam memulihkan data yang mungkin hilang atau terhapus secara tidak sengaja. Dengan Git, proses pemulihan data menjadi lebih mudah dan aman, memberikan rasa percaya diri kepada pengembang bahwa kode mereka tetap terlindungi dan dapat dipulihkan jika terjadi masalah.

### Dari Semua Framework yang Ada, Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Karena Django adalah framework yang populer dan banyak digunakan dalam pengembangan web. Selain itu Django memiliki fitur-fitur yang memudahkan pengembangan aplikasi web, seperti ORM dan template engine.

### Mengapa Model pada Django Disebut sebagai ORM?

Karena berfungsi sebagai jembatan antara objek-objek dalam kode Python dan tabel-tabel dalam database relasional.

---
