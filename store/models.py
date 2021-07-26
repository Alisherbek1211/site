from django.db import models
from datetime import datetime,timezone


class Category(models.Model):
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        
    name = models.CharField(verbose_name="Category names" ,max_length=255)
    icon = models.ImageField(upload_to="images/",verbose_name="Rasmi")
    slug = models.CharField(verbose_name="Category slug" ,max_length=255,null=True)


    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name = "Kichik Kategoriya"
        verbose_name_plural = "Kichik Kategoriyalar"

    
    name = models.CharField(verbose_name="Category names" ,max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(verbose_name="Category slug" ,max_length=255,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    title = models.CharField(verbose_name="Products name",max_length=255)
    price = models.FloatField(verbose_name="The price of the product") 
    slug = models.CharField(max_length=255,null=True)
    description = models.TextField(verbose_name="Description")
    rating = models.FloatField(verbose_name="Rate")
    image = models.ImageField(verbose_name="images",upload_to="image/",null=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(verbose_name="Date of creation",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Modified date",auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.price}"

    def get_rating_percent(self):
        return 100 * (self.rating / 5)

    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < 86400
