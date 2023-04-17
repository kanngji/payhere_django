from django import forms
from common.models import User

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ['phoneNumber','password']