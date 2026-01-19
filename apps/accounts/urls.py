from django.urls import path
from .views import admin_login, admin_dashboard, admin_logout

urlpatterns = [
    path('admin_login/', admin_login, name='admin_login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_logout/', admin_logout, name="admin_logout"),
]
