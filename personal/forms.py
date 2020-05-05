from django import forms
from data.models import *
from django.contrib.auth.models import User

class UpdateInfoUserForm(forms.ModelForm) :

    class Meta :
        model = InfoUser
        fields = ["phonenumber", "address", "default"]

class InfoForm(forms.ModelForm) :

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.default = kwargs.pop('default', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        info = super().save(commit=False)
        info.user = self.user
        info.default = self.default
        info.save()

    class Meta:
        model = InfoUser
        fields = ["phonenumber", "address"]