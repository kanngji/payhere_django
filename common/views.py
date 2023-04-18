from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import User
from .forms import LoginForm





# Create your views here.
# 로그인
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phoneNumber']
            raw_password = form.cleaned_data['password']
            try:
                user = User.objects.get(phoneNumber=phone_number)
            except User.DoesNotExist:
                user = None
                messages.warning(request, '등록된 사용자가 없습니다.')
                return render(request, 'common/login.html', {'form': form})
            if user.check_password(raw_password):
                request.session['user_phoneNumber']=user.phoneNumber
                return redirect('cafe:index')
            else:
                messages.warning(request, '비밀번호가 틀립니다.')
                return render(request, 'common/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'common/login.html', {'form': form})
            


# 회원가입
def register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        raw_password = request.POST.get('password')
        password = make_password(raw_password)

        # 중복된 휴대폰 번호 검사
        if User.objects.filter(phoneNumber=phone_number).exists():
            messages.warning(request, '이미 가입된 휴대폰번호입니다.')
            return redirect('common:register')

        # User 모델의 객체 생성
        user = User(phoneNumber=phone_number, password=password)
        user.save()

        return redirect('cafe:index')
    
    else:
        
        return render(request, 'common/register.html')

def logout(request):
    if 'user_phoneNumber' in request.session:
        
        del request.session['user_phoneNumber']
    return redirect('common:login')