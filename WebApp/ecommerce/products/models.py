from tkinter.constants import CASCADE
from django.contrib import admin
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category



class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True, default="")


    def __str__(self):
        return f"{self.name}, {self.price}"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

