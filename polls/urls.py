'''
Created on 2022/10/21

@author: t20cs059
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]