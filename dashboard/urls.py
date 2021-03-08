from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('line/', views.line, name='line'),
    path('media/', views.media, name='media'),
    path('price_list/', views.price_list, name='price_list'),
    path('contacts/', views.contacts, name='contacts'),
]
