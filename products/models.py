from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=10, blank=True)
    quantity = models.IntegerField(default=10, blank=True)
    cover = models.ImageField(upload_to='product_image/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
