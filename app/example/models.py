from django.db import models

class Product(models.Model):
    name = models.TextField()

class Cart(models.Model):
    purchase_date = models.DateTimeField()

    @property
    def price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

    @property
    def taxes(self):
        return self.price * self.tax_rate

    @property
    def stripe_fees(self):
        return self.price * 0.03

class CartItem(models.Model):
    added_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    products = models.ManyToManyField(Product)

    @property
    def price(self):
        return self.product.price

    @property
    def taxes(self):
        return self.product.price * (self.product.tax_rate / 100)
