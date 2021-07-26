from store.models import Product
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()

class Cart(models.Model):
    session_id = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(verbose_name="Date of creation",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Modified date",auto_now=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    created_at = models.DateTimeField(verbose_name="Date of creation",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Modified date",auto_now=True)

    def total_price(self):
        return self.quantity * self.product.price
