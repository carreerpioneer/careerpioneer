from tempfile import tempdir
from django.shortcuts import render, redirect
from .forms import JobForm, PlatformForm , StatusForm
from .models import Job, Platform , Status
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
  return render(request, 'home.html')

class Login(LoginView):
  template_name = 'registration/login.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def get_jobs(request):
  jobs = Job.objects.filter(user=request.user)
  context = {'jobs': jobs}
  return render(request, 'jobs/jobs.html', context)
  
@login_required
def job_details(request, pk):
  job_obj = Job.objects.get(id=pk)
  context = {'job': job_obj}
  return render(request, 'jobs/job_detail.html', context)

@login_required
def create_job(request):
  form = JobForm()

  if request.method == 'POST':
    form = JobForm(request.POST)
    if form.is_valid():
      form.instance.user = request.user
      form.save()
      return redirect('jobs')
  
  context = {'form': form}
  return render(request, 'jobs/job_form.html', context)

@login_required
def update_job(request, pk):
  job = Job.objects.get(id=pk)
  form = JobForm(instance=job)

  if request.method == 'POST':
    form = JobForm(request.POST, instance=job)
    if form.is_valid():
      form.save()
      return redirect('jobs')

  context = {'form': form, 'job': job}
  print(context)
  return render(request, 'jobs/job_form.html', context)

@login_required
def delete_job(request, pk):
  job = Job.objects.get(id=pk)

  if request.method == 'POST':
    job.delete()
    return redirect('jobs')

  context = {'object': job}
  return render(request, 'jobs/delete_template.html', context)

@login_required
def platform(request):
  platform = Platform.objects.all()
  form = PlatformForm()
  if request.method == 'POST':
    form = PlatformForm(request.POST) 
    if form.is_valid():
      form.save()
      return redirect('create-platform')
  context = {'form': form, 'platform': platform}
  return render(request, 'jobs/platform_form.html', context)

@login_required
def delete_platform(request, pk):
  platform = Platform.objects.get(id=pk)
  if request.method == 'POST':
    platform.delete()
    return redirect('create-platform')
  context = {'object': platform}
  return render(request, 'jobs/delete_template.html', context)

@login_required
def create_status(request):
  form = StatusForm()
  status = Status.objects.all()

  if request.method == 'POST':
    form = StatusForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('status')

  context = {'form': form, 'status': status}
  return render(request, 'status/status.html', context)

@login_required
def delete_status(request, pk):
  status = Status.objects.get(id=pk)

  if request.method == 'POST':
    status.delete()
    return redirect('status')

  context = {'object': status}
  return render(request, 'status/delete_template.html', context)
