from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

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
            print("Success!")
            user = form.get_user()
            login(request, user)
            return redirect("/")
        
        else:
            print(form.errors)
            
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", 
    {
        "form": form
    })

def logout_view(request):
    logout(request)
    return redirect("/login/")

def edit_user(request, user_id):
    
    editing_user = User.objects.get(id=user_id)

    if request.method == "POST":
        editing_user.username = request.POST.get("username")
        editing_user.email = request.POST.get("email")
        editing_user.save()
        return redirect("/")

    return render(request, "auth/edit_user.html",
    {
        "editing_user": editing_user 
    })