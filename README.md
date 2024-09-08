Nama : Widya Mutia Ichsan<br>
NPM : 2306165912<br>
Kelas : PBP E<br>

Aplikasi PWS yang sudah di-deploy dapat diakses melalui tautan berikut:
[http://pbp.cs.ui.ac.id/widya.mutia/dyascommerce](http://pbp.cs.ui.ac.id/widya.mutia/dyascommerce)

***
**Penjelasan implementasi tugas *step-bystep* (bukan hanya sekadar mengikuti tutorial).**


**1. Membuat sebuah proyek Django baru.**<br>
    Untuk langkah pertama saya membuat sebuah proyek django bernama *dyascommerce* menggunakan command :
    `django-admin startproject dyascommerce`

**2. Membuat aplikasi dengan nama main pada proyek tersebut.**<br>
    Langkah kedua yaitu membuat aplikasi baru bernama **main** di dalam proyek menggunakan perintah :
    `python manage.py starapp main`

**3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**<br>
    Langkah ke-3 yaitu menambahkan 'main' dan 'dyascommerce' ke dalam daftar aplikasi

    ` INSTALLED_APPS = [
    ...,
    'main',
    'dyascommerce' 
] `

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**<br>

`name : CharField
  price : IntegerField
  description : TextField`

    akan tetapi saya juga menambahkan beberapa atribut seperti:

`stock : IntegerField
  category : CharField
  image: ImageField`

**5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**







