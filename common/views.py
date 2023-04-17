from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User
from .forms import UserForm

# Create your views here.

def login(request):
    return render(request, 'common/login.html')

def register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        raw_password = request.POST.get('password')
        password = make_password(raw_password)

        # User 모델의 객체 생성
        user = User(phoneNumber=phone_number, password=password)
        user.save()

        return redirect('cafe:index')
    
    else:
        return render(request, 'common/register.html')
