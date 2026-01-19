from django.urls import path
from .views import customer_register, customer_dashboard, customer_login

urlpatterns = [
    path('register/', customer_register, name='customer_register'),
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
    path('login/', customer_login, name='customer_login'),
]