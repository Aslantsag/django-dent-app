from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='dashboard'),
    path('line/', views.LineListView.as_view(), name='line'),
    path('price_list/', views.PriceListView.as_view(), name='price_list'),
    path('price_list/add/', views.CreatePrice.as_view(), name='add-price'),
    path('price_list/update/<int:pk>/', views.UpdatePrice.as_view(), name='price-update'),
    path('price_list/delete/<int:pk>/', views.DeletePrice.as_view(), name='price-delete'),
    path('media/', views.MediaListView.as_view(), name='media'),
    path('media/add/', views.CreateMedia.as_view(), name='add-media'),
    path('media/update/update/<int:pk>/', views.UpdateMedia.as_view(), name='media-update'),
    path('media/update/delete/<int:pk>/', views.DeleteMedia.as_view(), name='media-delete'),
    path('contacts/', views.contacts, name='contacts'),
]
