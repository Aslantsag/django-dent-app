from django.urls import path, include
from . import views

urlpatterns = [
    path('line/add/', views.AddLine.as_view(), name='add-line'),
    path('line/<int:pk>/update/', views.update_line, name='line-update'),
    path('line/<int:pk>/delete/', views.delete_line, name='line-delete'),
    # path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('accounts/', include("django.contrib.auth.urls")),
]
