from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index,),

    # 搜索
    url(r'^index/assword', views.search),

]


