from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from demo.views import begin

urlpatterns = [
    path('test', begin, name='test'),
]
