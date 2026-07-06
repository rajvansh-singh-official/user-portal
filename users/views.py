from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, AuthenticationForm, DocumentForm
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

def view_user(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    
    documents = user.documents.all()
    
    document_form = DocumentForm()

    if request.method == "POST":
        
        if "save_profile" in request.POST:
        
            user.username = request.POST.get("username")
        
            user.email = request.POST.get("email")
        
            user.save()
        
            return redirect("view_user", user_id=user.id)
        
        elif "upload_document" in request.POST:
            
            document_form = DocumentForm(request.POST, request.FILES)
            
            if document_form.is_valid():
                
                document = document_form.save(commit=False)

                document.user = user

                document.save()

                return redirect("view_user", user_id=user.id)

    return render(
        request,
        "auth/view_user.html",
        {
            "user": user,
            "documents": documents,
            "document_form": document_form, 
        }
    )