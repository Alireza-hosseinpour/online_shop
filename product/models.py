from django.db import models
from utils.modules import path_and_rename


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    entity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename('products'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "products"
        verbose_name_plural = "products"
        db_table = "products"
