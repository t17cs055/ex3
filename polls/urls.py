'''
Created on 2019/10/18

@author: t17cs055
'''
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
]
