from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    RegistrationForm,
    AuthenticationForm,
    DocumentForm,
    InterviewScheduleForm
)
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Interview

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

    return render(request, "users/users.html",
        {
            "users": users,
            "users_count": users_count,
            "search": search,
        },       
    )

def view_user(request, user_id):
    
    user = get_object_or_404(User, id=user_id)
    
    document_form = DocumentForm()
    
    document_list = user.documents.all()
    
    interview_list = user.interviews.order_by("-scheduled_at")

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
        "users/view_user.html",
        {
            "user": user,
            "document_form": document_form,
            "document_list": document_list,
            "interview_list": interview_list,
        }
    )
    
def interviews(request):
    
    user_id = request.GET.get("user")
    
    interview_list = Interview.objects.order_by("scheduled_at")
    
    if request.method == "POST":
        
        interview_form  = InterviewScheduleForm(request.POST)
        
        if interview_form.is_valid():
            
            interview_form.save()

            return redirect("interviews")
        
    else:
        
        initial = {}

        if user_id:

            try:

                initial["user"] = User.objects.get(pk=user_id)

            except User.DoesNotExist:

                pass

        interview_form = InterviewScheduleForm(
            initial=initial
        )
        
    return render(
        request,
        "interviews/interviews.html",
        {
            "interview_form": interview_form,
            "interviews": interview_list,
        }
    )   