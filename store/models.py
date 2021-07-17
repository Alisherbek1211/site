from django.db import models
from django.db.models.fields import CharField


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phono_number = models.IntegerField()
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    product_description = models.TextField(max_length=255)
    rating = models.FloatField()
    cupon = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()