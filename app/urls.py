from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', menu_create),
    path('sub-menu/', sub_menu_create),
]