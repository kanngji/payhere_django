from django import forms
from .models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['phoneNumber', 'password']
#         widgets = {
#             'phoneNumber': forms.TextInput(attrs={'placeholder': '휴대폰번호를 입력하세요'}),
#             'password': forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력하세요'}),
#         }

class LoginForm(forms.Form):
    phoneNumber = forms.CharField(max_length=11, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super().clean()
        phoneNumber = cleaned_data.get('phoneNumber')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(phoneNumber=phoneNumber)
        except User.DoesNotExist:
            raise forms.ValidationError('등록된 사용자가 없습니다.')
        
        if not user.check_password(password):
            raise forms.ValidationError('비밀번호가 틀립니다.')

        return cleaned_data