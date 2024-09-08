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

     INSTALLED_APPS = [
    ...,
    'main',
    'dyascommerce' 
] 

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**<br>

`name : CharField`\n
`price : IntegerField`\n
`description : TextField`

    akan tetapi saya juga menambahkan beberapa atribut seperti:

`stock : IntegerField`\n
`category : CharField`\n
`image : ImageField`

**5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**

**6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**

**7.  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

***

bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 'urls.py', 'views.py', 'models.py', dan berkas 'html'.

***

**Penjelasan fungsi git dalam pengembangan perangkat lunak**<br>

    Fungsi git dalam pengembangan perangkat lunak yaitu sebagai sistem kontrol yang esensial yang digunakan untuk mengelola perubahan kode secara efektif, selain itu juga  memungkinkan pengembang untuk mencatat dan melacak setiap perubahan yang dilakukan pada kode sumber. Dengan Git, pengembang dapat mengatur berbagai versi aplikasi, yang sangat berguna untuk memantau perkembangan proyek dari waktu ke waktu.<br>

    selain itu juga, dengan menggunakan Git dapat mengurangi risiko kehilangan data. Karena Git menyimpan riwayat lengkap dari setiap perubahan yang dilakukan, sehingga pengembang dapat dengan mudah kembali ke versi sebelumnya jika diperlukan. Hal ini membantu dalam memulihkan data yang mungkin hilang atau terhapus secara tidak sengaja. Dengan Git, proses pemulihan data menjadi lebih mudah dan aman, memberikan rasa percaya diri kepada pengembang bahwa kode mereka tetap terlindungi dan dapat dipulihkan jika terjadi masalah.


**dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**<br>
    Karena Django adalah framework yang populer dan banyak digunakan dalam pengembangan web. Selain itu Django memiliki fitur-fitur yang memudahkan pengembangan aplikasi web, seperti ORM dan template engine.

**Mengapa model pada Django disebut sebagai ORM?**<br>
    Karena berfungsi sebagai jembatan antara objek-objek dalam kode Python dan tabel-tabel dalam database relasional.





