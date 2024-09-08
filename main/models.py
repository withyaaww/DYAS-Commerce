from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  
    price = models.IntegerField()  
    description = models.TextField()  
    stock = models.IntegerField()  
    category = models.CharField(max_length=100, default="General")  
    image = models.ImageField(upload_to='products/', null=True, blank=True)  

    def __str__(self):
        return self.name
