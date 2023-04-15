from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def index(request):
    product_list = Product.objects.order_by('-create_date')
    context = {'product_list': product_list}
    return render(request, 'cafe/product_list.html', context) 

# 상세조회
def detail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product':product}
    return render(request, 'cafe/product_detail.html',context)
