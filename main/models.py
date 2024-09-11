from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=255)  
    price = models.IntegerField()  
    description = models.TextField()  
    stock = models.IntegerField()  
    category = models.CharField(max_length=100, default="General")  
    # image = models.ImageField(upload_to='products/', null=True, blank=True)  

    def __str__(self):
        return self.name
    
class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    nama_lengkap = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    deskripsi = models.TextField()
    jumlah_character = models.IntegerField()