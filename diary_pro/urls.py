"""diary_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from diary_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('yearly/', views.yearly, name='yearly'),
    path('monthly/', views.monthly, name='monthly'),
    path('write/', views.write, name='write'),
    path('list/', views.list, name='list'),

    path('storage/', views.storage, name='storage'),
    path('storage_y/', views.storage_y, name='storage_y'),
    path('<int:id>/storage_yc/', views.storage_yc, name='storage_yc'),
    path('storage_m/', views.storage_m, name='storage_m'),

    path('<int:id>/',views.read, name='read'),

    path('add/',views.add, name='add'),

]
