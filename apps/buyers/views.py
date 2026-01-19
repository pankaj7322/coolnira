from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def buyer_dashboard(request):
    if not request.user.is_buyer:
        return redirect('login')
    return render(request, 'buyers/dashboard.html')
