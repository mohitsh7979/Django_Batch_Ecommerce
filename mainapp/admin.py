from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Students)

# @admin.register(Students)

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id','name','age','address','mobile_no','roll_no','image','File']


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","title","price","description","product_image","category","size"]
