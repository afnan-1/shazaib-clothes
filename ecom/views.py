from django.shortcuts import render,get_object_or_404,redirect,reverse,redirect
from .models import Product,Order,Category,Quantity
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
        quantity = Quantity(quantity=request.GET['quantity'],product=product,user=user)
        quantity.save()
        user.cart.add(product)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def searchProduct(request):
    category = Category.objects.all()
    product = Product.objects.filter(title__contains=request.GET.get('search'))
    return render(request,'index.html',{'search_result':product,'category':category})


def cart(request):
    category = Category.objects.all()
    total = []
    total_price = []
    quanty = []
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        quantity = Quantity.objects.filter(user=user)
        if (user.cart.count())<1:
            messages.info(request, 'You cart is empty')
        else: 
            for i in user.cart.all():
                total.append(i.price)
            for i in quantity.all():
                quanty.append(i.quantity)
            total = [int(i) for i in total]
            quanty = [int(i) for i in quanty]
            for num1, num2 in zip(total, quanty):
	            total_price.append(num1*num2)
            
        return render(request,'cart.html',{'user':user,'category':category,'total':sum(total_price),'quantity':quanty})



def category(request,cat_name):
    category = Category.objects.all()
    products = Product.objects.filter(category__name=cat_name)
    return render(request,'category.html',{'products':products,'category':category,'name':cat_name})
def deletecart(request,pk):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        product = get_object_or_404(Product,id=pk)
        quantity = Quantity.objects.filter(user=user,product=product).delete()
        user.cart.remove(product)
        return redirect('/cart/')

def checkout(request):
    quanty = []
    category = Category.objects.all()
    quantity = Quantity.objects.filter(user__id=request.user.id)
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        for i in quantity.all():
            quanty.append(i.quantity)
        return render(request,'checkout.html',{'user':user,'category':category})

def checkoutbilling(request):
    quanty = []
    total_price = []
    total = []
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser,id=request.user.id)
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        address = request.GET.get('address')
        city = request.GET.get('city')
        quantity = Quantity.objects.filter(user=user)
        order = Order(first_name=first_name, last_name=last_name, email=email, address=address,city=city,user=user)
        order.save()
        for i in user.cart.all():
            total.append(i.price)
            order.products.add(i)
        total_quantity=""
        for i in quantity.all():
            quanty.append(i.quantity)
            total_quantity +=  f'product {i.product.title} quantity {i.quantity} \n' 
        total = [int(i) for i in total]
        quanty = [int(i) for i in quanty]
        for num1, num2 in zip(total, quanty):
	        total_price.append(num1*num2) 
        order.total_price = sum(total_price)
        order.quantity = total_quantity
        order.save()
        user.cart.clear()
        Quantity.objects.all().delete()
        return redirect('/')