from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import JobForm, ApplicationForm

def home(request):
    jobs = Job.objects.all().order_by('-id')  # latest first
    return render(request, 'jobs/home.html', {'jobs': jobs})
    
    if request.user.is_authenticated:
     applied_jobs = Application.objects.filter(candidate=request.user).values_list('job_id', flat=True)

     return render(request, 'jobs/home.html', {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    })

@login_required
def post_job(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary = int(request.POST.get('salary'))

        Job.objects.create(
            employer=request.user,
            title=title,
            description=description,
            location=location,
            salary=salary
        )

        return redirect('employer_dashboard')

    return render(request, 'jobs/post_job.html')


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Already applied check
    if Application.objects.filter(candidate=request.user, job=job).exists():
         messages.warning(request, "You already applied for this job.")
         return render(request, 'jobs/apply_job.html', {'job': job})

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.candidate = request.user
            application.job = job
            application.save()

            messages.success(request, "Application submitted successfully!")

    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})

@login_required
def create_job(request):
    if request.user.user_type != 'employer':
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('employer_dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/create_job.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def employer_jobs(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/employer_jobs.html', {'jobs': jobs})

def view_applications(request, job_id):
    job = Job.objects.get(id=job_id)
    applications = Application.objects.filter(job=job)

    return render(request, 'jobs/view_applications.html', {
        'job': job,
        'applications': applications
    })

@login_required
def my_jobs(request):
    jobs = Job.objects.filter(employer=request.user)
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})

def all_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/all_jobs.html', {'jobs': jobs})