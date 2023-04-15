from django.contrib import admin
from .models import Product
# Register your models here.



#이름(name)으로 질문 데이터를 검색
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Product,ProductAdmin)