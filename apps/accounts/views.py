from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password = password)

#         if user is not None:
#             login(request, user)

#             if user.is_superuser:
#                 return redirect('admin_dashboard')
#             elif user.is_buyer:
#                 return redirect('buyer_dashboard')
#             elif user.is_customer:
#                 return redirect('customer_dashboard')
            
#         else:
#             return render(request, 'accounts/login.html',{
#                 'error': 'Invalid username or password'
#             })
#     return render(request, 'accounts/login.html')

def home(request):
    return render(request, 'home.html')

@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_dashboard')
    
    if request.method == "POST":
        username= request.POST.get("username")
        password= request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
    return render(request, "accounts/admin_login.html")