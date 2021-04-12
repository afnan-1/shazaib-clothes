from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate
from ecom.models import Order,Product
def signup_view(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')
        cnic = request.POST.get('cnic')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('dob')
        try:
            user = CustomUser.objects.create_user(username=username,email=email,password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.age = age
            user.cnic = cnic
            user.gender = gender
            user.date_of_birth = date_of_birth
            user.save()
        except:
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html', )
        return redirect('/users/login')
    else:
        return render(request,'signup.html')


def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'username or password is inncorrect please try again')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
        

def profile(request):
    if request.user.is_authenticated:
        current_user = CustomUser.objects.get(pk=request.user.pk)
        return render(request,'profile.html',{'user':current_user})
    else:
        print('user')
        return render(request,'profile.html')


def edit_profile(request):
    current_user = CustomUser.objects.get(pk=request.user.pk)
    male=False
    female=False
    if current_user.gender=='Male':
        male = True
    else:
        female = True
    if request.method=='POST':
        if request.user.is_authenticated: 
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            age = request.POST.get('age')
            date_of_birth = request.POST.get('dob')
            cnic = request.POST.get('cnic')
            gender = request.POST.get('gender')
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.age = age
            current_user.date_of_birth = date_of_birth
            current_user.cnic = cnic
            current_user.gender = gender
            current_user.save()
            return redirect('/users/profile')
    return render(request,'editprofile.html',{'user':current_user,'male':male,'female':female})

def logout_view(request):
    logout(request)
    return redirect('/')

def orders(request):
    order = Order.objects.filter(user=request.user).distinct()
    return render(request,'orders.html',{'order':order,})
