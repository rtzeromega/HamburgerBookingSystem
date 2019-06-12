from django.contrib.auth.models import Permission, User
from django.db import models

# python manage.py makemigrations
# python manage.py migrate
# python manage.py dbshell


class Create(models.Model):
    user = models.ForeignKey(User, default=1) # 有了这个字段之后，默认的后台添加失效，必须要自定义Form，除去这个字段
    create_food = models.CharField(max_length=100, null=True)
    create_logo = models.FileField(default=0)


class Store(models.Model):
    food = models.CharField(max_length=100, null=True)
    logo = models.FileField(default=0)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)


class Cart(models.Model):
    user = models.ForeignKey(User, default=1)
    food = models.ForeignKey(Store)


class Like(models.Model):
    user = models.ForeignKey(User, default=1)
    food = models.ForeignKey(Store)
    comment =models.CharField(max_length=200)