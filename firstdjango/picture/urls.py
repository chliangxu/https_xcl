"""
URL configuration for firstdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

# 指定应用名称
app_name = 'picture'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('id/<int:Picture_id>', views.PictureID_view, name='PictureID'),
    path("info", views.info_view, name='info'),
    path("url", views.url_view, name='url'),
    path('filter', views.filter_view, name='filter'),
    path("template", views.template_view, name='template'),
    path("sta", views.static_view, name='static'),

]

