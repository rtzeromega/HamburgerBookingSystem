from django import forms
from django.contrib.auth.models import User
from .models import Create, Store, Cart, Like


# 用户需要输入的字段
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# 自定义Customer, Store对象的输入信息
class CreateForm(forms.ModelForm):
    class Meta:
        model = Create        # 元类 即数据库模型为Create类
        fields = ['create_food', 'create_logo']
        exclude = ['user']      # user信息不能从后台输入


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['food', 'logo', 'price', 'quantity']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['food']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['comment']