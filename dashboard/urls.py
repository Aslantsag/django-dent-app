from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='dashboard'),
    path('line/', views.LineListView.as_view(), name='line'),
    # path('line/', views.line, name='line'),
    path('media/', views.media, name='media'),
    path('price_list/', views.PriceListView.as_view(), name='price_list'),
    path('price_list/add', views.CreatePrice.as_view(), name='add-price'),
    path('price_list/delete/<int:pk>/', views.UpdatePrice.as_view(), name='price-update'),
    path('price_list/delete/<int:pk>/', views.DeletePrice.as_view(), name='price-delete'),
    path('contacts/', views.contacts, name='contacts'),
]
