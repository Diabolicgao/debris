from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Post(models.Model) :
    
    STATUS_CHOICES = [
        ('ninjago', 'ninjago'),
        ('city', 'city'),
        ('animal', 'animal'),
        ('fantasy', 'fantasy'),
        ('star_wars', 'star_wars'),
        ('overwatch', 'overwatch'),
        ('item', 'item'),
        ('vehicle', 'vehicle'),
        ('custom', 'custom'),
        ('technic', 'technic'),
        ('dragon', 'dragon'),
        ('castle', 'castle'),
        ("cyberpunk", "cyberpunk"),
        ('dc', 'dc'),
        ('marvel', 'marvel'),
        ('brick', 'brick')
    ]

    category = models.CharField(max_length=50,choices=STATUS_CHOICES)
    title = models.CharField(max_length=100)
    info = models.TextField(null=True)
    description = models.TextField(null=True, default='Không có mô tả nào')
    note = models.CharField(max_length=100, null=True, default='Không có lưu ý nào')
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True,default='null')
    price = models.IntegerField()

    def __str__(self) :
        return self.title

EVENT_CHOICES = [
    ('event', 'event'),
    ('notify', 'notify'),
]
class Event(models.Model) :
    category = models.CharField(max_length=10, default='Event', choices=EVENT_CHOICES)
    title = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True,default="event.jpg")
    time_takes_place = models.CharField(max_length = 50, null = True)
    status = models.CharField(max_length=20, null=True)
    
    def __str__(self) :
        return self.title

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    body = models.CharField(max_length=350, null=True)
    time = models.DateTimeField(auto_now_add=True)

class ImagesOfPost(models.Model) :
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='images')
    image = models.ImageField(null=True)

class Cart(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    
class InfoUser(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='info')
    address = models.TextField(blank=True)
    phonenumber = models.CharField(max_length=10, blank=True)
    default = models.BooleanField(default=False)

PAYMENTS_CHOICE = [
    ("Thanh toán khi nhận hàng" , "COD"),
    ("ATM/Internet Banking" , "ATM/Internet Banking"),
    ("Chuyển khoản" , "Chuyển khoản")
]
class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    checked = models.BooleanField(default=False)
    address = models.TextField()
    phonenumber = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
    payments = models.BooleanField(verbose_name="Thanh toán khi nhận hàng")
    sum_money = models.IntegerField()
    tran_cost = models.IntegerField()
    cancel = models.BooleanField(default=False, verbose_name='Hủy')
    exchange_scf = models.BooleanField(default=False, verbose_name='Giao dịch thành công')
    
    def __str__(self) :
        return self.user.username

class CartOrder(models.Model) :
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cartorder')
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()

