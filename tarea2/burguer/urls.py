from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hamburguesa/', views.burguer_index),
    path('hamburguesa/<int:burguer_id>/', views.burguer_detail),
    path('hamburguesa/<int:burguer_id>/ingrediente/<int:ingrediente_id>/',
         views.burguer_ingredient_change),
    path('ingrediente/', views.ingredient_index),
    path('ingrediente/<int:ingredient_id>/', views.ingredient_detail),
]
