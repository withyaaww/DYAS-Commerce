from django.test import TestCase, Client
from django.utils import timezone
from .models import Product, CustomUser
from django.urls import reverse

class MainTest(TestCase):
    def setUp(self):
        # Setup awal untuk uji coba, seperti membuat objek produk dan pengguna
        self.client = Client()
        self.product = Product.objects.create(
            name="Beautiful Crochet Flower",
            price=50000,
            description="A handmade crochet flower, perfect for any occasion.",
            stock=10,
            category="Floral",
            image=None
        )
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="securepassword",
            nama_lengkap="Test User",
            email="testuser@example.com"
        )

    def test_main_url_is_exist(self):
        response = self.client.get(reverse('main:show_main'))  # Menggunakan nama URL dari routing
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get(reverse('main:show_main'))  # Menggunakan nama URL dari routing
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        # Menguji apakah produk telah berhasil dibuat
        response = self.client.get(reverse('main:show_main'))  # Halaman utama harus menampilkan produk
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.price)
        self.assertContains(response, self.product.description)

    def test_user_creation(self):
        # Menguji apakah pengguna telah berhasil dibuat
        self.assertTrue(CustomUser.objects.filter(username="testuser").exists())

    def test_login_user(self):
        # Menguji login pengguna
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'securepassword'})
        self.assertEqual(response.status_code, 302)  # Redirect setelah login
        self.assertIn('_auth_user_id', self.client.session)  # Memastikan pengguna telah login
