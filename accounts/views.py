from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from jobs.models import Job, Application

User = get_user_model()


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # role ke hisaab se redirect
            if user.user_type == 'employer':
                return redirect('employer_dashboard')
            else:
                return redirect('candidate_dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'accounts/login.html')


# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        # validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type=user_type   # IMPORTANT
        )

        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'accounts/register.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('home')


# ---------------- EMPLOYER DASHBOARD ----------------
@login_required
def employer_dashboard(request):
    jobs = Job.objects.filter(employer=request.user)

    total_applications = Application.objects.filter(
        job__employer=request.user
    ).count()

    return render(request, 'accounts/employer_dashboard.html', {
        'jobs': jobs,
        'total_applications': total_applications
    })


# ---------------- CANDIDATE DASHBOARD ----------------
@login_required
def candidate_dashboard(request):
    jobs = Job.objects.all()

    return render(request, 'accounts/candidate_dashboard.html', {
        'jobs': jobs
    })