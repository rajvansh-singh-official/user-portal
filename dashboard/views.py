from django.shortcuts import render
from django.contrib.auth.models import User

def dashboard(request):
    
    users_count = User.objects.count()

    return render(
        request, 
        "dashboard/dashboard.html",
        {
            "users_count": users_count,
        },       
    )