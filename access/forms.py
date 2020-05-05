from django import forms
import re
from django.contrib.auth.models import User
from data.models import * 

class RegistrationForm(forms.Form) :
    first_name = forms.CharField(label='', max_length=10)
    last_name = forms.CharField(label='',max_length=10)
    username = forms.CharField(label='',max_length=15)
    email = forms.EmailField(label='',)
    password1 = forms.CharField(label='',widget=forms.PasswordInput())
    password2 = forms.CharField(label='',widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'], first_name = self.cleaned_data['first_name'], last_name = self.cleaned_data['last_name'])

