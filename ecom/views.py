from django.shortcuts import render,get_object_or_404,redirect,reverse,redirect
from .models import Product,Order,Category
from users.models import CustomUser
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
import random

# Create your views here.
def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        return render(request,'index.html',{'products':products,'user':user,'category':category})
    return render(request,'index.html',{'products':products,'category':category})
    


def single_post(request,product):
    category = Category.objects.all()
    product = get_object_or_404(Product,slug=product)
    products = Product.objects.order_by('?')[:10]
    return render(request,'single_product.html',{'product':product,'category':category,'products':products})


def addtocart(request,id):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        product = get_object_or_404(Product,id=id)
        user.cart.add(product)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def searchProduct(request):
    category = Category.objects.all()
    product = Product.objects.filter(title__contains=request.GET.get('search'))
    return render(request,'index.html',{'search_result':product,'category':category})


def cart(request):
    category = Category.objects.all()
    total = 0
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        if (user.cart.count())<1:
            messages.info(request, 'You cart is empty')
        else: 
            for i in user.cart.all():
                total += i.price
        return render(request,'cart.html',{'user':user,'category':category,'total':total})



def category(request,cat_name):
    category = Category.objects.all()
    products = Product.objects.filter(category__name=cat_name)
    return render(request,'category.html',{'products':products,'category':category,'name':cat_name})
def deletecart(request,pk):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        product = get_object_or_404(Product,id=pk)
        user.cart.remove(product)
        return redirect('/cart/')

def checkout(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        return render(request,'checkout.html',{'user':user,'category':category})

def checkoutbilling(request):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        address = request.GET.get('address')
        city = request.GET.get('city')
        order = Order(first_name=first_name, last_name=last_name, email=email, address=address,city=city,user=user)
        order.save()
        for i in user.cart.all():
            order.products.add(i)
        user.cart.clear()
        return redirect('/')