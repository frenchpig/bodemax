from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('', views.loadIndex),
  path('agregar-producto', views.loadAddProduct),
  path('ver-productos', views.loadViewProducts),
  path('logout/', auth_views.LogoutView.as_view(),name='logout'),
  path('login/',views.loadViewLogin, name='login'),
  path('crear-solicitud',views.loadViewSolicitud, name='crear-solicitud'),
  path('ver-solicitudes',views.loadViewVerSolicitudes, name='ver-solicitudes'),
]

