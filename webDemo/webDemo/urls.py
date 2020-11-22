"""webDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webApp import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # # //这里mainpage是需要在浏览器中输入的接口名称，比如http://127.0.0.1:8000/mainpage,
    # # //而index则是输入该网址之后，相应会被调用的接口。
    # path(r'', views.index, name='index'),
    # path(r'login', views.login, name='login'),
    # path(r'loginVal', views.my_view, name='my_view'),

    # 考虑到登录系统属于站点的一级功能，为了直观和更易于接受，这里没有采用二级路由的方式，
    # 而是在根路由下直接编写路由条目，同样也没有使用反向解析名（name参数）
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls'))

]
