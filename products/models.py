from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=160)

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=10, blank=True)
    quantity = models.IntegerField(default=10, blank=True)
    cover = models.ImageField(upload_to='product_image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
