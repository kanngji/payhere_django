from django.urls import path

from . import views

# URL 네임스페이스 지정
app_name = 'cafe'

# name=''는 별칭이다
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:product_id>/',views.detail, name='detail'),
    path('product/create/', views.product_create, name='product_create'),
]