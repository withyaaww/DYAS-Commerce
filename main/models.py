from django.db import models
from django.contrib.auth.models import User
import uuid


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)  
    price = models.IntegerField() 
    description = models.TextField()  
    stock = models.IntegerField() 
    category = models.CharField(max_length=100, default="General")  
    # image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name  

    @property
    def is_stock_available(self):
        return self.stock > 0