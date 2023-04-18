from django.db import models
# 유효성 검사
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password,check_password

# Create your models here.
# User에 해당하는 모델 정의
class User(models.Model):
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})$')
    phoneNumber = models.CharField(validators=[phoneNumberRegex],max_length=11,unique=True)
    password = models.CharField(max_length=128)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    # 이름으로 표시되게
    def __str__(self):
        return self.phoneNumber