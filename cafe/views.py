
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    page = request.GET.get('page','1') # 페이지
    product_list = Product.objects.order_by('-create_date')
    paginator = Paginator(product_list,10) # 페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj}
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