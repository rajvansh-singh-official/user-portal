from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):

    search = request.GET.get("search", "")
    
    users = User.objects.all()

    if search:
        users = users.filter(username__icontains=search)
    
    users_count = User.objects.count()

    return render(
        request, 
        "home.html",
        {
            "users": users,
            "users_count": users_count,
            "search": search,
        },       
    )