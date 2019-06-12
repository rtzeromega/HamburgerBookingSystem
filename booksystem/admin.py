from django.contrib import admin
from .models import Create, Store, Like
from .forms import CreateForm, StoreForm, LikeForm


# 自定义表单管理
class CreateAdmin(admin.ModelAdmin):
    list_display = (
        'create_food', 'create_logo', 'user')
    form = CreateForm  # 自定义需要在后台中输入哪些信息


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'food', 'logo', 'quantity', 'price')
    form = StoreForm


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'food', 'user', 'comment')
    form = LikeForm


# Register your models here.
admin.site.register(Create, CreateAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Like, LikeAdmin)
