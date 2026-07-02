from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def register(request):
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
            
    else:
        form = RegistrationForm()

    return render(request, "auth/register.html", 
    {
        "form": form
    })

def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
            
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", 
    {
        "form": form
    })

def logout_view(request):
    logout(request)
    return redirect("login")

def users(request):

    search = request.GET.get("search", "")
    
    users = User.objects.all()

    if search:
        users = users.filter(username__icontains=search)
    
    users_count = User.objects.count()

    return render(request, "users.html",
        {
            "users": users,
            "users_count": users_count,
            "search": search,
        },       
    )

def edit_user(request, user_id):
    
    editing_user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        editing_user.username = request.POST.get("username")
        editing_user.email = request.POST.get("email")
        editing_user.save()
        return redirect("users")

    return render(request, "auth/edit_user.html",
    {
        "editing_user": editing_user 
    })