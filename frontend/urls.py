from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.loadIndex),
  path('agregar-producto', views.loadAddProduct)
]

