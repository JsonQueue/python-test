#-*- coding: utf-8 -*-
_author_ = 'slm'
_date_ = '2018/4/19 20:36'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add',views.add,name='add'),
    url(r'^delete',views.delete,name='del'),
    url(r'^update',views.update,name='up'),
    url(r'^chak',views.chak,name='chak')
]