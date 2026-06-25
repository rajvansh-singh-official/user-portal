from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import login, logout

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
