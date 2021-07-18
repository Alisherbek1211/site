from django.db import models


class User(models.Model):
    firstname = models.CharField(verbose_name="Firstname",max_length=255)
    lastname = models.CharField(verbose_name="Lastname",max_length=255,null=True)
    email = models.CharField(verbose_name="User Password",max_length=255)
    phone_number = models.CharField(verbose_name="Phone Number",max_length=20,null=True)
    password = models.CharField(verbose_name="Password",max_length=255)
    is_admin = models.BooleanField(verbose_name="Admin",default=False)
    is_staff = models.BooleanField(verbose_name="Staff",default=True)
    is_superuser = models.BooleanField(verbose_name="Superuser",default=False)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    name = models.CharField(verbose_name="Category names" ,max_length=255)

    created_at = models.DateTimeField(verbose_name="Date of creation", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Modified date",auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Products name",max_length=255)
    price = models.FloatField(verbose_name="The price of the product") 
    stock = models.IntegerField(verbose_name="Stock",default=1)
    product_description = models.TextField(verbose_name="Description")
    rating = models.FloatField(verbose_name="Rate")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image = models.ImageField(verbose_name="images",upload_to="image/",null=True)
    
    created_at = models.DateTimeField(verbose_name="Date of creation",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Modified date",auto_now=True)
    
    def __str__(self):
        return self.name
