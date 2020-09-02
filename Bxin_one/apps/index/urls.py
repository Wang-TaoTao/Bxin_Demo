from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'service/weather', views.get_menu, ),
    url(r'service/images', views.get_images, ),
    url(r'service/image_text', views.get_image_text, ),

    # 搜索
    # url(r'^index/assword', views.search),

]


