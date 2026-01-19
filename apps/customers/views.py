
from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Customer

User = get_user_model()

def customer_login(request):
    if request.user.is_authenticated:
        return redirect('customer_dashboard')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and not user.is_superuser:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, "Invalid customer credentials")

    return render(request, "customers/customer_login.html")


def customer_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('customer_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('customer_register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('customer_register')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create customer profile
        Customer.objects.create(
            user=user,
            phone=phone,
            address=address
        )

        # Auto login
        login(request, user)
        return redirect('customer_dashboard')

    return render(request, 'customers/customer_register.html')

@login_required
def customer_dashboard(request):
    return render(request, "customers/customer_dashboard.html")

