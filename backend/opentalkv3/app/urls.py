from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get_csrf_token/', views.get_csrf_token),
    path('register/', views.register),
    path('user_login/', views.user_login),
    path('users/', views.add_user_to_sidebar),
    path('add_user_to_sidebar/', views.add_user_to_sidebar),

]