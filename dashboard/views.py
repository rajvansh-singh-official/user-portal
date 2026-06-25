from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    
    users = User.objects.all()
    
    users_count = User.objects.count()

    return render(
        request, 
        "home.html",
        {
            'users': users,
            'users_count': users_count,
        }        
    )
