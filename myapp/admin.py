from django.contrib import admin
from .models import (Product , Cart, Customer , OrderPlace, UserDetails)
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'name' ,  'locality' , 'city' , 'zipcode' , 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' , 'selling_price' ,  'discounted_price' , 'description' , 'brand' , 'category' , 'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'product' ,  'quantity']



@admin.register(UserDetails)
class UserdetailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' ,'first_name' , 'last_name', 'mobile_number'  ,'email' , 'locality' , 'area_and_street' , 'city' , 'pincode' , 'landmark', 'state']




@admin.register(OrderPlace)
class OrderplaceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'product' , 'Customer' , 'quantity' , 'ordered_Date' , 'status']




    