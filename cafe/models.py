from django.db import models

# Create your models here.

# Product에 해당하는 모델 정의
class Product(models.Model):

    # choices
    SIZE_CHOICES = [
        ('SMALL','small'),
        ('LARGE','large')
    ]
    category = models.CharField(max_length=20) # 카테고리
    #  DecimalField는 숫자를 저장하기 위한 필드 유형 중 하나이며, max_digits 매개변수는 소수점을 포함한 숫자의 최대 자릿수를, decimal_places 매개변수는 소수점 아래 자릿수를 나타냅니다.
    price = models.DecimalField(max_digits=10, decimal_places=2) # 가격
    cost = models.DecimalField(max_digits=10, decimal_places=2) # 원가
    name = models.CharField(max_length=50) #이름
    description = models.TextField() # 설명
    barcode = models.TextField() # 바코드
    exp_date = models.TextField() # 유통기한
    size = models.CharField(max_length=20,choices=SIZE_CHOICES,default='SMALL') # 사이즈
    create_date = models.DateTimeField() # 생성시기

