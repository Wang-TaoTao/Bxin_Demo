"""Bxin_one URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('apps.index.urls')),

    url(r'^graphql', GraphQLView.as_view(graphiql=True))


]

from django.conf.urls import url
from karazhan.base import site as karazhan_site
urlpatterns += [url(r'^karazhan/', karazhan_site.urls)]



