from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('line/<int:pk>/', views.line, name='line'),
    path('price_list/<int:pk>/', views.price_list, name='price_list'),
    path('portfolio/<int:pk>/', views.media, name='media'),
    path('contacts/<int:pk>/', views.contacts, name='contacts'),
]
