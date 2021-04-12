from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import AbstractUser
from ecom.models import Product
# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    age = models.CharField(max_length=20, null=True,blank=True)
    cnic = models.CharField(max_length=15)
    date_of_birth = models.CharField(max_length=100,default='none')
    gender = models.CharField(max_length=10)
    cart = models.ManyToManyField(Product,null=True,blank=True)
    def __str__(self):
        return self.username
    
