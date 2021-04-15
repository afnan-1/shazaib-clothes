from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name    


class Product(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    publish = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    def get_absolute_url(self):
        return reverse("ecom:single_post", args=[self.slug])
    def __str__(self):
        return self.title

class Quantity(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('ecom.Product',on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.quantity) + " " +  self.product.title

class Order(models.Model):
    products = models.ManyToManyField(Product,blank=True,related_name='products')
    user = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE)
    quan = models.ManyToManyField(Quantity,related_name='quan')
    quantity = models.TextField(max_length=500,null=True,blank=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=400,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'Order by {self.first_name}'

