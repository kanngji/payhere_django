from django import forms
from cafe.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product # 사용할 모델
        fields = ['category','price','cost','name','description','barcode',
                  'exp_date','size']