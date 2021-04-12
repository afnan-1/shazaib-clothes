from django.shortcuts import render,redirect
from users.models import CustomUser

def home(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(pk=request.user.pk)
        return render(request,'index.html',{'user':user})
    else:
        return render(request,'index.html')


