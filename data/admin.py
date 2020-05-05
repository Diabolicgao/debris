from django.contrib import admin
from data.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CartInline(admin.StackedInline) :
    model = Cart
class InfoInline(admin.StackedInline) :
    model = InfoUser
class CommentInline(admin.StackedInline) :
    model = Comment
class ImageInline(admin.StackedInline) :
    model = ImagesOfPost

UserAdmin.inlines = [CartInline, InfoInline]
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Tùy biến Admin trong bảng Post
class PostAdmin(admin.ModelAdmin) :
    # Hiển thị cột 'title', 'category' và 'time'
    list_display = ['title', 'category', 'time']
    # Lọc các bài viết theo time
    list_filter = ['time']
    # Chưa rõ
    date_hierarchy = 'time'
    # Tìm kiếm sản phẩm theo tên
    search_fields = ['title']
    inlines = [CommentInline, ImageInline]

admin.site.register(Post,PostAdmin)

# Tùy biến Admin trong bảng Event
class EventAdmin(admin.ModelAdmin) :

    # Sửa status được chọn thành 'off'
    def Status_Change(self, request, queryset) :
        row_updated = queryset.update(status = 'off')
        if row_updated == 1 :
            message_bit = "1 story was"
        else :
            message_bit = "{} stories were".format(row_updated)
        self.message_user(request, "{} successfully marked as published.".format(message_bit))
        # Status_Change.short_description = 'Update status'

    # Hiển thị cột 'title', 'time_takes_place' và 'status'
    list_display = ['title','category', 'time_takes_place', 'status']
    # Lọc các bài viết theo time
    list_filter = ['time']
    # Chưa rõ
    date_hierarchy = 'time'
    # Tìm kiếm sản phẩm theo tên
    search_fields = ['title']
    # Kích hoạt hàm Status_Change 
    actions = [Status_Change]

admin.site.register(Event, EventAdmin)

class CartOrderInline(admin.StackedInline) :
    model = CartOrder
class OrderAdmin(admin.ModelAdmin) :
    list_display = ["user", "checked", "time", "cancel", "exchange_scf"]
    inlines = [CartOrderInline]

admin.site.register(Order, OrderAdmin)