"""hamburger URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views

app_name = 'booksystem'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),  # 登入
    url(r'^logout/$', views.logout_user, name='logout'),  # 登出
    url(r'^register/$', views.register, name='register'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^create/$', views.create, name='create'),
    url(r'^user_info/$', views.user_info, name='user_info'),
    url(r'^buy/store/(?P<store_id>[0-9]+)/$', views.book, name='book'),
    url(r'^refund/cart/(?P<cart_id>[0-9]+)/$', views.refund, name='refund'),

    url(r'^refund_like/like/(?P<like_id>[0-9]+)/$', views.refund_like, name='refund_like'),
    url(r'^(?P<store_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<create_id>[0-9]+)/delete/$', views.delete, name='delete'),

]
