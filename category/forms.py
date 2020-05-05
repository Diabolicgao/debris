from django import forms
from data.models import *

class CartForm(forms.ModelForm) :

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.item = kwargs.pop('item', None)
        self.price = kwargs.pop('price', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        cart = super().save(commit=False)
        cart.user = self.user
        cart.item = self.item
        cart.price = self.price
        cart.save()

    class Meta:
        model = Cart
        fields = ["amount"]

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]