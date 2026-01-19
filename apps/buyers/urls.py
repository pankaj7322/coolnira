from django.urls import path
from .views import buyer_dashboard

urlpatterns = [
    path('dashboard/', buyer_dashboard, name='buyer_dashboard'),
]
