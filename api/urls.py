from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('create-item/', views.create_item, name="create_item"),
  path('create-category/', views.create_category, name="create_category")
]

