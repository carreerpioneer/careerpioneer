from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job
from django.contrib.auth.views import LoginView


def get_jobs(request):
  jobs = Job.objects.all()
  context = {'jobs': jobs}
  return render(request, 'jobs/jobs.html', context)

def job_details(request, pk):
  job_obj = Job.objects.get(id=pk)
  context = {'job': job_obj}
  return render(request, 'jobs/job_detail.html', context)

def create_job(request):
  form = JobForm()

  if request.method == 'POST':
    form = JobForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('jobs')
  
  context = {'form': form}
  return render(request, 'jobs/job_form.html', context)

def update_job(request, pk):
  job = Job.objects.get(id=pk)
  form = JobForm(instance=job)

  if request.method == 'POST':
    form = JobForm(request.POST, instance=job)
    if form.is_valid():
      form.save()
      return redirect('jobs')

  context = {'form': form}
  return render(request, 'jobs/job_form.html', context)

def delete_job(request, pk):
  job = Job.objects.get(id=pk)

  if request.method == 'POST':
    job.delete()
    return redirect('jobs')

  context = {'object': job}
  return render(request, 'jobs/delete_template.html', context)






