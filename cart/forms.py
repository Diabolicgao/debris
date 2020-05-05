from django import forms
from data.models import *

class OrderForm(forms.ModelForm) :

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.address = kwargs.pop('address', None)
        self.phonenumber = kwargs.pop('phonenumber', None)
        self.sum_money = kwargs.pop('sum_money', None)
        self.tran_cost = kwargs.pop('tran_cost', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        order = super().save(commit=False)
        order.user = self.user
        order.address = self.address
        order.phonenumber = self.phonenumber
        order.sum_money = self.sum_money
        order.tran_cost = self.tran_cost
        order.save()
        return order
    class Meta:
        model = Order
        fields = ["payments"]