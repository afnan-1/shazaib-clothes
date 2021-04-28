from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','slug','category')
    prepopulated_fields = {
        "slug":("title",)
    }


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal=('products',)
    fields = ('products','user','quantity','total_price','email','address','city','first_name','last_name')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Order,OrderAdmin)