from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('line/<int:pk>/', views.LineListView.as_view(), name='line'),
    path('price_list/<int:pk>/', views.PriceView.as_view(), name='price_list'),
    path('portfolio/<int:pk>/', views.MediaView.as_view(), name='media'),
    path('contacts/<int:pk>/', views.ContactView.as_view(), name='contacts'),
]
