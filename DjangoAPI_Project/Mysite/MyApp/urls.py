from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
# from MyApp import views

urlpatterns= [
    path('idealweight/', views.idealweight, name='idealweight')
]