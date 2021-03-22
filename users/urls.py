from django.urls import path, include
from . import views

urlpatterns = [
    path('line/add/', views.AddLine.as_view(), name='add-line'),
    path('line/update/<int:pk>/', views.UpdateLine.as_view(), name='line-update'),
    path('line/delete/<int:pk>/', views.DeleteLine.as_view(), name='line-delete'),
    # path('login/', views.login, name='login'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('accounts/', include("django.contrib.auth.urls")),
]
