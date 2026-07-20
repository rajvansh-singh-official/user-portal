from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .forms import (
    RegistrationForm,
    AuthenticationForm,
    DocumentForm,
    InterviewScheduleForm,
    QuestionForm,
    CategoryForm,
)
from .models import (
    Interview,
    Question,
    Option,
    Category,
)

# ===== AUTHENTICATION =====

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

# ===== DASHBOARD =====

def dashboard(request):

    users_count = User.objects.count()

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "users_count": users_count,
        },
    )

# ===== USERS =====

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
    
    user = get_object_or_404(User, pk=user_id)
    
    document_list = user.documents.all()
    interview_list = user.interviews.order_by("-scheduled_at")

    document_form = DocumentForm()
    
    if request.method == "POST":
        
        if "save_profile" in request.POST:
        
            user.username = request.POST.get("username")
        
            user.email = request.POST.get("email")
        
            user.save()
        
            return redirect("view_user", user_id=user.id)
        
        if "upload_document" in request.POST:
            
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
    
# ===== INTERVIEWS =====
    
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
    
# ===== QUESTIONS =====

# display label maps for filter chips
_DIFFICULTY_LABELS = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard",
}

_TYPE_LABELS = {
    "mcq": "MCQ",
    "true_false": "True / False",
    "short_answer": "Short Answer",
    "long_answer": "Long Answer",
}

_STATUS_LABELS = {
    "active": "Active",
    "inactive": "Inactive",
}

def questions(request):
    
    question_list = Question.objects.order_by("-created_at")
    
    search       = request.GET.get("search", "").strip()
    category     = request.GET.get("category", "")
    difficulty   = request.GET.get("difficulty", "")
    question_type = request.GET.get("type", "")
    status       = request.GET.get("status", "")

    if search:
        question_list = question_list.filter(
            question_text__icontains=search
        )
    
    if category:
        question_list = question_list.filter(
            category_id=category
        )
        
    if difficulty:
        question_list = question_list.filter(
            difficulty=difficulty
        )

    if question_type:
        question_list = question_list.filter(
            question_type=question_type
        )

    # fixed: status filter was captured but never applied
    if status:
        question_list = question_list.filter(
            is_active=(status == "active")
        )

    # resolve category name for the active filter chip
    selected_category_name = ""
    if category:
        try:
            selected_category_name = Category.objects.get(pk=category).name
        except Category.DoesNotExist:
            category = ""

    if request.method == "POST":

        if "create_category" in request.POST:

            category_form = CategoryForm(request.POST)

            if category_form.is_valid():
                category_form.save()
                return redirect("questions")

            question_form = QuestionForm()

        elif "create_question" in request.POST:

            question_form = QuestionForm(request.POST)
        
            if question_form.is_valid():

                question = question_form.save(commit=False)

                if question.question_type == "mcq":

                    options = [
                        request.POST.get("option_1"),
                        request.POST.get("option_2"),
                        request.POST.get("option_3"),
                        request.POST.get("option_4"),
                    ]

                    if not all(options):
                        question_form.add_error(
                            None,
                            "All four options are required for MCQ."
                        )

                    else:

                        question.save()

                        correct_option = int(request.POST.get("correct_option"))

                        for i, option_text in enumerate(options, start=1):

                            Option.objects.create(
                                question=question,
                                option_text=option_text,
                                is_correct=(i == correct_option),
                            )

                        return redirect("questions")

                elif question.question_type == "true_false":

                    question.save()

                    correct_option = request.POST.get("correct_option")

                    Option.objects.create(
                        question=question,
                        option_text="True",
                        is_correct=(correct_option == "true"),
                    )

                    Option.objects.create(
                        question=question,
                        option_text="False",
                        is_correct=(correct_option == "false"),
                    )

                    return redirect("questions")
        
                else:

                    question.save()

                    return redirect("questions")
            
    else:
        
        question_form = QuestionForm()
        category_form = CategoryForm()
        
    return render(
        request,
        "questions/questions.html",
        {
            "question_form": question_form,
            "category_form": category_form,
            "questions": question_list,

            # raw filter values (for preserving dropdown selected state)
            "search": search,
            "selected_category": category,
            "selected_difficulty": difficulty,
            "selected_type": question_type,
            "selected_status": status,

            # human-readable labels (for filter chips)
            "selected_category_name": selected_category_name,
            "selected_difficulty_label": _DIFFICULTY_LABELS.get(difficulty, ""),
            "selected_type_label": _TYPE_LABELS.get(question_type, ""),
            "selected_status_label": _STATUS_LABELS.get(status, ""),

            "categories": Category.objects.filter(is_active=True).order_by("name"),
        }
    )