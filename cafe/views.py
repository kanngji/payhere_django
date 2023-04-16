
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from .forms import ProductForm
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

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.create_date= datetime.now()
            product.save()
            return redirect('cafe:index')
    else:
        form = ProductForm()
    context={'form':form}
    return render(request, 'cafe/product_form.html', context)