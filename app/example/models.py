from django.db import models

class Product(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.TextField()

class Cart(models.Model):
    purchase_date = models.DateTimeField()

class CartItem(models.Model):
    added_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    products = models.ManyToManyField(Product)

